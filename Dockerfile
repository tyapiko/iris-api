# 1. ベースとなるイメージを指定
# OS + Pythonがインストール済みの軽量なイメージを選択
FROM python:3.12-slim

# 2. コンテナ内での作業ディレクトリを設定
WORKDIR /app

# 3. 依存関係ファイルを先にコンテナにコピー
# このようにファイルを分けてコピーすると、Dockerのキャッシュが効きやすくなり、ビルドが高速化する
COPY requirements.txt .

# 4. requirements.txtを元に依存関係をインストール
# --no-cache-dir は、キャッシュを保存せず、イメージサイズを小さく保つためのおまじない
RUN pip install --no-cache-dir -r requirements.txt

# 5. アプリケーションのソースコード（カレントディレクトリの全ファイル）をコンテナにコピー
COPY . .

# 6. コンテナが起動した時に実行されるコマンドを指定
# uvicornを起動し、外部からのアクセスを許可する
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
