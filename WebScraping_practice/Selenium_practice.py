print("Importing Modules...")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


print("Connecting...")
ChromeOptions = Options()
ChromeOptions.add_experimental_option("detach", True)  # 화면 꺼짐 방지 옵션 추가
driver = webdriver.Chrome(options=ChromeOptions)
driver.get("https://naver.com")

print("Start Scrapping...")
driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()