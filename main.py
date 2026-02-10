from IPython.display import HTML, display

html_code = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Scratch Forum 爆速検索ツール</title>
    <style>
        body { font-family: sans-serif; display: flex; justify-content: center; padding: 50px; background: #f0f2f5; }
        .card { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 100%; max-width: 500px; border-top: 8px solid #855cd6; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #855cd6; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; font-size: 1.1em; }
        button:hover { background: #6b46b8; }
        .info { font-size: 0.85em; color: #666; margin-top: 15px; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="card">
        <h2 style="color: #855cd6; margin-top:0;">🚀 Scratch Forum Search</h2>
        <p>GitHub上で動く「規制回避型」検索ツールです。</p>

        <input type="text" id="q" placeholder="キーワード (例: 拡張機能)">
        <input type="text" id="u" placeholder="ユーザ名 (任意)">

        <button onclick="search()">フォーラムを検索する</button>

        <div class="info">
            <b>仕組み:</b> このツールはPythonサーバーを通さず、ブラウザから直接Googleのインデックスを叩くため、<b>通信規制(Error 113等)が絶対に起きません。</b>
        </div>
    </div>

    <script>
        function search() {
            const q = document.getElementById('q').value;
            const u = document.getElementById('u').value;
            if(!q && !u) return alert("キーワードかユーザ名を入れてください");

            // site検索コマンドを作成
            let query = `site:scratch.mit.edu/discuss ${q}`;
            if(u) query += ` "${u}"`;

            // Google検索へジャンプ
            window.open(`https://www.google.com/search?q=${encodeURIComponent(query)}`, '_blank');
        }
    </script>
</body>
</html>
"""

display(HTML(html_code))
