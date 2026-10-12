# Aphelion：用球形电机改进卫星姿态控制

卫星需要不断调整姿态，让天线、仪器或太阳能电池板朝向合适的方向。传统多轴结构可能增加体积、重量与连接复杂度，Aphelion 尝试用球形电机和控制算法改进这一过程。

这个案例能把机械结构、控制程序和功耗测量连接起来。下面既保留团队公开介绍的指标，也讨论怎样建立对照实验，让学生能够解释一个改进究竟来自哪里。


<figure class="case-photo">
<a href="https://conrad.spacecenter.org/2026-awards/" target="_blank" rel="noopener"><img src="https://conrad.spacecenter.org/wp-content/uploads/2026/04/Aphelion.avif" alt="Aphelion 在官方获奖介绍中的项目配图" loading="lazy" decoding="async"></a>
<figcaption>Aphelion 的官方介绍配图。<a href="https://conrad.spacecenter.org/2026-awards/">图片与项目介绍来源：2026 年获奖档案</a>。核查于 2026-10-12。</figcaption>
<p class="photo-unavailable" hidden>这张官方图片暂时未能载入，可以<a href="https://conrad.spacecenter.org/2026-awards/">打开项目原始报道</a>查看。</p>
</figure>

## 官方名录核查

2026，美国加州，Aerospace & Aviation Pete Conrad Scholars；质量-20%/体积-61.8%/功率-71%为初步原型申报，基准细节未公布。来源：[年度官方档案](https://conrad.spacecenter.org/2026-awards/)，核查于 2026-10-12。奖项可核实；性能、市场与财务数字属于官方转述的团队申报或预测。

## 项目背景与技术路线

卫星多轴控制相关的球形电机执行机构，官方名录确认其为美国团队并获 2026 Aerospace & Aviation Pete Conrad Scholars。技术目标是用较紧凑的机电结构替代多执行器系统，提高质量、体积、功耗指标。讨论引述团队初步原型比较：质量减 20%、体积减 61.8%、功耗减 71%，须查清比较基准和测量条件，并标为团队公布数据。

技术拆解：CAD / 3D 打印、机械自由度、转矩和传动，电机驱动、编码器与控制回路，PID 基本思想。PID：


$$
u(t)=K_{p}e(t)+K_{i}\int_{0}^{t} e(\tau)d\tau+K_{d}\frac{de(t)}{dt}
$$

<div class="relationship-figure"><div class="diagram-row"><div class="diagram-node">目标角度 r(t)</div><span class="diagram-arrow">→</span><div class="diagram-node">误差 e(t) 与 PID<br><small>比例、积分、微分</small></div><span class="diagram-arrow">→</span><div class="diagram-node">驱动与执行器<br><small>安全限幅、停止保护</small></div></div><div class="feedback-label">↑ 编码器测得 y(t) → 回到控制器，更新 e(t)=r(t)−y(t)</div><div class="diagram-support">同任务测试：定位误差 · 响应时间 · 超调 · 重复性 · 负载 · 总能量</div><p class="figure-caption">教学闭环控制示意，不是获奖团队的原始结构图。参数调试不能替代设备保护。</p></div>


学生可用 Arduino、ESP32 等成熟控制器建立传感反馈、闭环驱动、日志与 Python 图形。测试定位平均/最大误差、阶跃响应、稳定时间、重复性、功率与完成同一任务的总能量；不能仅靠某时刻功率声称节能。

## 工程原理、程序模块与实验建议

### 工程路径

从目标需求出发确定自由度、负载、速度与精度；设计 CAD 结构；制造低成本原型；安装驱动电路与角度反馈装置；搭建闭环控制；重复测试定位、响应与能耗。

在一维轴上可用比例、积分、微分反馈的组合，误差 $e(t)=r(t)-y(t)$，控制量：


$$
u(t)=K_{p}e(t)+K_{i}\int_{0}^{t} e(\tau)d\tau+K_{d}\frac{de(t)}{dt}
$$


解释目标角度、实际角度、误差、超调、稳定时间，不只把公式贴出来。若涉及多轴，增加旋转矩阵、基本运动学与限位逻辑。

### 控制系统程序模块

- 传感器：读取编码器角度、校准、检查越界和断连。
- 控制器：计算误差，输出适当控制信号；设限幅、安全退出。
- 记录器：写出时间、设定角度、实际角度、电流、电压和状态码。
- 计算程序：用 Python 绘制期望与实际轨迹、误差曲线、响应时间。

### 推荐测试矩阵

| 指标 | 方法 | 报告 |
|---|---|---|
| 定位 | 多个目标角度重复指令 | 平均、最大绝对误差 |
| 动态响应 | 阶跃命令 | 上升时间、稳定时间、超调 |
| 重复性 | 同一目标执行 10–20 次 | 标准差、失败次数 |
| 载荷 | 安全范围内增加负载 | 误差变化、稳定极限 |
| 能耗 | 同任务、同负载下积分 $VI$ | Wh，不只瞬时 W |
| 结构 | 实测质量与几何尺寸 | 与基准装置比较 |

公式 $E=\int_{0}^{T} V(t)I(t)\,dt$，明确测量时间与采样频率。历史讨论出现的 20%、61.8%、71% 是团队公布比较结果，项目报告本身应披露基准和重复测试，不能从摘要推出全部工况有效。

## 能量单位核对

若电压以 V、电流以 A、时间以秒计，积分结果为 J；换成 Wh 需要除以 3,600。同任务能量比较应包含完成时长，不能只比较某瞬间功率。

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
- [工程专题](../03-engineering/programming.md#aphelion)。

资料来源与更新记录见 [来源核查](../07-resources/source-method.md)。

## 公式符号与能量单位
目标角度为 $r(t)$，测得角度为 $y(t)$，误差 $e(t)=r(t)-y(t)$，控制输出为 $u(t)$。$K_{p}$、$K_{i}$ 和 $K_{d}$ 分别是比例、积分、微分增益。增益需在安全限幅下调试，模型不能代替设备保护。
电压 $V(t)$ 以 V、电流 $I(t)$ 以 A、时间以秒计时，$\int_{0}^{T}V(t)I(t)\,dt$ 的单位是 J；换成 Wh 需除以 3,600。这里的 $T$ 是同一任务的测量时长。
