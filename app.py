import streamlit as st
from openai import OpenAI

# 1. 頁面基本配置
st.set_page_config(page_title="生醫視覺產生器 Pro", layout="wide")
st.title("🧬 基因與細胞治療 - 進階 AI 繪圖工具")

# 2. 安全讀取 Secrets 裡的 API Key
if "OPENAI_API_KEY" not in st.secrets:
    st.error("❌ 請先在 Streamlit Secrets 中設定 OPENAI_API_KEY")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- 側邊欄設定 ---
with st.sidebar:
    st.header("🎨 視覺參數設定")
    subject = st.selectbox("核心主體", [
        "DNA Double Helix, glowing atoms", 
        "NK cells attacking a tumor cell", 
        "CAR-T cell therapy mechanism",
        "Mesenchymal Stem Cells (MSC) colony",
        "Exosomes being released from a cell",
        "Modern automated bio-laboratory"
    ])
    style = st.selectbox("視覺風格", ["Photorealistic 3D Render", "Scanning Electron Microscope (SEM) style", "Professional Scientific Illustration"])
    color_theme = st.selectbox("品牌色系", ["Deep Corporate Blue", "Bioluminescent Green", "Clinical Pure White", "Luxury Dark & Gold"])
    ratio_choice = st.radio("圖片比例", ["16:9 橫向 (簡報用)", "1:1 正方形", "9:16 直向 (手機用)"])

# --- 比例轉換邏輯 ---
if ratio_choice == "16:9 橫向 (簡報用)":
    target_size = "1792x1024"
elif ratio_choice == "9:16 直向 (手機用)":
    target_size = "1024x1792"
else:
    target_size = "1024x1024"

# --- 主畫面顯示 ---
st.subheader("🖼️ 準備生成")
st.write(f"**當前設定：** {subject} / {style} / {ratio_choice}")

# 🚀 確保按鈕在這裡 (不可以在 sidebar 的縮排內)
if st.button("🚀 開始生成高品質影像", type="primary"):
    final_prompt = f"A professional {style} of {subject}, color theme: {color_theme}, highly detailed, scientific accuracy, 8k resolution, cinematic lighting."
    
    with st.spinner("AI 繪製中..."):
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=final_prompt,
                size=target_size,
                quality="hd",
                n=1
            )
            st.image(response.data[0].url, caption="生成完成！右鍵即可另存圖片")
            st.success("✅ 成功！")
        except Exception as e:
            st.error(f"❌ 錯誤：{e}")
