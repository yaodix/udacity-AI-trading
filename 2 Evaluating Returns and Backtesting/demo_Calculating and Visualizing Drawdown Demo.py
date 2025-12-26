import pandas as pd

# 模拟股价数据
dates = pd.date_range('2023-01-01', periods=6, freq='D')
prices = pd.Series([100, 105, 98, 110, 108, 115], index=dates)

# 计算累积最大值（历史最高点）
historical_high = prices.cummax()

# 计算当前价格相对历史高点的回撤
drawdown = (prices - historical_high) / historical_high * 100  # 回撤百分比

result_df = pd.DataFrame({
    'Price': prices,
    'Historical High': historical_high,
    'Drawdown %': drawdown.round(2)
})

print(result_df)

# 输出：
#             Price  Historical High  Drawdown %
# 2023-01-01    100              100        0.00
# 2023-01-02    105              105        0.00  # 创新高
# 2023-01-03     98              105       -6.67  # 从高点回撤6.67%
# 2023-01-04    110              110        0.00  # 创新高
# 2023-01-05    108              110       -1.82  # 从高点回撤1.82%
# 2023-01-06    115              115        0.00  # 创新高