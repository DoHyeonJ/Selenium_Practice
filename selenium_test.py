from selenium import webdriver

path = "/Users/jodohyeon/workspace/selenium_practice/chromedriver"
driver = webdriver.Chrome(path)

driver.get("http://python.org")