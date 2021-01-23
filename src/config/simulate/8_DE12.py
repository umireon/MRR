import numpy as np

config = {
    'eta': 0.996,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([
        0.2382073291675155, 0.11657129596812835, 0.36458282211103205, 0.13988428488125942, 0.26234876636398874, 0.20276210564122357, 0.19391425932053435, 0.31643235167231454, 0.5645561725534555
    ]),  # 結合率
    'L': np.array([
        2.877305675054511e-05,
        2.877305675054511e-05,
        2.877305675054511e-05,
        2.877305675054511e-05,
        2.877305675054511e-05,
        2.877305675054511e-05,
        2.877305675054511e-05,
        2.877305675054511e-05
    ]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'center_wavelength': 1550e-9,
    # 'lambda': np.arange(1525e-9, 1555e-9, 1e-12)
}
