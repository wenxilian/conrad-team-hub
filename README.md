# Conrad Challenge 团队参赛与创新实践指南

非官方独立学习资料，面向学生和家长。赛事、13 案例、工程测试、商业算例与团队规划。规则及案例核查日期：2026-10-12。

## 安装与本地预览

当前已建 .venv。新机器使用 Python 3.11：

~~~powershell
python -m venv .venv
& ./.venv/Scripts/python.exe -m pip install -r requirements-lock.txt
& ./.venv/Scripts/python.exe -m mkdocs serve -a 127.0.0.1:8000
~~~

浏览器打开 http://127.0.0.1:8000/。通过 HTTP 读取，不把双击 HTML 当作搜索验收。

## 构建与检查

~~~powershell
& ./.venv/Scripts/python.exe tools/build.py
& ./.venv/Scripts/python.exe tools/validate_site.py
~~~

GitHub 产物在 dist/github/conrad-team-hub/，阿里云在 dist/aliyun/。ZIP 仅包含静态网站。KaTeX、字体、搜索与模拟器本地化。

## 目录与发布

docs/ 为正文、空白模板和本地资源；tools/ 为构建、验证及预览；GitHub Actions 只发布 main。dev 保存开发，main 只接收用户审核后的正式版本。

原始 sources/、规划 planning/ 和日志 logs/ 不提交。首次对外发布等待用户确认。目标账号 wenxilian，仓库 wenxilian/conrad-team-hub；不得覆盖 lianxhcn 配置。用 gh auth status 核实授权；Git 提交身份与推送账号不同。

公开暂存使用明确文件名单，禁止 git add .。不上传真实工程秘密、受访者身份或凭据。阿里云域名待批准，不猜实际地址。

## 限制与排错

中国站信息、原始实验、独立官网及图片许可有缺口，页面已标注。全文 PDF 与真实项目图片尚未完成。缺逐字原稿，不宣称 95% 内容恢复。

严格构建报断链时修复目标，勿关闭检查。缺公式时检查本地 KaTeX 与字体。Git 安全目录提示可在本次命令用 -c safe.directory=项目绝对路径；不修改全局配置。

KaTeX 0.16.22 使用 MIT 许可，原许可保存在资源目录。

## 连续阅读改造

根据阅读反馈，主导航改为29个入口。赛事、工程、商业基础、家庭硬件、团队、执行和来源按完整信息块合并；13案例有连续全览，也保留独立页。旧短页作为兼容网址保留，从主导航与搜索中排除。图表和模拟器放回相关正文，不只在工具箱中集中展示。原动态图片未随v3导出，原图检索线索和许可缺口继续保留。
