# -*- coding: utf-8 -*-
"""초음파이미지 따로 분리.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CZfPfMBICjc0ysn36esQS5hmIx0YGirS
"""



from google.colab import drive
drive.mount('/content/drive')

import os
file_path = 'C:\project\section4 project\초음파\천안초음파'
file_names = os.listdir(file_path)
file_names

# 천안 농가별 초음파 사진 따로 분리
import shutil
import os
from os.path import join
RootDir1 = r'C:\project\section4 project\초음파\천안초음파'
TargetFolder = r'C:\project\section4 project\초음파\chunan'
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        for name in files:
            if name.endswith('.jpg'):
                print ("Found")
                SourceFolder = os.path.join(root,name)
                shutil.copy2(SourceFolder, TargetFolder)

os.chdir('C:\project\section4 project\초음파\초음파\20110708\이석구\000192805636')
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = r'C:\project\section4 project\초음파\초음파\20110708\이석구\000192805636' + str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)

print(os.listdir("C:/project/section4 project/초음파/초음파/20111110/심현두/"))

# 폴더안 사진(jpg) 이름변경(폴더이름으로)
root = "C:/project/section4 project/초음파/초음파/20111110/심현두/002507264171"

for path, subdirs, files in os.walk(root):
    for name in files:
        extension = name.split(".")[-1].lower()
        if extension != "jpg":
            continue
        os.rename(os.path.join(path, name), os.path.join(path, os.path.basename(path) + "." + extension))
        
        print(os.path.basename(path))

# 안성 농가별 초음파 사진 따로 분리
import shutil
import os
from os.path import join
RootDir1 = r'C:\project\section4 project\초음파\초음파'
TargetFolder = r'C:\project\section4 project\초음파\anseong'
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        for name in files:
            if name.endswith('.jpg'):
                print ("Found")
                SourceFolder = os.path.join(root,name)
                shutil.copy2(SourceFolder, TargetFolder)

!pip install --upgrade xlrd

from tqdm import tqdm
from keras.layers import BatchNormalization
import pandas as pd
image_directory = "/content/drive/MyDrive/AI/section4/project/anseong"
df = pd.read_excel('/content/drive/MyDrive/AI/section4/project/안성농가종합초음파판독결과.xls', index_col=None, header=None)