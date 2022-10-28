from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# 로그인 페이지 : https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fbaramy.nexon.com%2F2022%2Fevent_1005-registration
loginPage = "https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fbaramy.nexon.com%2F2022%2Fevent_1005-registration"
driverPath = "../chromedriver.exe"

driver = []

# 계정 파싱
def read_ID_PW():
    account = {}

    try:
        with open("../id.json", "r") as f:
            account = json.load(f)
    except:
        print("No file")

    return account

# 페이스북 로그인
def facebook_login(id, pw, idx):
    pass

# 애플 로그인
def apple_login(id, pw, idx):
    pass

# 네이버 로그인
def naver_login(id, pw, idx):
    pass

# 구글 로그인
def google_login(id, pw, idx):
    txtID = '//*[@id="identifierId"]'
    txtPW = '//*[@id="password"]/div[1]/div/div[1]/input'
    idBT = '//*[@id="identifierNext"]/div/button'
    pwBT = '//*[@id="passwordNext"]/div/button'

    loginID = driver[idx].find_element(By.XPATH, txtID)
    loginID.send_keys(id)
    driver[idx].find_element(By.XPATH, idBT).click()


    loginPW = driver[idx].find_element(By.XPATH, txtPW)
    loginPW.send_keys(pw)
    driver[idx].find_element(By.XPATH, pwBT).click()

# 넥슨 로그인
def nexon_login(id, pw, idx):
    txtID = "txtNexonID"
    txtPW = "txtPWD"

    loginID = driver[idx].find_element(By.ID, txtID)
    loginPW = driver[idx].find_element(By.ID, txtPW)
    loginBT = driver[idx].find_element(By.CLASS_NAME, "button01")

    loginID.send_keys(id)
    loginPW.send_keys(pw)
    loginBT.click()

# 게임시작 버튼 /html/body/div[3]/header/aside/button
def game_start(idx):
    driver[idx].find_element(By.XPATH, "/html/body/div[3]/header/aside/button").send_keys("\ue007")

def main():
    account = read_ID_PW()

    # 드라이버
    for i in range(account['account'].__len__()):
        driver.append(webdriver.Chrome(driverPath))
        driver[i].implicitly_wait(2)
        driver[i].get(loginPage)

        id = account["id"][i]
        pw = account["pw"][i]
        nexon_login(id, pw, i)

        time.sleep(3)
        game_start(i)

if __name__ == "__main__":
    main()