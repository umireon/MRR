import numpy as np

config = {
    'eta': 1,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([0.9054194877516863, 0.5512608258891112, 0.3736631926448726, 0.37347734200336213, 0.5173400704611504, 0.740035249179362, 0.7391581972362704, 0.5579638563435033, 0.6097662424459871, 0.8759220113789248, 0.8873150303041232, 0.5721970875829617, 0.35889040406094436, 0.3169271959378231, 0.34529354349988933, 0.49422163698243965, 0.8543364482520788]),  # 結合効率
    'L': np.array([0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269, 0.00018269]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'center_wavelength': 1550e-9
}
