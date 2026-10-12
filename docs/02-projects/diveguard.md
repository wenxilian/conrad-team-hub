# DiveGuard：潜水时怎样传递一条短消息

潜水员在水下想向同伴或水面传递信息时，常规无线电通信会受到限制。DiveGuard 围绕这个问题提出低成本声学短消息系统，适合用来讨论通信性能与具体使用场景之间的关系。

这一页先看技术与测试，再讨论潜水机构和使用者的购买需求。市场估计和财务练习放在同一个案例里，帮助我们理解：一个设备能工作，距离形成可持续的产品还需要回答哪些问题。


<figure class="case-photo">
<a href="https://conrad.spacecenter.org/2026-awards/" target="_blank" rel="noopener"><img src="https://conrad.spacecenter.org/wp-content/uploads/2026/04/DiveGuard_China-Cyber.avif" alt="DiveGuard 在官方获奖介绍中的项目配图" loading="lazy" decoding="async"></a>
<figcaption>DiveGuard 的官方介绍配图。<a href="https://conrad.spacecenter.org/2026-awards/">图片与项目介绍来源：2026 年获奖档案</a>。核查于 2026-10-12。</figcaption>
<p class="photo-unavailable" hidden>这张官方图片暂时未能载入，可以<a href="https://conrad.spacecenter.org/2026-awards/">打开项目原始报道</a>查看。</p>
</figure>

## 官方名录核查

2026，中国，Cybertechnology & Security Power Pitch；市场124亿/2.16亿/648万美元为团队申报。来源：[年度官方档案](https://conrad.spacecenter.org/2026-awards/)，核查于 2026-10-12。奖项可核实；性能、市场与财务数字属于官方转述的团队申报或预测。

## 项目背景与技术路线

水下声学短消息通信设备，官方名录确认其为 2026 Cybertechnology & Security Power Pitch。它所面对的问题是：水下常规无线电传播受限，潜水员与水面沟通困难。技术为低成本水下声学通信，重点测试通信距离、误码率、延迟、深度、噪声、续航和可靠性。市场面向潜水学校、休闲和专业潜水客户，可能采用硬件销售及相关服务。此前讨论引述团队市场估计 TAM 124 亿美元、SAM 2.16 亿美元、SOM 648 万美元；必须在网站标注为项目资料所述，且 TAM 旅游产业与 SAM 设备市场统计口径不同，不能未经说明当成严格嵌套关系。教学模拟：20 家机构 × 每家 15 台 × 每台 150 美元 = 45,000 美元设备收入，非实际业绩。

## 商业验证与完整教学算例

**项目事实层**：中国团队提出水下声学通信短消息系统，讨论资料提到将潜水用户及潜水机构作为客户，赛事摘要中出现 TAM 124 亿美元、SAM 2.16 亿美元、SOM 648 万美元。三个市场数并非严格相同市场口径的嵌套集合，必须解释产业总额与设备市场差异。

**教育示范：自下而上市场规模**：假设可接触 20 家潜水培训机构，每家平均购入 15 台，每台 150 美元，则设备收入：


$$
R=20\times15\times150=45{,}000\ \mathrm{USD}
$$


这不是已成交订单。必须问「这 20 家机构从何而来？谁有权采购？有多大的预算？为什么选择我们的设备？」。

**教育示范：硬件盈亏平衡**：设单价 $P=150$ 美元、单位可变成本 $VC_{u}=90$ 美元、固定成本 $F=12{,}000$ 美元，则


$$
\Pi=(P-VC_{u})Q-F=60Q-12{,}000
$$


$$
Q^{*}=\frac{F}{P-VC_{u}}=200
$$


当 $Q=300$ 时，收入 45,000 美元，总成本 $12,000+300\times90=39,000$ 美元，利润 6,000 美元。销售 200 台才恰好达到此简化模型的盈亏平衡点。不考虑税费、折旧、售后等额外费用。可制作 0–600 台销量滑块。

**渠道验证**：联系潜水学校与潜水教练，进行受监管、可控的原型测试，重点通信距离、误码率、潜水安全需求、培训机构实际采购路径；性能与可靠性达标前不得把模拟测试说成真实水下安全保障。

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
- [商业专题](../04-business/diveguard-case.md)。

资料来源与更新记录见 [来源核查](../07-resources/source-method.md)。

## 图解与教学模拟

<div class="flow-grid">
<div class="flow-card"><strong>TAM：124 亿美元</strong><p>全球潜水旅游行业总额。</p></div>
<div class="flow-card"><strong>SAM：2.16 亿美元</strong><p>智能潜水设备市场估计。</p></div>
<div class="flow-card"><strong>SOM：648 万美元</strong><p>初期东南亚目标市场估计。</p></div>
</div>

这些为团队申报，旅游总额与设备市场口径不同，故不画成严格嵌套集合或按面积暗示比例。真正可获得市场需要客户、区域、年份和收入单位一致。[完整说明](../04-business/diveguard-case.md#market-sizing)。

<div class="calculator" data-model="hardware"></div>
