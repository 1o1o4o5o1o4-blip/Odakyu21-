// search.js
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

async function searchForum(query) {
    const url = `https://scratchdb.lefty.one{encodeURIComponent(query)}&order=newest`;
    
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
        const data = await response.json();
        
        console.log(`--- "${query}" の検索結果: ${data.length}件 ---`);
        data.slice(0, 10).forEach(post => {
            console.log(`【${post.username}】 ${post.time.posted}`);
            console.log(`URL: https://scratch.mit.edu{post.id}/`);
            console.log("-".repeat(20));
        });
    } catch (error) {
        console.error("エラーが発生しました:", error.message);
    }
}

// 検索したいワードを入れて実行
const keyword = process.argv[2] || "拡張機能";
searchForum(keyword);
