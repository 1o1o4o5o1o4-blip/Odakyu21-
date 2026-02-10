import requests

def search_scratch_forum(query=None, username=None):
    """
    Scratchフォーラムを用語やユーザー名で検索する
    """
    # ScratchDBの検索エンドポイント
    url = "https://scratchdb.lefty.one"
    
    # 検索パラメータの設定
    params = {
        "q": query,       # 検索キーワード
        "user": username, # ユーザー名
        "order": "newest" # 新しい順
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if not data:
            print("該当する投稿が見つかりませんでした。")
            return

        print(f"--- 検索結果: {len(data)}件 ---")
        for post in data[:10]:  # 直近10件を表示
            print(f"【{post['username']}】 {post['time']['posted']}")
            # 内容の冒頭を表示（HTMLタグを簡易除去する場合は別途処理が必要）
            content = post['content'][:100].replace('\n', ' ')
            print(f"内容: {content}...")
            print(f"URL: https://scratch.mit.edu{post['id']}/")
            print("-" * 30)
            
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# --- 実行例 ---
# 1. 特定のキーワードで検索
search_scratch_forum(query="拡張機能")

# 2. 特定のユーザーの投稿を検索
# search_scratch_forum(username="griffpatch")
