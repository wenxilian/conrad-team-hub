# 12 类图表与模拟器：教学重建

有些概念看图会更容易理解，所以我把时间轴、市场规模、控制流程和财务模拟器集中放在这里。大家可以直接试着调整参数，也可以回到对应章节看完整解释。

这些图表是按资料重建的学习工具，财务数字属于教学模拟；它们不代表获奖团队的原始图表或实际经营结果。

## 1. 全球赛事阶段时间轴

<div class="flow-grid flow-sequence" markdown>
<div class="flow-card"><strong>Activation</strong><p>2026-08-27 至 10-29<br>注册、组队、Lean Canvas<br>截止 23:59 CT</p></div>
<div class="flow-card"><strong>Innovation</strong><p>2027-01-07<br>Brief、视频、网站与付款<br>截止 23:59 CT</p></div>
<div class="flow-card"><strong>Finalists</strong><p>2027 年 2 月<br>公布与反馈<br>具体日期未确认</p></div>
<div class="flow-card"><strong>Summit</strong><p>2027-04-21 至 24<br>休斯敦展示与答辩</p></div>
</div>

以 [正式指南](https://conrad.spacecenter.org/wp-content/uploads/2026/08/2026-2027-Conrad-Challenge-Student-Guide-Official.pdf) 为准；[官网日期冲突](../01-overview/introduction.md#timeline) 已单独说明。

## 2. DiveGuard 市场层次与口径提醒

<div class="flow-grid">
<div class="flow-card"><strong>TAM：124 亿美元</strong><p>全球潜水旅游行业总额。</p></div>
<div class="flow-card"><strong>SAM：2.16 亿美元</strong><p>智能潜水设备市场估计。</p></div>
<div class="flow-card"><strong>SOM：648 万美元</strong><p>初期东南亚目标市场估计。</p></div>
</div>

这些为团队申报，旅游总额与设备市场口径不同，故不画成严格嵌套集合或按面积暗示比例。真正可获得市场需要客户、区域、年份和收入单位一致。[完整说明](../04-business/diveguard-case.md#market-sizing)。

## 3–5. 三个本地交互财务模型

[打开全部计算器](../04-business/calculators.md)：BeeGuard 订阅模型、DiveGuard 销量盈亏平衡、家庭安装价/节约/寿命模型。默认参数和复位按钮完整保留；全部教学模拟。

## 6. 三种利润情景

<div class="scenario-chart" data-scenario-chart></div>

教学模拟：利润 = (单价 − 单位变动成本) × 销量 − 固定成本。保守 -16,000 元，基准 -4,000 元，乐观 13,000 元。亏损画在零点左侧，不用正值遮盖。参数原表见 [BOM 与情景](../04-business/household-hardware.md#competition)。

## 7. BeeGuard 多模态诊断管线

<div class="relationship-figure"><div class="diagram-branches"><div class="diagram-node">蜂群视频<br><small>视觉特征</small></div><div class="diagram-node">蜂群音频<br><small>声学特征</small></div><div class="diagram-node">行为记录<br><small>追踪与时间特征</small></div></div><div class="diagram-root">↓ 多模态分析与异常识别 ↓</div><div class="diagram-support">验证：不同蜂群、季节、视频条件下的误报、漏报与复用意愿</div><p class="figure-caption">教学技术管线；团队原始数据与全部模块实现仍需核实。</p></div>

这是技术理解示意；不能证明队伍已完成所有模块。训练测试划分和原始数据仍需查证。[案例](../02-projects/beeguard.md)。

## 8. RescueBot 反馈与安全停止

<div class="relationship-figure">
<div class="diagram-row"><div class="diagram-node">启动命令与自检<br><small>目标、急停、电池</small></div><span class="diagram-arrow">→</span><div class="diagram-node">控制器<br><small>检查里程、障碍与状态</small></div><span class="diagram-arrow">→</span><div class="diagram-node">正常执行<br><small>限速驱动 → 到达停车、亮灯</small></div></div>
<div class="feedback-label">↑ 传感器反馈：每个控制周期回到控制器</div>
<div class="diagram-alert">异常分支：障碍 / 断连 / 超时 / 急停 → 关闭电机、安全停止 → 人工确认后复位</div>
<p class="figure-caption">教学控制示意，不是获奖队伍的原始控制图。异常处理优先于正常执行。</p></div>

传感反馈在每个周期回到控制器。故障后需要人工确认再复位，不能自动重启。[状态机伪代码与测试矩阵](../03-engineering/programming.md#rescuebot)。

## 9. 四页商业答辩

<div class="flow-grid">
<div class="flow-card"><strong>Problem & Customers</strong><p>痛点、真实客户、访谈与现有成本。</p></div>
<div class="flow-card"><strong>Savings & Payback</strong><p>实验节约、同工况基准与回收期。</p></div>
<div class="flow-card"><strong>Market & Competitors</strong><p>可达市场、替代方案与短板。</p></div>
<div class="flow-card"><strong>Cost & Business Model</strong><p>BOM、定价、盈亏平衡、下一轮验证。</p></div>
</div>

教学展示框架，不是官方规定的四页提交格式。[英文示范与七个问题](../04-business/five-models.md#pitch)。

## 10. 学生负责的三个工作组

<div class="relationship-figure"><div class="diagram-root">学生负责人：统筹与决策</div><div class="diagram-branches"><div class="diagram-node">工程与技术<br><small>结构、代码、集成、测试</small></div><div class="diagram-node">市场与商业<br><small>访谈、竞品、成本、计算</small></div><div class="diagram-node">文书与展示<br><small>英文、来源、演示、答辩</small></div></div><div class="diagram-support">成人导师支持：方法、资源与安全；学生承担研究与提交</div><p class="figure-caption">教学组织图。职能可以交叉，三个工作组不等于三名学生。</p></div>

学生负责人统筹决策，成员可跨组；成人导师支持资源、安全和方法。每周学生会议、每两周导师审查。[职责与会议](../05-team/mentors.md#roles)。

## 11. Markdown 单源与双部署

<div class="relationship-figure"><div class="diagram-row"><div class="diagram-node">Markdown 单源<br><small>dev 开发</small></div><span class="diagram-arrow">→</span><div class="diagram-node">审核通过的 main</div><span class="diagram-arrow">→</span><div class="diagram-node">静态构建</div></div><div class="diagram-branches"><div class="diagram-node">GitHub Pages<br><small>/conrad-team-hub/</small></div><div class="diagram-node">阿里云<br><small>独立域名根路径 /</small></div></div><p class="figure-caption">两套部署共享同一正文；首次发布仍需验收确认。</p></div>

没有第二份手工维护的正文。两个目标的相对资产、搜索和深层页面分别测试。[部署说明](source-method.md#website)。

## 12. 资料站布局示意

<div class="wireframe">
<div class="wireframe-head">顶部：八栏目与搜索</div>
<div class="wireframe-side">左栏：栏目与页面<br><br>手机端折叠到菜单</div>
<div class="wireframe-body">正文：导读、详细段落、公式、表格、案例<br><br>右侧或折叠目录：页内定位<br><br>底部：来源与延伸阅读</div>
</div>

宽表格只在自身容器横向滚动，公式使用本地字体。网站是学习资料，不使用商业广告式首屏。
