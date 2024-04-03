# 경로 설정
'''
conda create -n rps
conda activate rps
'''

# pip install
'''
pip install ultralytics
yolo predict
'''

# Raw 데이터 zip 파일을 가져오기
curl -L "https://public.roboflow.com/ds/orVECZFnvV?key=sDLGP3XRMk" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip

# yolo classify predict
yolo classify predict show model=C:/Users/gmlck/HeechansVS/my_seg_rps_240229.pt source=C:/Users/gmlck/HeechansVS/rps_vidio_720x1280_2.mp4

# 해당 영상은 스마트폰으로 가위바위보 테스트 영상을 720x1080 영상 사이즈로 학습한 결과, 대부분의 손 동작을 Rock(주먹)으로 인식
# 모듈 생성 과정에서 Raw 데이터는 모두 300x300 정사이즈로 학습을 진행
# 이에 따라 해당 영상을 1080x1080 정사이즈로 변환 후 다시 학습을 진행

yolo classify predict show model=C:/Users/gmlck/HeechansVS/my_seg_rps_240229.pt source=C:/Users/gmlck/HeechansVS/rps_vidio_1080x1080_2.mp4

# 해당 학습 결과, Scissors(가위)에 대한 정확도는 여전히 낮으나 Paper(보자기)를 인식하는 정확도가 향상