import os
from os.path import join
import pandas as pd
import sys
# bus = sys.argv[0]
# print(bus)
lables_path = 'Gray_Label'
lable_pngs = []
val_png = []
for (root, dirs, files) in os.walk(lables_path):
    for file in files:
        if '.png' in file:
            for png in files:
                lable_pngs.append(join(root,png))
                val_png.append(png.replace('_bin.png',''))
            break

# print(len(lable_pngs))
paths = ['Road02','Road03','Road04']
img_jpgs = []
val_jpg = []
for pathi in paths:
    for (root, dirs, files) in os.walk(pathi):
        for file in files:
            if '.jpg' in file:
                for png in files:
                    img_jpgs.append(join(root,png))
                    val_jpg.append(png.replace('.jpg', ''))
                break
# print(len(img_jpgs))

assert set(val_png)==set(val_jpg)
table = pd.DataFrame([img_jpgs,lable_pngs]).T
table.columns=['img','lbl']
table.to_csv('data_lables_paths.csv',index=False, encoding='GBK')
