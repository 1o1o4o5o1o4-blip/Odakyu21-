import streamlit as st
import requests
import time

# 1. データの読み込み（ページをめくって限界まで取る！）
@st.cache_data(ttl=300) # 5分間はデータを保存して速く動くようにするよ
def load_all_comments():
    all_comments = []
    # 0ページ目から24ページ目まで（最大1000件）繰り返す
    for page in range(25):
        # 1ページあたり40件ずつ取る設定（offset）
        offset = page * 40
        url = f"https://api.scratch.mit.edu/studios/51326987/comments?offset={offset}&limit=40"
        
        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()
            
            # データが空っぽになったら終了
            if not data or len(data) == 0:
                break
                
            for c in data:
                all_comments.append({
                    "id": c.get("id"),
                    "user": c.get("author", {}).get("username", "不明"),
                    "datetime": c.get("datetime_created", ""),
                    "content": c.get("content", ""),
                })
            
            # Scratchのサーバーに負担をかけないように一瞬だけ休憩
            time.sleep(0.1)
            
        except:
            break # エラーが起きたらそこまでで止める
            
    return all_comments

# アプリの見た目
st.set_page_config(page_title="過疎スタ限界検索", page_icon="🚀")
st.title("過疎スタ 限界突破検索アプリ")
st.caption("最新から最大1000件をまとめて取得中...")

# 2. 実行
with st.spinner("過疎スタの深くまで潜ってデータを取っています..."):
    comments_list = load_all_comments()

# サイドバーで検索
with st.sidebar:
    st.header("検索フィルタ")
    user_q = st.text_input("ユーザー名")
    text_q = st.text_input("キーワード")

# 3. 検索処理
results = [c for c in comments_list if user_q.lower() in c["user"].lower() and text_q.lower() in c["content"].lower()]

# 4. 表示
st.write(f"### 取得した {len(comments_list)} 件中、{len(results)} 件がヒット！")

for c in results:
    with st.container():
        st.markdown(f"**{c['user']}** <small style='color:gray'>{c['datetime']}</small>", unsafe_allow_html=True)
        st.write(c["content"])
        st.divider()
