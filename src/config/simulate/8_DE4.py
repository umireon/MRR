import numpy as np

config = {
    'eta': 0.996,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([
        0.4931288291940284,
        0.23773460534516977,
        0.23245345904922893,
        0.21456478266924955,
        0.5190212950044067,
        0.4178576917907628,
        0.2289143041704449,
        0.2417461845883982,
        0.6447915996572446
    ]),  # 結合率
    'L': np.array([
        0.00014158170782014258,
        0.00014158170782014258,
        0.00014158170782014258,
        0.00014158170782014258,
        0.00033979609876834226,
        0.00014158170782014258,
        0.00014158170782014258,
        0.00014158170782014258
    ]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'center_wavelength': 1550e-9,
    # 'lambda': np.arange(1525e-9, 1575e-9, 1e-12)
}
