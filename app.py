import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="生醫視覺產生器 Pro", layout="wide")
st.title("🧬 基因與細胞治療 - 進階 AI 繪圖工具")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- 側邊欄：進階選單 ---
with st.sidebar:
    st.header("🎨 視覺自定義")
    
    # 1. 主體
    subject = st.selectbox("核心主體", [
        "DNA Double Helix", "T-Cells attacking tumor", 
        "Stem Cells division", "Exosomes", "Laboratory robotic arm",
        "Patient receiving cell therapy"
    ])
    
    # 2. 風格
    style = st.selectbox("視覺風格", [
        "Photorealistic 3D Render", "Electron Microscope (SEM) Style", 
        "Minimalist Vector Illustration", "Cinematic Film Still"
    ])
    
    # 3. 色系
    color_theme = st.select_slider("品牌色系", options=["Deep Blue", "Bio-Green", "Clean White", "High-contrast Black"])
    
    # 4. 比例 (DALL-E 3 支援 square, wide)
    ratio = st.radio("圖片比例", ["1024x1792 (16:9 橫向)", "1024x1024 (1:1 方型)"])

# --- 生成邏輯 ---
if st.button("🚀 生成高品質圖像"):
    # 根據選單動態組合 Prompt
    # 我們在這裡加入一些固定增益詞來維持「高級感」
    final_prompt = (
        f"A professional {style} of {subject}. "
        f"Primary color theme: {color_theme}. "
        f"Features: scientific accuracy, high-end medical visualization, "
        f"4k resolution, octane render, trending on artstation, "
        f"clean composition, soft depth of field."
    )
    
    with st.spinner("AI 專家正在繪圖中..."):
        try:
            # 判斷比例設定
            size_param = "1792x1024" if "16:9" in ratio else "1024x1024"
            
            response = client.images.generate(
                model="dall-e-3",
                prompt=final_prompt,
                size="1024x1792", # DALL-E 3 橫向需固定此格式或根據官方參數調整
                quality="hd"
            )
            
            st.image(response.data[0].url)
            st.info(f"當前 Prompt 邏輯：{final_prompt}") # 讓業務知道背後跑了什麼，增加學習感
        except Exception as e:
            st.error(f"錯誤：{e}")
