# README

## 利用方法

* spmod.yaml がanacondaの仮想環境の設定ファイルとなっているので, 適宜以下のコマンドなどで環境構築する.  
* cvxpyの導入でpythonのバージョンが下がるため, 仮想環境の利用を推奨.  

```conda create -n [env_name] --file spmod.yaml```


## ファイル構成


### 多項式補間, 最小二乗法, リッジ回帰

以降に述べるディレクトリには3つのファイルが存在する.  
ファイル名と手法の対応はそれぞれ以下の通りである.

* Polynominal_interpolation : 補間多項式
* Least_square_method : 最小二乗法
* Ridge_regression : リッジ回帰

#### y2t
    
* y = 2 * t 関係のファイル
    * ガウス雑音なし/あり でわけてある
        * ガウス雑音なし : Original
        * ガウス雑音あり : With_Gaussian_noise

#### Sin_wave

* y = sin(t) 関係のファイル
    * ガウス雑音あり版のみ (書籍準拠)


### スパースモデリング

以下は多項式補間, L2正則化(書籍に明記されてないけどリッジ回帰と同義), スパースモデリングを用いた

* Polynominal_interpolation : 多項式補間
* L2_norm : L2正則化
* Sparse_modeling : スパースモデリング

#### 80th_polynominal

* y = -t^80 + t に対して実行
    * スパースモデリングはあまりにもきれいにground_truth(実際の値)と重なるので, 適宜コメントアウトしたり工夫して確かめるとよい


# 注意点

動作の正確さは保証しません