import streamlit as st
import urllib.parse

st.title("Scratchフォーラム検索（Google経由）")

query = st.text_input("検索キーワード", value="拡張機能")
username = st.text_input("ユーザー名（任意）")

if st.button("検索実行"):
    # Googleで「site:scratch.mit.edu/discuss」を指定して検索するURLを作成
    search_terms = f"site:scratch.mit.edu/discuss {query} {username}".strip()
    encoded_query = urllib.parse.quote(search_terms)
    google_url = f"https://www.google.com{encoded_query}"
    
    st.success("接続エラーを回避するため、Google検索リンクを生成しました。")
    st.markdown(f"### [👉 ここをクリックして検索結果を表示]({google_url})")
    
    st.info("※サーバーの制限により直接データを取得できないため、ブラウザで公式フォーラムを直接検索します。")
