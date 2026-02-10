name: JS Search Runner
on:
  workflow_dispatch: # ボタン一発で実行
    inputs:
      keyword:
        description: '検索ワード'
        required: true
        default: '拡張機能'

jobs:
  run-search:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - name: Install dependencies
        run: npm install node-fetch
      - name: Run Script
        run: node search.js "${{ github.event.inputs.keyword }}"
