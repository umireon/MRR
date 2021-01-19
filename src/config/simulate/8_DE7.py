import numpy as np

config = {
    'eta': 0.996,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([
        0.70841736,
        0.12178538,
        0.15120923,
        0.36295535,
        0.1039419,
        0.17404851,
        0.26015934,
        0.22711359,
        0.79778539
    ]),  # 結合率
    'L': np.array([
        4.6584949e-05,
        4.6584949e-05,
        4.6584949e-05,
        4.6584949e-05,
        4.6584949e-05,
        4.6584949e-05,
        4.6584949e-05,
        4.6584949e-05
    ]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'center_wavelength': 1550e-9,
    # 'lambda': np.arange(1525e-9, 1575e-9, 1e-12)
}
