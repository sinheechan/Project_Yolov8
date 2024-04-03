import zipfile
import os

# 가상환경 설정
'''
conda create -n car_seg python=3.12
conda activate car_seg
'''

# 압축 해제할 파일 경로
zip_file_path = "C:/Github_VisualStudio/roboflow.zip"

# 압축을 해제할 폴더 경로
extract_to_folder = "C:/Github_VisualStudio/roboflow"

# 압축 해제
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_folder)


# 경로와 이미지 붙여쓰기 : glob
from glob import glob

train_img = glob('C:/Github_VisualStudio/roboflow/train/images/*.jpg')
train_txt = glob('C:/Github_VisualStudio/roboflow/train/labels/*.txt')
val_img = glob('C:/Github_VisualStudio/roboflow/valid/images/*.jpg')
val_txt = glob('C:/Github_VisualStudio/roboflow/valid/labels/*.txt')

print(len(train_img), len(train_txt))
print(len(val_img), len(val_txt))


# 직접 txt 파일 생성 후 경로 지정 후 쓰기

with open('C:/Github_VisualStudio/ultralytics/train_val_txt/train.txt', 'w') as f:
  f.write('\n'.join(train_img) + '\n')

with open('C:/Github_VisualStudio/ultralytics/train_val_txt/val.txt', 'w') as f:
  f.write('\n'.join(val_img) + '\n')


# 이미지 예측
yolo segment predict model=C:/Github_VisualStudio/ultralytics/my_seg_car_240227.pt source=C:/Github_VisualStudio/roboflow/test/images

# 영상 예측
yolo segment predict model=C:/Github_VisualStudio/ultralytics/my_seg_car_240227.pt source= https://youtu.be/qbaWkt8V6HQ