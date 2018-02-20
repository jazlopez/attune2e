# Jaziel Lopez
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils import __init__, error, log
from exceptions import e2eException

__init__()

def test(name, selector, timeout=3):

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, selector)))

    element.click()

    sleep(timeout)

    driver.get_screenshot_as_file(name + '.png')


config = {

    'url': {

        'login': 'http://localhost.thermofisher.com:8080',

        'homepage': 'http://localhost.thermofisher.com:8080/#/'

    },

    'username': 'miguelangel.lopez@thermofisher.com',

    'password': 'Thermo123'
}

# initialize test counters

passed = 0

total = 10


def get_driver(selenium_url="http://localhost:4444/wd/hub"):

    """
    Get Selenium WebDriver instance

    :param selenium_url

    :return WebDriver
    """

    try:

        driver = webdriver.Remote(selenium_url, webdriver.DesiredCapabilities.CHROME.copy())

        log(passed, total, 'WebDriver instance successfully obtained')

        return driver

    except Exception as e:

        error('Unable to get an instance of WebDriver: {}'.format(e))

        exit()


def login_me(driver):

    """
    Perform automatic login

    :param driver:

    :return:
    """

    try:

        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username')))

        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password')))

        submit = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="submit"]')))

        username.send_keys(config['username'])
        password.send_keys(config['password'])
        submit.click()

        return driver

    except TimeoutException as e:

        driver.close()

        raise e2eException("Unable to set/find either of any: username, password or submit element")


try:

    driver = login_me(get_driver())

except e2eException as e:

    error(str(e))


# login_me(driver)
# try:
#
#     username = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, 'username')))
#
#     password = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, 'password')))
#

#

#
#     sleep(5)
#
#     passed += 1
#     log(passed, total, "User has been successfully logged in")
#
#     # collapse
#     sidebar = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'collapse-button')))
#
#     sidebar.click()
#
#     passed += 1
#     log(passed, total, "Instrument List sidebar has been successfully collapsed")
#
#     devices = WebDriverWait(driver, 2).until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.device-item')))
#
#     current_device = devices[0]
#     current_device.click()
#
#     passed += 1
#     log(passed, total, "Device has been successfully selected")
#
#     chart_tab = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'levey-jennings-tab-container')))
#
#     chart_tab.click()
#
#     sleep(5)
#
#     passed += 1
#     log(passed, total, "User has landed on Levey Jennings module")
#
#     baselineList = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'baseline-tab-btn-lv')))
#
#     baselineList.click()
#
#     sleep(5)
#
#     passed += 1
#     log(passed, total, "Baseline has been successfully loaded")
#
#     driver.get_screenshot_as_file('baseline-tab-expanded.png')
#
#     baseline = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '#baseline-tab-btn-lv ul.list-group li:nth-of-type(2)')))
#
#     baseline.click()
#
#     passed += 1
#
#     sleep(5)
#
#     #click on plotting
#     plottingList = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'plotting-statistics-btn')))
#
#     plottingList.click()
#
#     sleep(5)
#
#     #click on 3rd option
#     plotOption = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '#plotting-statistics-btn ul.list-group  li:nth-of-type(3)')))
#
#     plotOption.click()
#
#     #seep 3 seconds
#     sleep(5)
#
#     #take a picture
#     driver.get_screenshot_as_file('mfi-chart-loaded.png')
#
#     # change color
#     selectedChannel = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '#channels-levey-jennings .channel-btn:nth-child(3)')))
#
#     selectedChannel.click()
#
#     sleep(5)
#
#     driver.get_screenshot_as_file('toggleChartChannel.png')
#
#
#
#     log(passed, total, "User has successfully selected a baseline from menu")
#
#     sleep(5)
#
#     driver.get_screenshot_as_file('baseline-click.png')
#
#     test('ToggleBarChart', 'view-bar-chart', 5)
#
#     test('ToggleMultipleChart', 'view-grid-chart', 5)
#
#     print(driver.current_url)
#
# except BaseException as e:
#
#     error('An error has occurred')
#     error(str(e))
#
# finally:
#
#     print("Status {} {}".format(passed, total))
#     print("Finally.. closing web driver")
#     driver.close()
#