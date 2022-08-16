# conda指令:
'''
使用powershell需初始化conda
conda init powershell
生成.condarc文件
conda config --set show_channel_urls yes
显示镜像源
conda config --show-sources
设置镜像源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2/
删除镜像源恢复默认
conda config --remove-key channels
帮助
conda -h
查询某个指令帮助
conda <command> -h
版本
conda -V
当前环境安装包列表
conda list
环境列表
conda env list
创建虚拟环境
conda create -n <env name> python=3.9
激活虚拟环境
conda activate <env name>
退出虚拟环境
conda deactivate
当前环境创建requirements.txt
conda list -e > requirements.txt
当前环境安装requirements.txt
conda install --yes --file requirements.txt
当前环境安装包
conda install <package name>
指定环境删除所有的包即删除环境
conda remove -n <env name> --all
指定环境删除指定包
conda remove -n <env name> <package name>
当前环境删除指定的包
conda remove <package name>/conda clean <package name>/conda uninstall <package name>
更新conda和其他所有包
conda upgrade conda
更新指定包
conda update <package name>

删除没用的包
conda clean -p
删除tar包
conda clean -t
删除所有包及cache
conda clean -y --all
'''
# pip指令：
'''
设置清华镜像源为pip默认
(其他：https://pypi.douban.com/simple/)
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
升级pip
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
包列表
pip list
显示包信息
pip show <package name>
安装包
pip install <package name>
卸载包
pip uninstall <package name>
创建requirements.txt（可能会丢失依赖包的版本号）
pip freeze > requirements.txt
安装requirements.txt
pip install -r requirements.txt
'''
# python3-pip-autoremove指令：
'''
卸载包及依赖(conda remove不好用时再用这个)
pip3-autoremove <package name>
'''
# pyinstaller指令：
'''
pyinstaller -F -w xxx.py -i 'logo.ico'
'''