import time

from selenium import webdriver


def test_lambdatest_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/")
    print("Title ", driver.title)
    time.sleep(2)



def test2_lambatest_ecomerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    print("Title: ", driver.title)
    time.sleep(2)

def testRexWebsite():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rexjones2.com")
    print("Title: ", driver.title)
    time.sleep(2)


def gogle_test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.com")
    print("Title: ", driver.title)
    time.sleep(2)
