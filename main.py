import streamlit as st

# 1. 画面の見た目をスッキリさせる
st.set_page_config(layout="centered", page_title="Scratch Search")
st.title("⚡️ 爆速検索")

# 2. 入力欄（Enterキーですぐに反応するように設定）
q = st.text_input("キーワード入力 → Enter", placeholder="例: 拡張機能 user:abee")

if q:
    # Googleの高度な検索（site:指定）を1秒で生成
    url = f"https://www.google.com+{q}"
    
    # 3. リンクをデカデカと表示（迷わせない）
    st.markdown(f"""
        <a href="{url}" target="_blank" style="
            display: inline-block;
            padding: 15px 25px;
            background-color: #ff4b4b;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            font-size: 20px;
            width: 100%;
            text-align: center;
        ">🚀 フォーラムで検索結果を見る</a>
    """, unsafe_allow_html=True)

st.caption("※サーバー負荷を避けるため、直接Googleのインデックスを参照します。")
