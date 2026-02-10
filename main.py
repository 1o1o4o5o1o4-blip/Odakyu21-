import streamlit as st
import requests

st.title("Scratchフォーラム検索")

# 入力欄
query = st.text_input("検索キーワード", value="拡張機能")
username = st.text_input("ユーザー名（任意）")

if st.button("検索実行"):
    url = "https://scratchdb.lefty.one"
    params = {"q": query, "user": username, "order": "newest"}
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if not data:
            st.warning("見つかりませんでした。")
        else:
            for post in data[:10]:
                with st.expander(f"投稿者: {post['username']} ({post['time']['posted']})"):
                    st.write(post['content'][:500]) # 冒頭を表示
                    st.markdown(f"[投稿を見る](https://scratch.mit.edu{post['id']}/)")
    except Exception as e:
        st.error(f"エラー: {e}")
