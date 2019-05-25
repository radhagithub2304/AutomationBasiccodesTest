from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:/Users/Dell/Desktop/Drivers/chromedriver_win32 (2)/chromedriver.exe")
driver.get("https://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.quit()