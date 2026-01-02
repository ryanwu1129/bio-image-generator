import streamlit as st
from openai import OpenAI

# 1. 頁面基本配置
st.set_page_config(page_title="生醫視覺產生器 Pro", layout="wide")
st.title("🧬 基因與細胞治療 - 進階 AI 繪圖工具")
st.write("透過參數化設定，快速生成適合簡報、官網或社群的高端生醫影像。")

# 2. 安全讀取 Secrets 裡的 API Key
if "OPENAI_API_KEY" not in st.secrets:
    st.error("❌ 請先在 Streamlit Secrets 中設定 OPENAI_API_KEY")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- 側邊欄：進階參數設定 ---
with st.sidebar:
    st.header("🎨 視覺參數設定")
    
    # 選擇主體 (針對您的產業優化)
    subject = st.selectbox("1. 核心主體", [
        "DNA Double Helix, glowing atoms", 
        "NK cells attacking a tumor cell", 
        "CAR-T cell therapy mechanism",
        "Mesenchymal Stem Cells (MSC) colony",
        "Exosomes being released from a cell",
        "Modern automated bio-laboratory",
        "Scientist looking at a glowing viral vector"
    ])
    
    # 選擇風格
    style = st.selectbox("2. 視覺風格", [
        "Photorealistic 3D Render", 
        "Scanning Electron Microscope (SEM) style", 
        "Cinematic Medical Documentary",
        "Professional Scientific Illustration",
        "Abstract High-tech Digital Art"
    ])
    
    # 選擇品牌色系
    color_theme = st.selectbox("3. 品牌色系", [
        "Deep Corporate Blue (深邃企業藍)", 
        "Bioluminescent Green (生機螢光綠)", 
        "Clinical Pure White (臨床純淨白)", 
        "Luxury Dark & Gold (高端黑金)",
        "Vibrant Purple & Blue (基因科技紫藍)"
    ])

    # 選擇視角
    view_angle = st.radio("4. 構圖視角", ["Macro (極致微距特寫)", "Eye-level (平視專業感)", "Isometric (等距立體視角)"])
    
    # 選擇比例 (這部分已修正 API 對應邏輯)
    ratio_choice = st.radio("5. 圖片比例", ["16:9 橫向 (簡報用)", "1:1 正方形", "9:16 直向 (手機用)"])

# --- 後台邏輯計算 ---
# 根據選擇的比例轉換
