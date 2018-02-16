# Jaziel Lopez
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def log(of, total,message):

    print("[{}/{}] {}".format(of, total, message))


config = {

    'url': {

        'login': 'http://localhost.thermofisher.com:8080',

        'homepage': 'http://localhost.thermofisher.com:8080/#/'

    },

    'username': 'miguelangel.lopez@thermofisher.com',

    'password': 'Thermo123'
}

driver = webdriver.Remote("http://localhost:4444/wd/hub",
                          webdriver.DesiredCapabilities.CHROME.copy())

driver.get(config['url']['login'])

passed = 0
total = 10


try:

    username = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, 'username')))

    password = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, 'password')))

    submit = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="submit"]')))

    username.send_keys(config['username'])
    password.send_keys(config['password'])

    submit.click()

    passed += 1
    log(passed, total, "User has been logged in successfully")

    # sleep(5)
    #
    # # collapse
    # sidebar = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.ID, 'collapse-button')))
    #
    # sidebar.click()
    #
    # print("Sidebar has been collapsed")
    #
    # devices = WebDriverWait(driver, 2).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.device-item')))
    #
    # current_device = devices[0]
    # current_device.click()
    #
    # chart_tab = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.ID, 'levey-jennings-tab-container')))
    #
    # chart_tab.click()
    #
    # baselineList = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.ID, 'baseline-tab-btn-lv')))
    #
    # baselineList.click()
    #
    # driver.get_screenshot_as_file('baseline-tab-expanded.png')
    #
    # sleep(5)
    #
    # baseline = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '#baseline-tab-btn-lv ul.list-group  li:nth-of-type(2)')))
    #
    # baseline.click()
    #
    # sleep(5)
    #
    # driver.get_screenshot_as_file('baseline-click.png')
    #
    # print(driver.current_url)


except Exception as e:

    print('An error has occurred')
    print(e)


finally:

    print("Status {} {}".format(passed, total))
    print("Finally.. closing web driver")
    driver.close()






