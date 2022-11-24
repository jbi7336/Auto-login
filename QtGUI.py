import webdriver as wd

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from MainWindow import Ui_baramWindow
from jsonControl import read_json, input_account, make_json
from selenium.webdriver.chrome.service import Service
from model import listModel
from psutil import process_iter
from subprocess import CREATE_NO_WINDOW

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
        self.loadBtn.pressed.connect(self.load)
        self.deleteBtn.pressed.connect(self.delete)
        self.updateBtn.pressed.connect(self.update)
        self.loginBtn.pressed.connect(self.login)
        self.executeBtn.pressed.connect(self.execute)
        self.allLoginBtn.pressed.connect(self.all_login)
        self.allExecuteBtn.pressed.connect(self.all_execute)

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
        id, pw, job, platform = self.get_info()
        
        # 공백 안됨.
        if id and pw:
            jsonTemp = input_account(id, pw, job, platform)
            self.model.df["account"].append(jsonTemp)
            self.model.layoutChanged.emit()
            self.save()
            self.text_clear()

    def load(self):
        indexes = self.idListView.selectedIndexes()

        if indexes:
            index = indexes[0]
            df = self.model.df["account"][index.row()][1]
            id, pw, job, platform = df["ID"], df["PW"], df["JOB"], df["PLATFORM"]

            self.text_clear()
            self.idText.insert(id)
            self.pwText.insert(pw)
            self.combo_set(self.jobType, job)
            self.combo_set(self.platformType, platform)

    def combo_set(self, comboType, typeName):
        index = comboType.findText(typeName)
        if index != -1:
            comboType.setCurrentIndex(index)

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
        id, pw, job, platform = self.get_info()
        indexes = self.idListView.selectedIndexes()

        if indexes and (id and pw):
            index = indexes[0]
            jsonTemp = input_account(id, pw, job, platform)
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
                self.driver[row] = self.make_driver()
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
                self.driver[row] = self.make_driver()
                self.driver[row].implicitly_wait(3)
                wd.web_login(self.driver[row], data)
                self.status_change(row, True)
        QMessageBox.information(self, "로그인", "로그인이 완료되었습니다.")

    # 선택된 브라우저에 한해서 클라이언트 실행
    def execute(self):
        indexes = self.idListView.selectedIndexes()

        if indexes:
            index = indexes[0]
            row = index.row()

            try:
                wd.game_start(self.driver[row])
            except KeyError as e:
                print("EXECUTE")
                print(e)
                pass 
            except wd.ex.NoSuchWindowException as e:
                print("EXECUTE")
                print(e)
                pass

    # 모든 브라우저에서 클라이언트 실행
    def all_execute(self):
        for i in range(self.model.rowCount(None)):
            try:
                wd.game_start(self.driver[i])
                self.wait_client(i)
            except KeyError as e:
                print("ALLEXECUTE")
                print(e)
            except wd.ex.NoSuchWindowException as e:
                print("ALLEXECUTE")
                print(e)
                pass
        
        QMessageBox.information(self, "실행", "실행이 완료되었습니다.")

    # login(), all_login() 메소드가 실행된 데이터 인지 체크
    def status_change(self, row, status):
        _, info = self.model.df["account"][row]
        self.model.df["account"][row] = (status, info)
        self.model.layoutChanged.emit()        

    def make_driver(self):
        options = wd.uc.ChromeOptions()

        # 바람의나라 홈페이지 외부프로토콜 허용.
        prefs = { "protocol_handler.allowed_origin_protocol_pairs": {
                        "https://baramy.nexon.com": {
                            "ngm": True
                        }
                    }
                }

        options.add_experimental_option("prefs", prefs)
        dr = wd.uc.Chrome(use_subprocess=True, service_creationflags=CREATE_NO_WINDOW, options=options)

        return dr

    # 실행 중인 프로세스를 순회하여 클라이언트 실행 확인.
    def wait_client(self, index):
        index = index + 1
        count = 0

        while(count < index):
            for proc in process_iter():
                try:
                    processName = proc.name()

                    if processName == "baram.exe":
                        count = count + 1
                except (NoSuchProcess, AccessDenied, ZombieProcess):
                    pass

                if index == count:
                    return
            count = 0

    # 계정 데이터 json 형식으로 저장
    def save(self):
        make_json(self.model.df)

    # GUI 가 종료시 이벤트를 받아 모든 계정데이터를 False 처리
    def closeEvent(self, event):
        reqMsg = QMessageBox.question(self, "종료", "종료하시겠습니까?")

        if reqMsg.name == "Yes":
            for i in range(self.model.rowCount(None)):
                _, temp = self.model.df['account'][i]
                self.model.df['account'][i] = (False, temp)

                try:
                    self.driver[i].quit()
                except Exception as e:
                    print("CLOSEEVENT")
                    print(e)
                    pass

            self.save()
            event.accept()
        else:
            event.ignore()
