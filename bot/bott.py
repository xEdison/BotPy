from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

sleep(2)
driver.get('https://www.instagram.com/accounts/login/')
sleep(5)

username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys('edison_77x')
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys('Edison77x')
button_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
button_login.click()
sleep(5)


hashtag_list = ['jer0o0o0', 'ben10', 'colombia']


for hashtag in hashtag_list:
    driver.get('https://www.instagram.com/' + hashtag + '/')
    sleep(3)


    firs_thumbnail = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
    firs_thumbnail.click()
    sleep(3)

    # first_thumbnail = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[1]/div[1]/a/div[1]')
    # first_thumbnail.click()
    # sleep(3)

    for n in range(1):
        try:
            button_like = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div')
            button_like.click()
            sleep(2)
        except:
            pass

driver.quit()
