import numpy as np

config = {
    'eta': 1,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([0.5046040246268209, 0.15363162694655808, 0.12089146531089001, 0.151544046298763, 0.5133452680909094]),  # 結合効率
    'L': np.array([0.00018269, 0.00018269, 0.00018269, 0.00018269]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'center_wavelength': 1550e-9
}
