# 双平台部署技术规范

- 网站源码使用 MkDocs + Material，适合结构化多篇 Markdown；版本应固定到经测试的兼容版本，不随意使用 latest。
- 建议统一 `use_directory_urls: false`，降低双部署路径歧义；两套配置应核实 GitHub Pages 子路径与阿里云根路径。
- GitHub 构建 `site_url: https://wenxilian.github.io/conrad-team-hub/`；阿里云构建 `site_url: https://<approved-domain>/`。不要在提交前猜测实际服务器域名。
- 使用自定义 `mkdocs.github.yml`、`mkdocs.aliyun.yml`，或脚本生成临时配置；Markdown 和资产保持唯一来源。CSS/JS 尽量本地，避免依赖 GitHub raw 与外部 CDN。
- 自动化部署优先 GitHub Actions (Pages)；阿里云优先由授权用户复制完整 build 目录到 Nginx 静态站根目录。不要提交 SSH key、API key、真实域名访问凭证到 GitHub。
- 若需要离线双击 HTML 阅读，单独生成 offline profile；官方 MkDocs 文档指出 file:// 模式存在 search 等限制，不能以服务器访问成功推断离线可用。
- 每个发布版本产生 git commit SHA、构建日期和部署清单；部署后抓取关键页面并检查 asset 200 状态。
- 用户可从另一站点访问完整静态目录，前提是 Nginx 正确配置路径、缓存与 MIME 类型。

参考：https://www.mkdocs.org/user-guide/deploying-your-docs/ 及 https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/configuration.md

## 第一版实际构建

运行 tools/build.py，生成 dist/github/conrad-team-hub 与 dist/aliyun；后者以时间戳 ZIP 打包。生产域名尚未确认，阿里云配置不指定虚构地址，链接使用相对路径。

GitHub 需在 wenxilian 授权确认后创建仓库；首次发布必须用户验收批准。dev 提交开发成果，审核后才建立/合并 main 并开启 Pages (Source: GitHub Actions)。

阿里云部署将 ZIP 解压至批准的 Nginx 站点目录，保留完整 assets 与 search 子目录。Nginx 配置包括 index index.html，try_files $uri $uri/ =404；不要把整个内部项目目录当 Web 根目录。配置由管理员按真实域名/服务器审查后执行，不索取凭据。

本地模拟验证：在 dist/github 启 HTTP 8001，访问 /conrad-team-hub/；在 dist/aliyun 启 HTTP 8002，访问 /。相对资源、深层页面、搜索和公式分别检查。
