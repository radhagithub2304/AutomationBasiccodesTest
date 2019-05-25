from selenium import webdriver
driver=webdriver.Ie(executable_path="C:/Users/Dell/Desktop/Drivers/IEDriverServer_Win32_3.14.0/IEDriverServer.exe")
driver.get("https://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.quit()