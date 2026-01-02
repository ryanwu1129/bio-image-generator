{\rtf1\ansi\ansicpg950\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
\
# 1. \uc0\u35373 \u32622 \u20171 \u38754 \u27161 \u38988 \u33287 \u29986 \u26989 \u39080 \u26684 \
st.set_page_config(page_title="\uc0\u29983 \u37291 \u23560 \u26989 \u35222 \u35258 \u29986 \u29983 \u22120 ", layout="wide")\
st.title("\uc0\u55358 \u56812  \u22522 \u22240 \u33287 \u32048 \u32990 \u27835 \u30274  - \u26989 \u21209 \u23560 \u23660  AI \u32362 \u22294 \u24037 \u20855 ")\
st.write("\uc0\u21482 \u38656 \u36984 \u25799 \u38364 \u37749 \u23383 \u65292 \u21363 \u21487 \u29983 \u25104 \u36969 \u21512 \u31777 \u22577 \u30340 \u39640 \u36074 \u24863 \u27675 \u22285 \u22294 \u12290 ")\
\
# --- \uc0\u20596 \u37002 \u27396 \u65306 \u26989 \u21209 \u36984 \u21934  ---\
with st.sidebar:\
    st.header("\uc0\u55356 \u57256  \u22294 \u29255 \u21443 \u25976 \u35373 \u23450 ")\
    \
    # \uc0\u20027 \u39636 \u36984 \u25799 \
    subject = st.selectbox("1. \uc0\u36984 \u25799 \u35222 \u35258 \u20027 \u39636 ", [\
        "DNA \uc0\u38617 \u34746 \u26059  (DNA Helix)", \
        "\uc0\u20813 \u30123 \u32048 \u32990 \u25915 \u25802 \u30284 \u32048 \u32990  (Immune cells vs Cancer)", \
        "\uc0\u23526 \u39511 \u23460 \u31185 \u23416 \u23478  (Scientists in Lab)", \
        "\uc0\u24185 \u32048 \u32990 \u32080 \u27083  (Stem Cell Structure)",\
        "\uc0\u37291 \u30274 \u25976 \u25818 \u33287 \u22522 \u22240 \u22294 \u35676  (Medical Data/Genomics)"\
    ])\
    \
    # \uc0\u27675 \u22285 \u36984 \u25799 \
    vibe = st.radio("2. \uc0\u36984 \u25799 \u22294 \u29255 \u27675 \u22285 ", [\
        "\uc0\u39640 \u31185 \u25216 \u31934 \u28310  (Tech-Blue)", \
        "\uc0\u28331 \u26262 \u33287 \u24076 \u26395  (Warm & Hopeful)", \
        "\uc0\u26997 \u31777 \u23560 \u26989  (Minimalist White)"\
    ])\
    \
    # \uc0\u27604 \u20363 \u36984 \u25799 \
    aspect_ratio = st.selectbox("3. \uc0\u31777 \u22577 \u27604 \u20363 ", ["16:9 (\u38928 \u35373 )", "4:3", "1:1"])\
\
# --- \uc0\u24460 \u21488 \u65306 \u25552 \u31034 \u35422 \u32068 \u21512 \u37007 \u36655  ---\
# \uc0\u26681 \u25818 \u36984 \u21934 \u65292 \u24460 \u21488 \u33258 \u21205 \u36681 \u25563 \u28858 \u24375 \u22823 \u30340  AI \u25552 \u31034 \u35422 \
vibe_map = \{\
    "\uc0\u39640 \u31185 \u25216 \u31934 \u28310  (Tech-Blue)": "futuristic laboratory, blue glowing lights, holographic elements, sharp focus, cinematic lighting",\
    "\uc0\u28331 \u26262 \u33287 \u24076 \u26395  (Warm & Hopeful)": "soft natural light, bright, optimistic atmosphere, warm color palette, human-centric",\
    "\uc0\u26997 \u31777 \u23560 \u26989  (Minimalist White)": "clean white background, high-end medical aesthetics, sharp details, studio lighting, professional photography"\
\}\
\
# \uc0\u26680 \u24515 \u25552 \u31034 \u35422 \u20778 \u21270 \u65306 \u21152 \u20837 \u29983 \u37291 \u29986 \u26989 \u24517 \u20633 \u30340 \u39640 \u36074 \u24863 \u27161 \u31844 \
base_prompt = f"Professional medical visualization of \{subject\}, \{vibe_map[vibe]\}, 8k resolution, highly detailed, octane render, scientific accuracy, masterpiece."\
\
# --- \uc0\u21069 \u31471 \u23637 \u31034  ---\
st.subheader("\uc0\u55357 \u56541  \u38928 \u35336 \u29983 \u25104 \u30340 \u25552 \u31034 \u35422  (\u33258 \u21205 \u32068 \u21512 \u20013 )")\
st.code(base_prompt, language="text")\
\
if st.button("\uc0\u55357 \u56960  \u38283 \u22987 \u29983 \u25104 \u22294 \u29255  (\u38656 \u35201 \u20018 \u25509  API)"):\
    st.info("\uc0\u36889 \u35041 \u23559 \u26371 \u20018 \u25509  DALL-E 3 \u25110  Midjourney API\u65292 \u22294 \u29255 \u38928 \u35336 \u22312  10 \u31186 \u20839 \u29983 \u25104 ...")\
    # \uc0\u27492 \u34389 \u21152 \u20837  API \u21628 \u21483 \u20195 \u30908 \
    # st.image(generated_url)\
    st.warning("\uc0\u30446 \u21069 \u28858 \u28436 \u31034 \u29256 \u26412 \u65292 \u23526 \u38555 \u20018 \u25509 \u24460 \u21363 \u21487 \u30452 \u25509 \u19979 \u36617 \u22294 \u29255 \u33267 \u31777 \u22577 \u20351 \u29992 \u12290 ")}