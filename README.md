# PangBoo

專案開發枋模

## 建立 Python virtual environment

```bash
python -m venv venv
```

## 載入 Python virtual environment

Ta̍k-kái攏ài開，才來開發。

```bash
source venv/bin/activate
```

## 安裝tox

tox是tī本機走test用--ê。

```bash
pip install tox
```

## 更新套件版本

`requirements.in`是記專案有直接用ê第三方套件。`requirements.txt`是管kui專案全部第三方套件koh對應版本，保證開發、CI試驗、上線版本一致。

1. 請先 `pip install pip-tools` tàu [pip-tools](https://github.com/jazzband/pip-tools) 自動管理套件版本。
2. 手動更新`requirements.in`。
3. 揀一款指令自動更新套件版本。

      ```bash
      # 有必要--ê才更新
      pip-compile
      # 盡量更新
      pip-compile --upgrade
      ```

4. 檢查`requirements.txt`更新狀態。
