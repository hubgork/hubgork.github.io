# hubgork.github.io

个人站 GitHub Pages 主仓（空脚手架）。旧预览已归档到 [hub-read/pages-archive](https://github.com/hub-read/pages-archive)。

用法：新建顶层子文件夹，放入 `index.html`，push 到 `main`。根目录 `index.html` 由 `scripts/build-index.py` 在 Actions 构建时自动生成（不要手改提交），按最近提交时间列出含 `index.html` 的子目录。

- 标题取自页面 `<title>`；可选 `meta.json`：`{"title":"...","description":"..."}` 覆盖。
- 只放非机密内容。
- 推送后约 20–40 秒上线。
