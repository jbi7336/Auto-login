from selenium import webdriver

# 로그인 페이지 : https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fbaramy.nexon.com%2F2022%2Fevent_1005-registration

loginPage = "https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fbaramy.nexon.com%2F2022%2Fevent_1005-registration"

driver = webdriver.Chrome("../chromedriver.exe")
driver.implicitly_wait(2)
driver.get(loginPage)


# 넥슨 로그인
def nexon_login():
    txtID = "txtNexonID"
    txtPW = "txtPWD"

    loginID = driver.find_element_by_id(txtID)
    loginPW = driver.find_element_by_id(txtPW)


if __name__ == '__main__':
    pass

