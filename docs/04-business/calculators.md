# 三个财务模拟器：改变假设，检查结论

看商业预测时，我想知道：如果售价、销量或成本变了，原来的结论还能成立吗？这些计算器可以帮助我和其他同学把几个关键假设放在一起比较。

可以先用默认数值理解公式，再换成自己查到的数据。这里的结果用于学习和讨论，不代表真实订单或经营记录。

## BeeGuard 订阅模型

<div class="calculator" data-model="saas"></div>

年度收入为 $12NP$，边际贡献为 $12N(P-v)$；边际贡献还需扣固定成本才能得到简化利润。

## DiveGuard 销量与盈亏平衡

<div class="calculator" data-model="hardware"></div>

利润为 $(P-v)Q-F$；仅在 $P>v$ 时有正销量盈亏平衡点 $F/(P-v)$。销量为整数时向上取整，恰好整除时该点利润为零。

## 家庭购置与净节约

<div class="calculator" data-model="household"></div>

回收期为 $P/S$，寿命期简单净节约为 $TS-P$。图中比较累计节约 $tS$ 与初始支出 $P$，属于差额示意，没有绘制真实两方案总成本。等于寿命时仅刚好收回初始投入。

## 延伸阅读

- [计算的原始假设](household-hardware.md#model-limits)。
- [NPV 与成本](household-hardware.md#savings)。

资料来源与更新记录见 [来源核查](../07-resources/source-method.md)。
