# FireAIDSS：从火情信息到无人机协作

面对火情，一个系统需要经历感知、判断和行动几个环节。FireAIDSS 把 AI 与无人机协作放在一起，为我们提供了一个拆解系统工程的例子：哪些任务依赖数据，哪些任务依赖控制与通信？

这里按技术管线介绍能力要求和测试思路。学生不必一开始就承担全部复杂功能，可以先选择一个能安全验证的环节，再说明它与整个系统的关系。


<figure class="case-photo">
<a href="https://conrad.spacecenter.org/2025-winners/" target="_blank" rel="noopener"><img src="https://conrad.spacecenter.org/wp-content/uploads/2025/10/微信图片_20250112133658-1024x575.jpeg" alt="FireAIDSS 在官方获奖介绍中的项目配图" loading="lazy" decoding="async"></a>
<figcaption>FireAIDSS 的官方介绍配图。<a href="https://conrad.spacecenter.org/2025-winners/">图片与项目介绍来源：2025 年获奖档案</a>。核查于 2026-10-12。</figcaption>
<p class="photo-unavailable" hidden>这张官方图片暂时未能载入，可以<a href="https://conrad.spacecenter.org/2025-winners/">打开项目原始报道</a>查看。</p>
</figure>

## 官方名录核查

2025，Swarmthinkers，中国，Energy & Environment Power Pitch；官网确认无人机群与3D火势预测描述，未确认PINN细节、中国站金奖或实战成熟度。来源：[年度官方档案](https://conrad.spacecenter.org/2025-winners/)，核查于 2026-10-12。奖项可核实；性能、市场与财务数字属于官方转述的团队申报或预测。

## 项目背景与技术路线

该案例适合学习无人机与应急监测的系统思路。官方名录确认，Swarmthinkers 是中国学生团队，获得 2025 年 Energy & Environment Power Pitch；中国站金奖的说法仍待正式资料确认。官方资料确认无人机群与三维火势预测的方案描述；我们此前还讨论过传感器与物理信息神经网络 (PINN)，但公开摘要尚不足以确认其具体实现。官网摘要不足以确认多机自主飞行的实际成熟度、公开代码、训练数据或真实误差。不能把「使用了 PINN」等同于证明已经达到实战部署要求。

教学拆解：

- 平台：无人机载荷、供电、传感器、GPS / IMU。
- 数据：图像、热成像、时间与位置标记，Python/NumPy/Pandas/OpenCV。
- 模型：由简化传播模型到有物理约束的学习模型，比较 baseline。
- 多机：先实现模拟中的任务分配、覆盖率和路径规划，再考虑实体系统集成。
- 测试：火源分割的 precision / recall / F1；传播预测误差 MAE / RMSE、空间偏移；覆盖率与延迟；异常工况表现。
- 安全：用公开数据、模拟、无燃烧替代场景，不能自行制造真实火情。

## 工程原理、程序模块与实验建议

### 技术管线

`公开或合法采集的图像/热成像 + 风速/风向/地形 → 时间同步与位置配准 → 火情区域提取 → 简化传播基线 → 改进预测模型 → 风险地图 → 模拟监测任务调度`。

<div class="relationship-figure"><div class="diagram-branches"><div class="diagram-node">图像 / 热成像<br><small>合法采集或公开数据</small></div><div class="diagram-node">风向、风速、地形<br><small>时间同步与位置配准</small></div></div><div class="diagram-root">↓ 火情区域提取与数据处理 ↓</div><div class="diagram-row"><div class="diagram-node">简化传播基线</div><span class="diagram-arrow">→</span><div class="diagram-node">改进预测与误差比较</div><span class="diagram-arrow">→</span><div class="diagram-node">风险地图与监测任务模拟</div></div><p class="figure-caption">教学技术管线。PINN具体实现及多机实飞成熟度未核实；用公开数据与安全模拟验证。</p></div>

第一阶段可先完成离线图像处理；第二阶段使用公开数据进行传播预测；第三阶段仅在模拟环境展示多机任务调度。不应先承诺已经实现多无人机自主实飞。PINN 的具体实现尚待进一步资料确认。作为一个可探讨的技术方向，PINN 是物理信息神经网络，教学时要说明偏微分/物理约束与损失函数的关系，但高中生不必从头研发复杂物理求解器。

### 必要编程栈

Python、NumPy、Pandas、OpenCV、Matplotlib 作为入门；可根据需要加入 PyTorch。飞行任务模拟可参考 PX4 或 ArduPilot，但必须确认开源许可、安全边界、硬件匹配及学生是否真正理解调用方式。

### 试验设计

1. 图像检测：测试集中含不同光照、烟雾背景，记录 TP、FP、FN，计算 Precision、Recall 和 F1；避免训练数据与测试数据混用。
2. 传播预测：采用有标注时间序列，比较简单恒速传播基准与改进模型，用 MAE、RMSE、空间重合度评价；说明数据来源和预测时间跨度。
3. 路径规划：在模拟网格上模拟单机与多机监测，比较覆盖率、耗时、通信约束。
4. 总体响应：输入传感数据至输出风险图的端到端时延，至少包括平均和最差情况。
5. 失败案例：烟尘遮挡、传感器丢帧、定位偏差和异常输入如何处理；标示当前无法保证的性能。

火灾相关验证必须采用公开火情数据、合规模拟或非燃烧模拟场景，不能自行制造野火或在无授权环境开展飞行。

## PINN 的证据边界

关于物理信息神经网络 (PINN)、中国站金奖与真实多机自主飞行成熟度，现有官方摘要仍不足以确认。我们可以据此了解技术方向，但不能把这些线索写成团队已经完成的成果。

## 已知、推断与资料缺口

| 信息层次 | 本页如何使用 |
|---|---|
| 官方名录事实 | 上方列明的年度奖项归属 |
| 团队申报 | 方案说明、性能及市场数字；未作独立复现 |
| 教学推断与模拟 | 客户研究、程序和实验建议；不归给获奖团队 |
| 尚无证据 | 完整代码、原始数据、全部工况报告、专利授权细节、独立官网及完整实验资料 |


## 延伸阅读

- [案例对照](index.md#comparison)。
- [工程测试](../03-engineering/programming.md#testing)。
- [工程专题](../03-engineering/programming.md#fireaidss)。

资料来源与更新记录见 [来源核查](../07-resources/source-method.md)。
