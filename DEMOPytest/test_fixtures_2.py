import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def start_automatic_fixture():
    print("Start Test With Automatic Fixture")

@pytest.fixture(scope="module")
def Setup_Teardown():
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    driver.maximize_window()
    driver.find_element(By.XPATH,
                        "//input[@placeholder='E-Mail Address']") \
                            .send_keys("plexmediaserver1523@gmail.com")
    driver.find_element(By.XPATH,
                        "//input[@placeholder='Password']") \
        .send_keys("Admin123")
    driver.find_element(By.XPATH,
                        "//input[@value='Login']").click()
    print("Log In")
    yield
    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "Logout").click()
    print("Log Out")

@pytest.mark.usefixtures("Setup_Teardown")
def test1_order_history_title():
    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "Order").click()
    assert driver.title == "Order History"
    print("Test 1 Is Complete")

@pytest.mark.usefixtures("Setup_Teardown")
def test2_change_password_title():
    driver.find_element(By.PARTIAL_LINK_TEXT,
                        "Password").click()
    assert driver.title == "Change Password"
    print("Test 2 Is Complete")

