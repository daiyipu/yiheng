# 风控模型监控指标汇总

## 一、模型表现监控
> 1. **Ranking & Accuracy** ：排序性和准确性，用来量化评分卡的强度，主要通过Lift，Odds，KS(Kolmogorov-Smirnov)，AUC，Gini等指标进行反映
> 2. **Population Stability Index**：群体稳定性指标，用来衡量分数分布的变化
> 3. **Characteristic Stability Index**：特征稳定性指标，用来衡量特征层面的变化
> 4. **Vintage Analysis**：账龄分析，在账龄的基础上分析投资组合变现
> 5. **Portfolio Analysis**：组合分析，关注组合风险，主要包含逾期分布(Delinquency Distribution)和转移矩阵或滚动率分析(Transition Matrix or Roll Rate Analysis)
> 6. **MIV On Characteristic**:特征的边际信息值，用来监控特征预测能力的变化，可以和CSI结合起来看
> 7. **Concept Drift Detection**：客群偏移检测，用来监控客群变化
> 8. **Score Misalignment**：分数错配，用来监控评分卡分数的偏移程度，从而确定是否需要重新Refit评分卡模型

## 二、模型影响分析
> 1. **Selection Process: Reject waterfall**：选择过程：拒绝瀑布流，即在申贷放款过程中每个环节（反欺诈拒绝、政策拒绝、人为拒绝、风控拒绝等）拒绝流量变化，反映了整体流程的稳定性
> 2. **Concordance Analysis**：一致性分析，分析模型决策与策略决策（不使用模型分的策略规则）的一致性，即模型决策过程中认为的坏样本，策略决策过程中是否也认为是坏样本
> 3. **Override Analysis**：撤销分析，分析风控整体决策后最终决定（放款、拒绝）的变化，即对被模型通过但是被信审拒绝人群的拒绝原因进行分析


