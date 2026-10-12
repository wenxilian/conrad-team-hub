# OncoMap：用数据预测治疗反应

同一种治疗对不同患者的效果可能不同。OncoMap 尝试结合 RNA 测序数据与机器学习预测癌症免疫治疗反应，为我们提供了一个了解数据分析项目的入口。

这个方向对数据来源、验证划分和专业合作要求较高。下面介绍其公开技术路线，并讨论如何理解预测表现；课堂或团队练习应与真实临床应用分别看待。


<figure class="case-photo">
<a href="https://conrad.spacecenter.org/2026-awards/" target="_blank" rel="noopener"><img src="https://conrad.spacecenter.org/wp-content/uploads/2026/04/OncoMap.avif" alt="OncoMap 在官方获奖介绍中的项目配图" loading="lazy" decoding="async"></a>
<figcaption>OncoMap 的官方介绍配图。<a href="https://conrad.spacecenter.org/2026-awards/">图片与项目介绍来源：2026 年获奖档案</a>。核查于 2026-10-12。</figcaption>
<p class="photo-unavailable" hidden>这张官方图片暂时未能载入，可以<a href="https://conrad.spacecenter.org/2026-awards/">打开项目原始报道</a>查看。</p>
</figure>

## 官方名录核查

2026，The Cartographers，美国华盛顿州，Health & Nutrition Pete Conrad Scholars；RNA模型和KNN为方案申报，非临床认证。来源：[年度官方档案](https://conrad.spacecenter.org/2026-awards/)，核查于 2026-10-12。奖项可核实；性能、市场与财务数字属于官方转述的团队申报或预测。

## 项目背景与技术路线

基于 RNA 测序、生物统计/机器学习、KNN 的个体治疗反应预测概念。技术要点为高维数据、样本外验证、模型泛化和临床评估边界。商业用户可能是医院/临床机构，但竞赛获奖不等于通过医疗器械临床认证。

## 教学拆解：客户、验证与商业路线

读到这里，我们可以进一步考虑如何验证和推广类似方案。下面是供团队练习的建议，尚不是获奖团队已完成实验的记录。

目标客户：研究机构或临床机构；不是可以直接给患者使用的医疗工具。

验证任务：区分训练与样本外数据，检查患者泄漏、RNA 批次差异与类不平衡；KNN 的相似度、特征标准化及验证方案应报告。原始样本和临床评价未公开时不能自行补指标。

商业分析：医疗采用涉及验证与采购要求。教学层面可研究客户流程和成本，不对患者提出治疗建议，也不以竞赛奖项代替认证。

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

资料来源与更新记录见 [来源核查](../07-resources/source-method.md)。
