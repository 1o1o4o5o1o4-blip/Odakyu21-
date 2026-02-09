import streamlit as st
import requests

# 1. データの読み込み（shinyaさんのGitHubから取得）
@st.cache_data
def load_data():
    # 正しいRawデータのURL
    url = "https://raw.githubusercontent.com/hd3a/kasosuta-dataset/refs/heads/main/scratch_shinya_all.json"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

# 2. データの準備
try:
    data = load_data()
    comments_list = []
    
    # JSONの中身を使いやすいように整理する
    for c in data.get("comments", []):
        # 親コメント
        comments_list.append({
            "id": c["id"],
            "user": c["user"],
            "datetime": c["datetime"],
            "content": c["content"],
            "is_reply": False
        })
        # 返信（リプライ）も追加
        for r in c.get("replies", []):
            comments_list.append({
                "id": r["id"],
                "user": r["user"],
                "datetime": r["datetime"],
                "content": r["content"],
                "is_reply": True
            })
except Exception as e:
    st.error(f"データの読み込みに失敗しました: {e}")
    st.stop()

# 3. アプリの見た目（UI）
st.set_page_config(page_title="過疎スタ ログ検索", page_icon="📝")
st.title("過疎スタ ログ検索アプリ")
st.caption("Created by ncyo / Data source: hd3a")

# 検索フォーム
with st.sidebar:
    st.header("検索設定")
    user_q = st.text_input("ユーザー名で検索")
    text_q = st.text_input("内容で検索")

# 4. 検索処理
results = comments_list

if user_q:
    results = [c for c in results if user_q.lower() in c["user"].lower()]
if text_q:
    results = [c for c in results if text_q.lower() in c["content"].lower()]

# 5. 結果の表示
st.write(f"### 検索結果: {len(results)} 件")

if not results:
    st.info("見つかりませんでした。キーワードを変えてみてね。")
else:
    # ページネーション（一度に200件表示）
    page_size = 200
    total_pages = (len(results) + page_size - 1) // page_size
    page = st.number_input("ページ番号", min_value=1, max_value=total_pages, value=1)
    
    start = (page - 1) * page_size
    end = start + page_size

    for c in results[start:end]:
        prefix = "↳ " if c["is_reply"] else ""
        # 読みやすく色分け
        st.markdown(f"**{prefix}{c['user']}** `{c['datetime']}`  \n{c['content']}  \n(ID:{c['id']})")
        st.divider()
