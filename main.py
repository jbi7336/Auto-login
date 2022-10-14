from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# 로그인 페이지 : https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fbaramy.nexon.com%2F2022%2Fevent_1005-registration
loginPage = "https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fbaramy.nexon.com%2F2022%2Fevent_1005-registration"

driver = driver.Chrome("../chromedriver.exe")
driver.implicitly_wait(3)
driver.get(loginPage)

# 계정 파싱
def read_ID_PW():
    account = { "id" : [], "pw" : [] , "google" : 0}
    f = open("../id.txt", "r")

    # 분류
    while True:
        line = f.readline()

        if not line:
            break
        
        str_temp = line.strip().split(':')
        if str_temp[0] != "google":
            key, value = str_temp
            account[key].append(value)
        else: # Google
            account["google"] = account["google"] + 1
    
    return account

# 구글 로그인
# //*[@id="contents"]/div/div[2]/button[2]
def google_login():
    driver.find_element_by_xpath('//*[@id="contents"]/div/div[2]/button[2]').send_keys("\ue007")

# 넥슨 로그인
def nexon_login(id, pw):
    txtID = "txtNexonID"
    txtPW = "txtPWD"

    loginID = driver.find_element_by_id(txtID)
    loginPW = driver.find_element_by_id(txtPW)
    loginBT = driver.find_element_by_class_name("button01")

    loginID.send_keys(id)
    loginPW.send_keys(pw)
    loginBT.send_keys("\ue007")

# 게임시작 버튼 /html/body/div[3]/header/aside/button
def game_start():
    driver.find_element_by_xpath("/html/body/div[3]/header/aside/button").send_keys("\ue007")

# 다음 로그인 대기
def logout():
    pass

def wait_next():
    pass

def main():
    account = read_ID_PW()

    for i in range(account.__len__()):
        id = account["id"][i]
        pw = account["pw"][i]
        nexon_login(id, pw)

        time.sleep(5)
        game_start()

main()
