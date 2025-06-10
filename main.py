# 1. 必要なライブラリをインポート
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

# 2. FastAPIインスタンスの作成
app = FastAPI()

# 3. 入力データ用のモデルを定義 (Pydanticを使用)
# これにより、リクエストの型チェックとAPIドキュメントの自動生成が行われます。
class IrisItem(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 4. 学習済みモデルの読み込み
# このmain.pyが実行される場所からの相対パスでモデルファイルを指定します。
model = joblib.load('iris_model.pkl')

# 品種名を定義 (モデルの出力 0, 1, 2 に対応する名前)
iris_species = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

# 5. トップページ（ルート）のエンドポイント (動作確認用)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier API"}

# 6. 予測を行うエンドポイントを作成
# POSTリクエストを http://<host>:<port>/predict で受け付けます。
@app.post("/predict")
def predict(item: IrisItem):
    # 受け取ったデータをモデルが予測できる形式(2次元配列)に変換
    input_data = np.array([[
        item.sepal_length,
        item.sepal_width,
        item.petal_length,
        item.petal_width
    ]])

    # モデルで予測を実行
    prediction_index = model.predict(input_data)[0]
    
    # 予測されたインデックスに対応する品種名を取得
    species_name = iris_species[prediction_index]

    # 予測結果をJSON形式でクライアントに返す
    return {"prediction": species_name}
