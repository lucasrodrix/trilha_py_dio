import os, shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# os.mkdir(ROOT_PATH/'03_os_shutil')
arquivo = open(ROOT_PATH/'osshutil.txt','w')
arquivo.close()

# os.rename(ROOT_PATH/'osshutil.txt', ROOT_PATH/'OsShutil.txt')
# os.remove(ROOT_PATH/'osshutil.txt')
shutil.move(ROOT_PATH/'osshutil.txt',ROOT_PATH/'03_os_shutil'/'osshutil.txt')