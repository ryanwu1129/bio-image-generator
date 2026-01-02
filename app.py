import streamlit as st
from openai import OpenAI

# 1. 頁面基本設定
st.set_page_config(page_title="生醫視覺產生器", layout="wide")
st.title("🧬 基因與細胞治療 - 業務專屬 AI 繪圖工具")

# 2. 安全讀取 Secrets 裡的 API Key
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception as e:
    st.error("請先在 Streamlit Secrets 中設定 OPENAI_API_KEY")
    st.stop()

# --- 側邊欄選單 ---
with st.sidebar:
    st.header("🎨 圖片參數設定")
    subject = st.selectbox("1. 選擇視覺主體", [
        "DNA Double Helix, glowing technology style", 
        "Immune cells attacking cancer cells, microscopic view", 
        "Scientists working in a futuristic biotech lab", 
        "Stem cell structure, organic and professional",
        "Genomic data visualization on a medical screen"
    ])
    
    vibe = st.radio("2. 選擇圖片氛圍", ["Tech-Blue (科技冷藍)", "Warm & Hopeful (溫馨希望)", "Minimalist White (極簡專業)"])
    
# 氛圍邏輯轉換
vibe_map = {
    "Tech-Blue (科技冷藍)": "futuristic blue lighting, cinematic, high-tech",
    "Warm & Hopeful (溫馨希望)": "soft natural light, bright, empathetic, optimistic",
    "Minimalist White (極簡專業)": "clean white background, sharp focus, medical journal style"
}

# --- 執行按鈕 ---
if st.button("🚀 生成簡報專用圖片"):
    # 組合最終提示詞
    final_prompt = f"Professional medical 3D visualization of {subject}, {vibe_map[vibe]}, highly detailed, 8k resolution, octane render, scientific accuracy."
    
    with st.spinner("AI 正在為您繪製中，請稍候約 10-15 秒..."):
        try:
            # 呼叫 DALL-E 3
            response = client.images.generate(
                model="dall-e-3",
                prompt=final_prompt,
                size="1024x1792",  # 生成 9:16 或 16:9 比例 (取決於模型支援)
                quality="hd",
                n=1
            )
            
            # 顯示結果
            image_url = response.data[0].url
            st.image(image_url, caption="點擊右鍵即可另存圖片至簡報中使用")
            st.success("生成成功！")
            
        except Exception as e:
            st.error(f"生成失敗，請檢查 API Key 或額度是否充足。錯誤訊息: {e}")
