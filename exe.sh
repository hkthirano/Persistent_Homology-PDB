tmp=$1
filename=${tmp%.pdb}

mkdir tmp
mkdir tmp/${filename}_datas

#PDBファイルからATOMのCαを抜き出す
python3 read_atom_from_PDB.py PDBfile/$filename.pdb > tmp/${filename}_datas/${filename}_atom.txt

#atom.txtからPersistent Homologyを計算する
python3 -m homcloud.pc2diphacomplex -I -D -d 3  tmp/${filename}_datas/${filename}_atom.txt $filename.idiagram

mv $filename.idiagram tmp/${filename}_datas/

#2次（空洞）のパーシステント図をプロットする
python3 -m homcloud.plot_diagram -d 2 -l tmp/${filename}_datas/$filename.idiagram

#テキストファイルに書き出す
python3 -m homcloud.diagram_to_text -d 2 tmp/${filename}_datas/$filename.idiagram -o tmp/${filename}_datas/$filename-pd2.txt
