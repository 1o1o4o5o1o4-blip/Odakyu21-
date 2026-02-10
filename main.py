import urllib.parse
from IPython.display import display, HTML

# --- 設定 ---
query = "拡張機能" # 検索したいキーワード
username = ""     # 特定のユーザーで絞り込むなら入力（例: "abee"）
# -----------

def generate_scratch_search(q, u):
    # Googleに「Scratchフォーラム内だけを検索」と命令する特殊コマンド
    # site: はドメイン指定、inurl: はURLに特定の文字を含むものに限定
    base_query = f"site:scratch.mit.edu/discuss {q}"
    if u:
        base_query += f' "{u}"' # ユーザー名を引用符で囲んで精度アップ
        
    encoded_query = urllib.parse.quote(base_query)
    search_url = f"https://www.google.com{encoded_query}"
    
    html = f'''
    <div style="font-family: sans-serif; padding: 20px; border: 2px solid #855cd6; border-radius: 10px; background-color: #f9f7ff;">
        <h2 style="color: #855cd6; margin-top: 0;">🚀 Scratchフォーラム 確実検索</h2>
        <p>キーワード: <b>{q}</b> {f' | ユーザー: <b>{u}</b>' if u else ''}</p>
        <p style="font-size: 0.9em; color: #666;">
            ※APIやスクレイピングがブロックされる環境でも、このリンクなら公式の最新データを安全に表示できます。
        </p>
        <a href="{search_url}" target="_blank" style="
            display: inline-block;
            background-color: #855cd6;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            box-shadow: 0 4px #5c3fa1;
        ">👉 検索結果を今すぐ表示する</a>
    </div>
    '''
    display(HTML(html))

# 実行
generate_scratch_search(query, username)
