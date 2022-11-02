import undetected_chromedriver as uc
import selenium.common.exceptions as ex

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

loginPage = "https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fbaramy.nexon.com%2F"
mainPage = "https://baramy.nexon.com/"

# 드라이버와 계정 정보를 받아 플랫폼 선별하여 로그인
def web_login(driver, data):
    id = data["ID"]
    pw = data["PW"]
    platform = data["PLATFORM"]
    driver.get(loginPage)

    # 이미 로그인을 한 상태에서 다시 누를 시 예외처리
    try:
        bt = driver.find_element(By.CLASS_NAME, "bt" + platform)
        bt.click()
    except ex.NoSuchElementException as e:
        driver.get(mainPage)
        return

    if platform == "Nexon":
        nexon_login(driver, id, pw)
    elif platform == "Google":
        google_login(driver, id, pw)
    elif platform == "Naver":
        naver_login(driver, id, pw)
    elif platform == "Facebook":
        facebook_login(driver, id, pw)
    else:
        # Wrong platform (Do not support)
        return

# 페이스북 로그인
def facebook_login(driver, id, pw):
    txtID = "email"
    txtPW = "pass"

    try:
        loginID = driver.find_element(By.ID, facebookID)
        loginPW = driver.find_element(By.ID, txtPW)

        loginID.send_keys(id)
        loginPW.send_keys(pw)
        loginPW.send_keys("\ue007")
    except:
        return

# 네이버 로그인
def naver_login(driver, id, pw):
    txtID = "id"
    txtPW = "pw"

    try:
        loginID = driver.find_element(By.ID, txtID)
        loginPW = driver.find_element(By.ID, txtPW)

        loginID.send_keys(id)
        loginPW.send_keys(pw)
        loginPW.send_keys("\ue007")
    except:
        return



# 구글 로그인
def google_login(driver, id, pw):
    txtID = '//*[@id="identifierId"]'
    txtPW = '//*[@id="password"]/div[1]/div/div[1]/input'

    try:
        loginID = driver.find_element(By.XPATH, txtID)
        loginID.send_keys(id)
        loginID.send_keys("\ue007")

        # Load delay
        driver.implicitly_wait(2)

        loginPW = driver.find_element(By.XPATH, txtPW)
        loginPW.send_keys(pw)
        loginPW.send_keys("\ue007")
    except:
        return

# 넥슨 로그인
def nexon_login(driver, id, pw):
    txtID = "txtNexonID"
    txtPW = "txtPWD"

    try:
        loginID = driver.find_element(By.ID, txtID)
        loginPW = driver.find_element(By.ID, txtPW)

        loginID.send_keys(id)
        loginPW.send_keys(pw)
        loginPW.send_keys("\ue007")
    except:
        return

def game_start(driver):
    # 드라이버의 현재 페이지 확인 후 실행
    # 페이지가 맞지 않는다면 이동.
    if driver.current_url == mainPage:
        pass
    else:
        driver.get(mainPage)

    try:
        btn = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/header/div/aside/div/button'))
        )
        btn.click()
    except ex.UnexpectedAlertPresentException:
        # 너무나 빠른 입력으로 인한 AlertBox 생성시
        pass
    except:
        # 예상되지 않은 오류
        # 1. 로그인을 하지 않은 상태에서 Excute 사용시 무반응
        return