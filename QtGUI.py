import webdriver as wd

from PyQt6 import uic, QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from MainWindow import Ui_baramWindow
from jsonControl import read_json, input_account, make_json
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

class listModel(QtCore.QAbstractListModel):
    def __init__(self, df=None):
        super().__init__()
        self.df = df or {}

        # 읽은 데이터 상태 표시 이미지
        self.tick = QtGui.QImage('./image/tick.png')
        self.redcross = QtGui.QImage('./image/redcross.png')

    # ListView 에 보여질 데이터 선별
    # Override
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # Json
            _, json = self.df['account'][index.row()]
            platform = json['PLATFORM']
            id = json['ID']
            pw = json['PW']
            job = json['JOB']

            strTemp = f'{job}\t{platform}\t{id}\t'
            return strTemp

        if role == Qt.ItemDataRole.DecorationRole:
            status, _ = self.df['account'][index.row()]
            if status:
                return self.tick
            else:
                return self.redcross

    # Override
    def rowCount(self, index):
        return self.df['account'].__len__()

# 메인 프레임
class Window(QMainWindow, Ui_baramWindow):
    def __init__(self):
        super().__init__()
        Ui_baramWindow().__init__()
        self.driver = {}

        # UI 설정
        self.setupUi(self)

        # ListView 모델 등록
        self.model = listModel()
        self.model.df = read_json()
        self.idListView.setModel(self.model)

        # 버튼과 이벤트 연결
        self.addBtn.pressed.connect(self.add)
        self.deleteBtn.pressed.connect(self.delete)
        self.updateBtn.pressed.connect(self.update)
        self.loginBtn.pressed.connect(self.login)
        self.executeBtn.pressed.connect(self.exCute)
        self.allLoginBtn.pressed.connect(self.all_login)
        self.allExecuteBtn.pressed.connect(self.all_exCute)

    # 입력된 데이터 형식 읽어서 저장
    def get_info(self):
        idTemp = self.idText.text()
        pwTemp = self.pwText.text()
        jobTemp = self.jobType.currentText()
        pfTemp = self.platformType.currentText()

        return idTemp, pwTemp, jobTemp, pfTemp

    # ID, PW 입력창 청소
    def text_clear(self):
        self.idText.clear()
        self.pwText.clear()

    # 입력한 데이터 등록
    def add(self):
        infoTemp = self.get_info()
        
        # 공백 안됨.
        if infoTemp[0] and infoTemp[1]:
            jsonTemp = input_account(infoTemp[0], infoTemp[1], infoTemp[2], infoTemp[3])
            self.model.df["account"].append(jsonTemp)
            self.model.layoutChanged.emit()
            self.save()
            self.text_clear()

    # 선택된 데이터를 삭제
    def delete(self):
        indexes = self.idListView.selectedIndexes()

        if indexes:
            index = indexes[0]
            del self.model.df["account"][index.row()]
            self.model.layoutChanged.emit()
            self.save()

    # 선택된 데이터를 새로이 입력된 데이터로 교체
    def update(self):
        infoTemp = self.get_info()
        indexes = self.idListView.selectedIndexes()

        if indexes and (infoTemp[0] and infoTemp[1]):
            index = indexes[0]
            jsonTemp = input_account(infoTemp[0], infoTemp[1], infoTemp[2], infoTemp[3])
            self.model.df["account"][index.row()] = jsonTemp
            self.model.layoutChanged.emit()
            self.save()
            self.text_clear()

    # 선택한 계정만 로그인
    def login(self):
        indexes = self.idListView.selectedIndexes()

        if indexes:
            index = indexes[0]
            row = index.row()
            _, data = self.model.df["account"][row]

            try:
                wd.web_login(self.driver[row], data)
            except:
                service = Service()
                self.driver[row] = wd.uc.Chrome(use_subprocess=True, service_creationflags=CREATE_NO_WINDOW)
                self.driver[row].implicitly_wait(3)
                wd.web_login(self.driver[row], data)
            self.status_change(row, True)

    # 등록된 모든 계정 로그인
    def all_login(self):
        for row in range(self.model.rowCount(None)):
            _, data = self.model.df["account"][row]

            try:
                wd.web_login(self.driver[row], data)
            except:
                self.driver[row] = wd.uc.Chrome(use_subprocess=True, service_creationflags=CREATE_NO_WINDOW)
                self.driver[row].implicitly_wait(3)
                wd.web_login(self.driver[row], data)
            self.status_change(row, True)

    # 선택된 브라우저에 한해서 클라이언트 실행
    def exCute(self):
        indexes = self.idListView.selectedIndexes()

        if indexes:
            index = indexes[0]
            row = index.row()

            try:
                wd.game_start(self.driver[row])
            except KeyError:
                pass 
            except wd.ex.NoSuchWindowException:
                pass

    # 모든 브라우저에서 클라이언트 실행
    def all_exCute(self):
        for i in range(self.model.rowCount(None)):
            try:
                wd.game_start(self.driver[i])
            except KeyError:
                pass
            except wd.ex.NoSuchWindowException:
                pass

    # login(), all_login() 메소드가 실행된 데이터 인지 체크
    def status_change(self, row, status):
        _, info = self.model.df["account"][row]
        self.model.df["account"][row] = (status, info)
        self.model.layoutChanged.emit()        

    # 계정 데이터 json 형식으로 저장
    def save(self):
        make_json(self.model.df)

    # GUI 가 종료시 이벤트를 받아 모든 계정데이터를 False 처리
    def closeEvent(self, event):
        for i in range(self.model.rowCount(None)):
            _, temp = self.model.df['account'][i]
            self.model.df['account'][i] = (False, temp)

        self.save()
        event.accept()