import pyper
import pandas as pd

df = pd.read_excel("./data/20211116_CIT.xlsx")   # 相対パスでデータディレクトリ内のエクセルファイルを読み込み
df_preprocessed = df.iloc[:, 10:]   # RTにおいてのデータ抽出
df_preprocessed.to_excel("./data/preprocessed.xlsx")   # グラフ作成用にデータディレクトリにエクセルファイルを出力
r = pyper.R(use_pandas="True")   # Rを利用するためのインスタンスの生成
r.assign("data", df_preprocessed)   # 前処理したデータフレーム型のデータをR上に格納

r("source('./anovakun_486.txt', encoding='utf-8')")   # R上で実行ファイルと同じディレクトリ上のANOVA君の読み込み
# R上で2要因参加者内分散分析を実行し、resultで結果を格納
# 要因A:質問の種類が3水準、要因B:時間経過の有無が2水準、
# auto=Tとすると球面性検定が有意であった被験者内効果に対してGreehnouse-Geisserのイプシロンによる自由度の調整を行う
# eta=Tとすると分散分析表にη二乗を追加する
result = r('anovakun(data,"sAB", 3, 2, auto=T, eta=T)')
print(result)