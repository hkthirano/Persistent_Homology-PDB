# 使い方

1. HomCloud(Persistent Homology解析ソフトウェア)をインストールしてください。  
HomCloudのインストールは[こちら](http://www.wpi-aimr.tohoku.ac.jp/hiraoka_labo/homcloud/)から。

2. Protein Data Bankから解析したいPDBファイル(hogehoge.pdb)を、"PDB Format"の形式でダウンロードしてください。  
ダウンロードしたPDBファイルは、Persistent_PDB/PDBfile/の中に入れてください。  
PDBファイルのダウンロードは[こちら](https://www.rcsb.org/)から。  
サンプルファイルとして、"1xq5.pdb"が最初から入っています。
3. 実行は以下の通りです。
````bash
sh exe.sh hogehoge.pdb
# sh exe.sh 1xq5.pdb (サンプルファイルの実行例)
````
実行後は、Persistent_PDB/tmp/hogehoge_datas/の中に以下のファイルが入ります。  
 * hogehoge_atom.txt：hogehoge.pdb から抜き出したα炭素の座標。  
 * hogehoge.idiagram：プロットするためのデータ。  
 * hogehoge-pd2.txt：プロットする際の、birth(横軸)-death(縦軸)のペア。

5. 結果  
[パーシステントホモロジーでタンパク質の穴を見てみる](https://qiita.com/hokuto_HIRANO/items/98cf702d04d80ec2d66f)
