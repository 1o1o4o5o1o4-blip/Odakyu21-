import streamlit as st
import requests

# 1. データの読み込み（ここを本物の過疎スタAPIに変えたよ！）
@st.cache_data(ttl=60) # 60秒ごとに最新をチェックするようにしたよ
def load_data():
    # 本物の過疎スタ（スタジオID: 51326987）のコメントを取得する住所
    url = "https://api.scratch.mit.edu/studios/51326987/comments"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

# 2. データの準備
try:
    data = load_data()
    comments_list = []
    
    # 本物のScratchデータ（API）の形に合わせて読み取り方を変えたよ
    for c in data:
        comments_list.append({
            "id": c["id"],
            "user": c["author"]["username"], # APIではここが名前
            "datetime": c["datetime_created"],
            "content": c["content"],
            "is_reply": False
        })
        # ※APIの基本設定ではリプライ（返信）は別で取る必要があるから、
        # まずはメインのコメントだけが表示されるようになっているよ！
except Exception as e:
    st.error(f"データの読み込みに失敗しました: {e}")
    st.stop()

# 3. アプリの見た目
st.title("過疎スタ リアルタイム検索")
st.caption("今の過疎スタの最新コメントを表示中！")

user_q = st.sidebar.text_input("ユーザー名で検索")
text_q = st.sidebar.text_input("内容で検索")

# 4. 検索と表示
results = [c for c in comments_list if user_q.lower() in c["user"].lower() and text_q.lower() in c["content"].lower()]

st.write(f"### 最新のコメント: {len(results)} 件")

for c in results:
    st.markdown(f"**{c['user']}** `{c['datetime']}`")
    st.write(c["content"])
    st.divider()
