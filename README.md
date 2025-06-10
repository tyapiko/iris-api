# Iris Classifier API (アヤメ品種分類API)

## 1. 概要 (Overview)

このプロジェクトは、アヤメ(Iris)の計測データ（がく片の長さ・幅、花びらの長さ・幅）から、その品種（Setosa, Versicolour, Virginica）を予測する機械学習モデルを搭載したWeb APIです。
アプリケーションはDockerコンテナとしてパッケージ化されており、どこでも簡単に実行できます。

## 2. 技術スタック (Tech Stack)

* **言語:** Python 3
* **機械学習:** scikit-learn, joblib, pandas
* **APIフレームワーク:** FastAPI
* **サーバー:** uvicorn
* **コンテナ化:** Docker
* **バージョン管理:** Git, GitHub

## 3. 使い方 (Usage)

1.  このリポジトリをクローンまたはダウンロードします。
2.  お使いの環境にDockerがインストールされていることを確認します。
3.  リポジトリのルートディレクトリで、以下のコマンドを実行してDockerイメージをビルドします。
    ```bash
    docker build -t iris-api .
    ```
4.  以下のコマンドでコンテナを起動します。
    ```bash
    docker run -p 8000:80 iris-api
    ```
5.  Webブラウザで `http://localhost:8000/docs` にアクセスすると、APIの対話的なドキュメントを閲覧・テストできます。

## 4. APIエンドポイント

### POST `/predict`

アヤメの計測データをJSON形式で送信すると、予測される品種名を返します。

**リクエストボディ:**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

## レスポンス
{
  "prediction": "setosa"
}
