from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_successfull():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(1000)

    userName= "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    password ="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"


    driver.find_element_by_xpath(userName).send_keys("Admin")

    driver.find_element_by_xpath(password).send_keys("admin123")

    driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

    expected = 'OrangeHRM'
    actual_value= driver.title

    assert expected ==actual_value