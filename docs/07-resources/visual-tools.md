# 12 类图表与模拟器：教学重建

> 非官方学习资料。图形由本站代码重建，不是获奖团队原图。核查于 2026-10-12。

## 1. 全球赛事阶段时间轴

<div class="flow-grid" markdown>
<div class="flow-card"><strong>Activation</strong><p>2026-08-27 至 10-29<br>注册、组队、Lean Canvas<br>截止 23:59 CT</p></div>
<div class="flow-card"><strong>Innovation</strong><p>2027-01-07<br>Brief、视频、网站与付款<br>截止 23:59 CT</p></div>
<div class="flow-card"><strong>Finalists</strong><p>2027 年 2 月<br>公布与反馈<br>具体日期未确认</p></div>
<div class="flow-card"><strong>Summit</strong><p>2027-04-21 至 24<br>休斯敦展示与答辩</p></div>
</div>

以 [正式指南](https://conrad.spacecenter.org/wp-content/uploads/2026/08/2026-2027-Conrad-Challenge-Student-Guide-Official.pdf) 为准；[官网日期冲突](../01-overview/timeline.md) 已单独说明。

## 2. DiveGuard 市场层次与口径提醒

<div class="flow-grid">
<div class="flow-card"><strong>TAM：124 亿美元</strong><p>底稿中的行业总额口径。</p></div>
<div class="flow-card"><strong>SAM：2.16 亿美元</strong><p>底稿中的可服务市场估计。</p></div>
<div class="flow-card"><strong>SOM：648 万美元</strong><p>底稿中的可获得市场估计。</p></div>
</div>

这些为团队申报，旅游总额与设备市场口径不同，故不画成严格嵌套集合或按面积暗示比例。真正可获得市场需要客户、区域、年份和收入单位一致。[完整说明](../04-business/market-sizing.md)。

## 3–5. 三个本地交互财务模型

[打开全部计算器](../04-business/calculators.md)：BeeGuard 订阅模型、DiveGuard 销量盈亏平衡、家庭安装价/节约/寿命模型。默认参数和复位按钮完整保留；全部教学模拟。

## 6. 三种利润情景

<div class="scenario-chart" data-scenario-chart></div>

教学模拟：利润 = (单价 − 单位变动成本) × 销量 − 固定成本。保守 -16,000 元，基准 -4,000 元，乐观 13,000 元。亏损画在零点左侧，不用正值遮盖。参数原表见 [BOM 与情景](../04-business/competition.md)。

## 7. BeeGuard 多模态诊断管线

<div class="flow-grid">
<div class="flow-card"><strong>输入</strong><p>蜂群视频、音频与行为记录</p></div>
<div class="flow-card"><strong>分析</strong><p>视觉特征、声学特征与行为追踪</p></div>
<div class="flow-card"><strong>诊断</strong><p>异常识别与结果解释</p></div>
<div class="flow-card"><strong>验证</strong><p>不同蜂群/季节的误报、漏报与复用意愿</p></div>
</div>

这是技术理解示意；不能证明队伍已完成所有模块。训练测试划分和原始数据仍需查证。[案例](../02-projects/beeguard.md)。

## 8. RescueBot 反馈与安全停止

<div class="flow-grid">
<div class="flow-card"><strong>命令与自检</strong><p>目标距离、电池、急停、传感器状态</p></div>
<div class="flow-card"><strong>控制器</strong><p>读取里程与障碍反馈，判断状态</p></div>
<div class="flow-card"><strong>正常执行</strong><p>限速驱动；到达后停车并启动警示</p></div>
<div class="flow-card"><strong>异常优先</strong><p>障碍、断连、超时、急停 → 安全停止</p></div>
</div>

传感反馈在每个周期回到控制器。故障后需要人工确认再复位，不能自动重启。[状态机伪代码与测试矩阵](../03-engineering/rescuebot.md)。

## 9. 四页商业答辩

<div class="flow-grid">
<div class="flow-card"><strong>Problem & Customers</strong><p>痛点、真实客户、访谈与现有成本。</p></div>
<div class="flow-card"><strong>Savings & Payback</strong><p>实验节约、同工况基准与回收期。</p></div>
<div class="flow-card"><strong>Market & Competitors</strong><p>可达市场、替代方案与短板。</p></div>
<div class="flow-card"><strong>Cost & Business Model</strong><p>BOM、定价、盈亏平衡、下一轮验证。</p></div>
</div>

教学展示框架，不是官方规定的四页提交格式。[英文示范与七个问题](../04-business/pitch.md)。

## 10. 学生负责的三个工作组

<div class="flow-grid">
<div class="flow-card"><strong>工程与技术</strong><p>结构、程序、集成、测试证据。</p></div>
<div class="flow-card"><strong>市场与商业</strong><p>访谈、竞品、报价与计算。</p></div>
<div class="flow-card"><strong>文书与展示</strong><p>英文叙述、来源、演示与答辩。</p></div>
</div>

学生负责人统筹决策，成员可跨组；成人导师支持资源、安全和方法。每周学生会议、每两周导师审查。[职责与会议](../05-team/roles.md)。

## 11. Markdown 单源与双部署

<div class="flow-grid">
<div class="flow-card"><strong>开发 dev</strong><p>正式 Markdown 与本地资源<br>内部资料排除</p></div>
<div class="flow-card"><strong>审查 → main</strong><p>内容、来源、隐私与构建验收<br>首次发布取得确认</p></div>
<div class="flow-card"><strong>GitHub Pages</strong><p>静态构建<br>/conrad-team-hub/ 子路径</p></div>
<div class="flow-card"><strong>阿里云</strong><p>同一正文的静态构建<br>独立域名根路径 /</p></div>
</div>

没有第二份手工维护的正文。两个目标的相对资产、搜索和深层页面分别测试。[部署说明](website-project.md)。

## 12. 资料站布局示意

<div class="wireframe">
<div class="wireframe-head">顶部：八栏目与搜索</div>
<div class="wireframe-side">左栏：栏目与页面<br><br>手机端折叠到菜单</div>
<div class="wireframe-body">正文：导读、详细段落、公式、表格、案例<br><br>右侧或折叠目录：页内定位<br><br>底部：来源与延伸阅读</div>
</div>

宽表格只在自身容器横向滚动，公式使用本地字体。网站是学习资料，不使用商业广告式首屏。
