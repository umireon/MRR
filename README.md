# MRR

## Need to install

[Python 3](https://www.python.org/downloads/)
Git

## OS

recommend for using Linux / macOS

## Download this repository

git clone https://github.com/nimiusrd/MRR.git

## 仮想環境 / virtual env
ref: https://docs.python.org/3/library/venv.html

### 作成 / make

```bash
python3 -m venv .
```

### 有効化 / activate

```bash
. bin/activate
```

## install

```bash
pip3 install -r requirements.txt
```
## 実行 / execute

### 最適化 / optimize

configuration file: `src/config/base.py`

```bash
cd src
python main.py
```

### シミュレーション / simulate

`-c`オプションは`src/config/simulate`にあるpythonファイルを指定する．

```bash
cd src
python main.py -c two_same_2
```

## Jupyter

### 起動

```bash
jupyter notebook
```
基本的に`notebook/`でファイルを作成する．

## テスト

```bash
cd src
python -m unittest discover -s __tests__
```
