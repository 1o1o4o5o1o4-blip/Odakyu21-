import streamlit as st
import requests

# 1. データの読み込み
@st.cache_data(ttl=60)
def load_data():
    # 本物の過疎スタ（スタジオID: 51326987）
    url = "https://api.scratch.mit.edu/studios/51326987/comments"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

# 2. データの整理（ここでエラーが起きないように工夫したよ！）
comments_list = []
try:
    data = load_data()
    
    # data自体がリスト（[ ]で囲まれたもの）になっているかチェック
    if isinstance(data, list):
        for c in data:
            # メインのコメントを追加
            comments_list.append({
                "id": c.get("id"),
                "user": c.get("author", {}).get("username", "不明"),
                "datetime": c.get("datetime_created", ""),
                "content": c.get("content", ""),
                "is_reply": False
            })
    else:
        st.error("データの形が予想と違いました。")

except Exception as e:
    st.error(f"データの読み込みに失敗しました: {e}")
    st.stop()

# 3. アプリの見た目
st.title("過疎スタ リアルタイム検索")
st.caption("最新のコメントを検索できるよ！")

# 検索メニュー
with st.sidebar:
    user_q = st.text_input("ユーザー名で検索")
    text_q = st.text_input("内容で検索")

# 4. 検索処理
results = comments_list
if user_q:
    results = [c for c in results if user_q.lower() in c["user"].lower()]
if text_q:
    results = [c for c in results if text_q.lower() in c["content"].lower()]

# 5. 結果の表示
st.write(f"### 結果: {len(results)} 件")

for c in results:
    st.markdown(f"**{c['user']}** `{c['datetime']}`")
    st.write(c["content"])
    st.divider()
