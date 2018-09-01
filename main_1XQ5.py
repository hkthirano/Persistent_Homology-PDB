from Read_XYZ.main import Read_xyz as r_xyz
import subprocess

config = ['A', 'NA', 'NA']

demo = r_xyz('./PDBfile/1OVA.pdb', config)

demo.matching_lines()
demo.extract_xyz()
demo.save_extract_xyz('./Data/1OVA_xyz.txt')


# pythonコマンドはフルパスを指定した方がいいかも
# ex. /bin/python .pyenv/hoge/hoge/python
shell_1 = ['python', '-m', 'homcloud.pc2diphacomplex', '-I', '-D', '-d',
           '3', '--no-square', './Data/1OVA_xyz.txt', './Data/1OVA_pointcloud.idiagram']
subprocess.call(shell_1)


shell_2 = ['python', '-m', 'homcloud.plot_diagram', '-X', '64',
           '-d', '2', '-l', './Data/1OVA_pointcloud.idiagram', '-o', './Data/1OVA_PD.png']
subprocess.call(shell_2)


shell_3 = ['rm', 'Data/1OVA_pointcloud.idiagram']
subprocess.call(shell_3)
