# Auto-login
```
바람의나라:연 로그인 및 게임실행 관리를 위해 만든 Python 프로그램
```

## Requirements
```
async-generator==1.10
attrs==22.1.0
cffi==1.15.1
charset-normalizer==2.1.1
click==7.1.2
exceptiongroup==1.0.0
h11==0.14.0
idna==3.4
outcome==1.2.0
pycparser==2.21
PyQt6==6.0.2
pyqt6-plugins==6.0.2.2.2
PyQt6-Qt==6.0.1
PyQt6-Qt6==6.4.0
PyQt6-sip==13.4.0
pyqt6-tools==6.0.2.3.2
PySocks==1.7.1
python-dotenv==0.21.0
qt6-applications==6.0.2.2.2
qt6-tools==6.0.2.1.2
requests==2.28.1
selenium==4.5.0
sniffio==1.3.0
sortedcontainers==2.4.0
trio==0.22.0
trio-websocket==0.9.2
undetected-chromedriver==3.1.6
urllib3==1.26.12
websockets==10.4
wincertstore==0.2
wsproto==1.2.0
```

## 사용방법
```
1. 코드가 존재하는 상위 폴더에 크롬드라이버를 함께 두어야 합니다.
2. 필요 라이브러리 설치후 main.py를 실행하면 GUI가 구현됩니다.
```

![image](https://user-images.githubusercontent.com/35110792/199516897-3bb33530-a83f-4254-a35d-c01b10bf1c6f.png)

```
기존에 ./resource/id.json 에 계정 정보가 저장되어 있다면 정보를 읽어
ListView 에 ( status / job / platform / id ) 형식으로 보이게 계정정보가 보이게 됩니다.
```

### Add
```
ID, PW 을 적고, 직업과 계정 플랫폼을 선택한 뒤 Add 버튼을 누르시면 계정정보가 저장됩니다.
ID나 PW를 빈칸으로 둘 시 Add 가 진행되지 않습니다.
```

### Delete
![image](https://user-images.githubusercontent.com/35110792/199517746-34776a66-6c52-4c07-8e07-91f9f7a175aa.png)
```
계정목록을 마우스로 클릭한 뒤 Delete 버튼을 누르면 계정정보가 삭제됩니다.
```

### Update
![image](https://user-images.githubusercontent.com/35110792/199518708-284caa4a-7edf-4583-b36f-c2732a3e4d99.png)
```
선택한 데이터를 입력한 데이터로 교체합니다.
```

### Login, Execute
```
단일, 기능의 경우 선택한 데이터에 한해 (로그인, 게임실행) 실행합니다.
All 기능의 경우 리스트에 있는 모든 데이터가 동작합니다.
```

## 주의사항
```
1. 로그인 동작이 완료되지 않았는데, 실행버튼을 누르면 동작을 하지 않습니다.
2. 자동화된 브라우저를 사용하기 때문에 기존 브라우저에 저장된 캐시데이터 및 계정정보를 사용하지 않습니다. 계정 OTP나 2차 인증이 요구됩니다.
3. 크롬브라우저를 사용합니다. 크롬브라우저가 없을시 제대로 동작하지않습니다.
4. 크롬드라이버와 크롬의 버전을 맞춰 주셔야합니다.
    - https://chromedriver.chromium.org/downloads
5. 홈페이지 정보를 파싱해서 사용하는 것이기 때문에 홈페이지 정보가 변경될 시 제대로 동작하지 않을 수 있습니다.
```