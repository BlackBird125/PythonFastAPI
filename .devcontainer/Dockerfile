# ベースイメージとしてPython 3.9を使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /workspace

# 依存関係をインストール
COPY ./app/requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r /workspace/requirements.txt

# アプリケーションのソースコードをコピー
COPY ./app /workspace/app

# ポート8000を開放
EXPOSE 8000

# アプリケーションを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
