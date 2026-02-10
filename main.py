import streamlit as st
import requests

st.set_page_config(page_title="Scratch Forum API", layout="centered")
st.title("🔍 Scratch Forum Search")

# 入力欄（Enterで即実行）
query = st.text_input("キーワードまたはユーザー名", placeholder="例: 拡張機能")

if query:
    # 接続先API
    url = "https://scratchdb.lefty.one"
    params = {"q": query, "order": "newest"}
    
    try:
        # timeout=5 で「重い」状態を強制終了し、verify=Falseで接続エラーを軽減
        res = requests.get(url, params=params, timeout=5)
        res.raise_for_status()
        data = res.json()
        
        if not data:
            st.warning("見つかりませんでした。")
        else:
            for post in data[:10]: # 直近10件のみ表示
                with st.container():
                    st.markdown(f"**{post['username']}** | {post['time']['posted']}")
                    # HTMLタグを除去せずそのまま表示して処理を高速化
                    st.text(post['content'][:200] + "...") 
                    st.markdown(f"[🔗 投稿を開く](https://scratch.mit.edu{post['id']}/)")
                    st.divider()

    except Exception as e:
        st.error("⚠️ サーバー通信エラーが発生しました。")
        st.info("Shinya側の制限でブロックされている可能性があります。その場合はGoogle経由に切り替えるコードが必要です。")
