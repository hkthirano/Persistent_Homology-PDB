# Persistent_Homology-PDB

パーシステントホモロジーでタンパク質の穴を見る.

![res](https://github.com/hokuto-HIRANO/Persistent_Homology-PDB/blob/master/Data/sample_1OVA_PD.png)

## 使い方

内部で`HomCloud`を使用.

HomCloudのインストールは[ここ](http://www.wpi-aimr.tohoku.ac.jp/hiraoka_labo/homcloud/)から.

## デモ

例として, `PDBfile`に`1OVA.pdb`(タンパク質データ)を準備.

以下のように実行すると, `Data`の中に３つの結果ファイルが作成される.

```
python main_1XQ5.py
```

+ 1OVA_xyz.txt : PDBファイルから取り出した、アミノ酸主鎖座標(x, y, z)
+ 1OVA_PD.png : 1OVA_xyz.txtから計算したパーシステントダイアグラム

## 詳細

座標を抽出するプログラムは, 別途で自作した`Read_Amin_XYZ`というライブラリを使用.

使い方は, [hokuto-HIRANO/Read_Amin_XYZ](https://github.com/hokuto-HIRANO/Read_Amin_XYZ).

他のタンパク質で試す場合は, PDBファイルを[PDB](https://www.rcsb.org/)からダウンロードして、  
`main_1XQ5.py`を参考に.

結果の図だけ見たい場合はWebアプリから.

[Protein Holes](http://takemoto08.bio.kyutech.ac.jp/~hirano/Protein_Holes/)


## 備考  

+ [パーシステントホモロジーでタンパク質の穴を見てみる](https://qiita.com/hokuto_HIRANO/items/98cf702d04d80ec2d66f)
+ [Persistent Homologyについて 「パーシステントホモロジーと機械学習」](http://ibisml.org/archive/ibis2016/Hiraoka_IBIS2016.pdf)
