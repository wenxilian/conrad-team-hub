---
search:
  exclude: true
---

# 图片位置、原检索线索与可视化清单

完整上下文已合并到 [连续阅读章节](source-method.md#media)，本页保留原链接兼容。

> 资料性质：图位与重建记录 / 待取得媒体许可。整理与核查日期：2026-10-12。本站为非官方独立学习资料。

> 这是原聊天中的**插图位置与原始检索描述清单**，并非已提取到的原图文件地址。聊天使用了动态图片检索组件 (`AsyncImage` / `AsyncImageGroup`)，其 `query` 提供的是搜索描述，不是图片 URL。不能把检索描述假装为原图链接。图片需要 Codex 重新搜寻并核验版权、来源和匹配关系；优先链接到赛事或学校的原始报道页面，不要直接盗链或使用带水印图片。网站应保留图位，即使暂缺图片。

| 原讨论中的位置 | 原始图片检索描述 (供重新检索) | 建议链接/处理 |
|---|---|---|
| 赛事介绍、总决赛现场 | `Conrad Challenge student innovators Innovation Summit Space Center Houston team presentation` | https://conrad.spacecenter.org/ |
| 赛事介绍、学生路演 | `Conrad Challenge students team project pitch competition Space Center Houston` | https://conrad.spacecenter.org/ |
| 竞赛领域：航空航天 | `student model rocket aerospace engineering science project prototype` | 教学配图，注明非对应参赛作品 |
| 竞赛领域：网络安全 | `student cybersecurity programming laptop technology science competition` | 教学配图 |
| 竞赛领域：能源环境 | `school science fair renewable energy solar panel wind turbine prototype` | 教学配图 |
| 竞赛领域：健康营养 | `student health biomedical engineering wearable health monitor prototype` | 教学配图 |
| 竞赛领域：水资源 | `water quality sensor testing device environmental science student project` | 教学配图 |
| Soaring Seeds 项目图 | `2026 Conrad Challenge Soaring Seeds smart backwashing safe water system China team` | https://conrad.spacecenter.org/2026-awards/ |
| DiveGuard 项目图 | `2026 Conrad Challenge DiveGuard China underwater acoustic communication student team` | https://conrad.spacecenter.org/2026-awards/ |
| VisionBridge 项目图 | `2026 Conrad Challenge VisionBridge China visually impaired AI glasses smart cane team` | https://conrad.spacecenter.org/2026-awards/ |
| OctoScope 项目图 | `2026 Conrad Challenge OctoScope China canal underwater monitoring student team` | https://conrad.spacecenter.org/2026-awards/ |
| FireAIDSS 获奖队伍 | `Conrad Challenge 2025 FireAIDSS Swarmthinkers Sarah Huang wildfire drone swarm team` | https://conrad.spacecenter.org/2025-winners/ |
| FireAIDSS 工程演示 | `wildfire mapping quadcopter drone thermal camera field test` | 示意配图，注明非获奖团队真实试验 |
| Aphelion 项目图 | `Conrad Challenge 2026 Aphelion Landon Kummer Tobin Palmer Brandon Kirbyson satellite steering` | https://conrad.spacecenter.org/2026-awards/ |
| Aphelion 控制结构图 | `spherical motor multi axis actuator laboratory engineering prototype` | 示意配图 |
| Aphelion 电机试验台 | `satellite gimbal actuator engineering test bench motor position encoder` | 示意配图 |
| BeeGuard 项目图 | `2026 Conrad Challenge BeeGuard Ethan Liang Rory Hu honeybee AI beehive project` | https://conrad.spacecenter.org/2026-awards/ |
| OncoMap 项目图 | `2026 Conrad Challenge OncoMap The Cartographers Anshul Raghav Krishay Singh` | https://conrad.spacecenter.org/2026-awards/ |
| RescueBot 项目图 | `Conrad Challenge 2024 Running Bits RescueBot automatic warning triangle robot` | https://conrad.spacecenter.org/2024-conrad-challenge-innovation-summit-awards/ |
| RescueBot 机器人结构示意 | `small mobile robot chassis ultrasonic sensor obstacle avoidance arduino prototype` | 示意配图 |
| 家庭产品成本类示意 | `student science fair renewable energy engineering prototype` | 仅当有必要时使用 |

## 原来并非真实图片链接的插图

原聊天中还展示了若干**即时生成的图形组件和交互模拟器**，其图形没有独立可引用的远程 URL。请在网站以本地代码重建，而不是截取聊天页面截图：

1. 赛事流程时间轴：2026–2027 报名和总决赛阶段，核对本届官方日期。
2. 商业模型分层示意：DiveGuard 的 TAM / SAM / SOM 套层图；明确三个市场数字口径并不严格嵌套。
3. BeeGuard SaaS 模拟器：用户数 `N=300`，月费 `P=10 USD`，月单位可变成本 `2 USD`；年度收入 `R=12NP`，年度边际贡献 `12N(P-VC)`；交互改变客户数、价格和成本。**教学数据**。
4. DiveGuard 硬件盈亏平衡模拟器：`P=150 USD`，`VC=90 USD`，`F=12000 USD`，`Q*=200`；销量调节。**教学数据**。
5. 家庭产品节约模拟器：购置成本 `P=600 RMB`，年净节约 `S=240 RMB`，寿命 5 年；回收期 2.5 年，寿命期简单净节约 600 元；画成本曲线。**教学数据**。
6. 三种利润情景柱图：保守 `-16000`、基准 `-4000`、乐观 `13000` 元。**教学数据**。
7. BeeGuard 多模态管线：蜂群视频/音频 → 计算机视觉/声学分析/行为追踪 → 异常诊断。
8. RescueBot 控制流程：启动命令 → 控制器 → 电机执行和传感反馈 → 安全停止。
9. 四页商业答辩幻灯片缩略图：Problem & Customers、Savings & Payback、Market & Competitors、Cost & Business Model。
10. 项目管理三工作组结构图：工程与技术、市场与商业、文书与展示，在学生负责人统筹和成人导师支持下运行。
11. GitHub → 静态构建 → GitHub Pages / 阿里云双部署示意图。
12. 网站左侧目录与正文栏的布局线框图。

**重建要求**：使用 Mermaid、SVG、Plotly 或原生 JS；交互模拟器的初始参数、公式和教学数据标记必须保留；图表适配手机与打印版。


本轮未复制未获许可的官方照片。13 个案例页保留来源页和图位；三个财务模拟器与全部 12 类教学可视化已代码重建，见 [可视化工具页](visual-tools.md)。原图与完整 PDF 仍待处理。

资料边界与更正记录见 [来源核查](source-method.md)。
