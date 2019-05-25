from selenium import webdriver
driver=webdriver.Firefox(executable_path="C:/Users/Dell/Desktop/Drivers/geckodriver-v0.24.0-win64/geckodriver.exe")
driver.get("https://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.quit()