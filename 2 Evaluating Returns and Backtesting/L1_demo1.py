import numpy as np


annual_returns = np.array([0.1,-0.05, 0.2, 0.08, -0.12])
print(annual_returns)
cumulative_compounded_returns = np.cumprod(1 + annual_returns) - 1
print(cumulative_compounded_returns)
# 计算过程
# 第1年：1.10 - 1 = 0.10
# 第2年：(1.10 × 0.95) - 1 = 1.045 - 1 = 0.045
# 第3年：(1.045 × 1.20) - 1 = 1.254 - 1 = 0.254
# 第4年：(1.254 × 1.08) - 1 = 1.35432 - 1 = 0.35432
# 第5年：(1.35432 × 0.88) - 1 = 1.1918016 - 1 = 0.1918016