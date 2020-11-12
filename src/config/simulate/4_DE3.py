import numpy as np

config = {
    'eta': 1,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([0.6801970187866004, 0.11628269020813592, 0.03828242340296922, 0.02904591528771383, 0.19303860210040208]),  # 結合率
    'L': np.array([2.28357593e-04, 5.70893983e-05, 5.70893983e-05, 5.70893983e-05]),  # リング周長
    'n_eq': 3.3938,  # 等価屈折率
    'n_g': 4.2,  # 実効屈折率
    'center_wavelength': 1550e-9,
    # 'lambda': np.arange(1535e-9, 1565e-9, 1e-12)
}
