from selenium import webdriver
import time
import pandas as pd

def main():
    
    #ログインIDとパスワードを変数に入れる
    USER = "####"
    Pass = "####"
    
    #chromeのwebdriverを起動
    browser = webdriver.Chrome(executable_path = 'C:\\Users\\###\\OneDrive\\デスクトップ\\MyDriver\\Crome\\chromedriver.exe')
    browser.implicitly_wait(3)


    #ログインするサイトにアクセス
    url_login = "###"
    browser.get(url_login)
    time.sleep(3)


    #ログイン操作1
    elem = browser.find_element_by_id('ap_email')
    elem.clear()
    elem.send_keys(USER)
    browser_from = browser.find_element_by_id('continue')
    time.sleep(3)
    browser_from.click()

    #ログイン操作2
    elem = browser.find_element_by_id('ap_password')
    elem.clear()
    elem.send_keys(Pass)
    browser_from = browser.find_element_by_id('signInSubmit')
    time.sleep(3)
    browser_from.click()


    #会員ページにアクセス
    url = "###"
    time.sleep(1)
    browser.get(url)
    
if __name__ == '__main__':
    main()