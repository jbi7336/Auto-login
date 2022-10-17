from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# 로그인 페이지 : https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fbaramy.nexon.com%2F2022%2Fevent_1005-registration
loginPage = "https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fbaramy.nexon.com%2F2022%2Fevent_1005-registration"

driver = []

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
def nexon_login(id, pw, idx):
    txtID = "txtNexonID"
    txtPW = "txtPWD"

    loginID = driver[idx].find_element_by_id(txtID)
    loginPW = driver[idx].find_element_by_id(txtPW)
    loginBT = driver[idx].find_element_by_class_name("button01")

    loginID.send_keys(id)
    loginPW.send_keys(pw)
    loginBT.send_keys("\ue007")

# 게임시작 버튼 /html/body/div[3]/header/aside/button
def game_start(idx):
    driver[idx].find_element_by_xpath("/html/body/div[3]/header/aside/button").send_keys("\ue007")

def main():
    account = read_ID_PW()

    # 드라이버
    for i in range(account["id"].__len__()):
        driver.append(webdriver.Chrome("../chromedriver.exe"))
        driver[i].implicitly_wait(2)
        driver[i].get(loginPage)

        id = account["id"][i]
        pw = account["pw"][i]
        nexon_login(id, pw, i)

        time.sleep(3)
        game_start(i)

main()
