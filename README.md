# AI_16_Chanuk_CP1_DS
------------
## 소개
> 주제 : 영상 내 주행 트럭 중 과적/정상 차량 구분하기.<br>
> 사용한 모델 라이브러리 : <b><a href="https://github.com/ultralytics/yolov5">yolov5</a></b>


## 설치
<i>이 패키지는 yolov5 모델을 서브모듈로 가지고 있습니다.</i>
```Bash
!git clone --recurse-submodules https://github.com/tjfdnjfch/AI_16_Chanuk_CP1_DS

!pip install -r AI_16_Chanuk_CP1_DS/requirements.txt
```
## 기능

```python
from  AI_16_Chanuk_CP1_DS.src.detect import Truck

# Truck(source)
# class를 생성할 수 있습니다.
# source : 이미지 또는 영상의 경로

mytruck = Truck("sample.mp4")



# Truck(source).detect(project = './', output = '', conf = 0.7)
# 입력된 경로의 파일에서 트럭을 감지한 파일을 생성합니다.
# project : 프로젝트명. 결과물들이 공통적으로 저장될 경로 (yolv5 arguments의 project에 해당.)
# output : 파일명. 파일이 저장될 경로입니다. (yolv5 arguments의 name에 해당.)
# conf : 신뢰도. 0~1의 값을 가집니다. (yolv5 arguments의 conf에 해당.)

mytruck.detect()



# Truck(source).cmd_output(plain = 1)
# yolov5 detect를 커맨드 창에서 실행시켰을 경우의 출력 문구를 반환합니다. (detect를 먼저 실행한 후에 가능합니다.)
# plain : 0 또는 1의 값을 가집니다. plain = 1일 경우 서식이 제거된 텍스트만을 반환합니다.

mytruck.cmd_output()



# Truck(source).show(detected = 0)
# cv2를 이용해 이미지를 보여주거나 영상을 재생합니다.
# detected : 0 또는 1의 값을 가집니다. 0일 경우에는 원본 파일을, 1일 경우에는 detect로 변환된 파일을 보여줍니다.

mytruck.show()



# Truck(source).info(detected = 0)
# 파일의 확장자나 이미지/영상의 해상도를 출력 후 반환합니다.
# detected : 0 또는 1의 값을 가집니다. 0일 경우에는 원본 파일을, 1일 경우에는 detect로 변환된 파일의 정보입니다.

mytruck.info()

```






