import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="生醫視覺產生器 Pro", layout="wide")
st.title("🧬 生醫科研視覺產生器")

if "OPENAI_API_KEY" not in st.secrets:
    st.error("❌ 找不到 API Key")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

with st.sidebar:
    st.header("🎨 科研參數設定")
    
    subject_zh = st.selectbox("1. 核心主體", [
        "發光的細胞核與 DNA 鏈 (Nucleus)", 
        "蛋白質分子三維結構 (Protein)",
        "脂質雙層膜與受體 (Cell Membrane)",
        "NK 細胞攻擊癌症顆粒 (Immunotherapy)",
        "外泌體釋放過程 (Exosomes)",
        "現代自動化實驗室 (Bio-Lab)",
        "奈米藥物載體 (Nanoparticles)"
    ])
    
    style_zh = st.selectbox("2. 視覺風格", ["寫實 3D 渲染 (專業感)", "電子顯微鏡攝影 (質感)", "扁平化科學插畫 (簡約)"])
    color_zh = st.selectbox("3. 品牌色系", ["企業深藍", "生機螢光綠", "純淨白", "高端黑金", "科技紫"])
    ratio_zh = st.radio("4. 圖片比例", ["16:9 橫向", "1:1 正方形", "9:16 直向"])

size_map = {"16:9 橫向": "1792x1024", "1:1 正方形": "1024x1024", "9:16 直向": "1024x1792"}
target_size = size_map[ratio_zh]

# 背後指令強化：加入 "Scientific accurate" 與 "Photorealistic"
final_prompt = f"Professional {style_zh} of {subject_zh}, {color_zh} theme, highly detailed, scientific accuracy, cinematic lighting, 8k, octane render, biology laboratory aesthetic."

if st.button("🚀 開始繪製科研影像", type="primary"):
    with st.spinner("AI 正在解析生物結構中..."):
        try:
            response = client.images.generate(
                model="dall-e-3", prompt=final_prompt, size=target_size, quality="hd"
            )
            st.image(response.data[0].url, use_container_width=True)
            st.success("✅ 生成完成！")
            
            with st.expander("📝 查看此影像的科學描述詞"):
                st.code(final_prompt)
        except Exception as e:
            st.error(f"❌ 錯誤：{e}")
