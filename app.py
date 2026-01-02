import streamlit as st
from openai import OpenAI

# 頁面標題
st.set_page_config(page_title="生醫視覺產生器", layout="wide")
st.title("🧬 基因與細胞治療 AI 繪圖工具")

# 安全讀取 Secrets
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("❌ 尚未在 Secrets 中設定 API Key")
    st.stop()

# 側邊欄選單
with st.sidebar:
    st.header("🎨 設定")
    subject = st.selectbox("1. 選擇主體", ["DNA Helix", "Immune Cells", "Laboratory", "Stem Cells"])
    vibe = st.radio("2. 選擇氛圍", ["Tech-Blue", "Warm", "Minimalist"])

# 生成按鈕
if st.button("🚀 生成圖片"):
    with st.spinner("AI 繪製中..."):
        try:
            prompt = f"Professional medical 3D visualization of {subject}, {vibe} style, 8k, scientific accuracy."
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1792",
                quality="hd"
            )
            st.image(response.data[0].url)
            st.success("完成！右鍵即可儲存。")
        except Exception as e:
            st.error(f"錯誤：{e}")
