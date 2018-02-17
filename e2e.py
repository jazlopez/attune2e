# Jaziel Lopez
from colorama import init
from colorama import Fore
from colorama import Back
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

init()


def error(message):

    print(Fore.RED + message)


def log(of, out, message):

    print(Fore.BLUE + "[{}/{}] {}".format(of, out, message))


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

driver = webdriver.Remote("http://localhost:4444/wd/hub",
                          webdriver.DesiredCapabilities.CHROME.copy())

driver.get(config['url']['login'])

passed = 0
total = 10


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

    sleep(5)

    passed += 1
    log(passed, total, "User has been successfully logged in")

    # collapse
    sidebar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'collapse-button')))

    sidebar.click()

    passed += 1
    log(passed, total, "Instrument List sidebar has been successfully collapsed")

    devices = WebDriverWait(driver, 2).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.device-item')))

    current_device = devices[0]
    current_device.click()

    passed += 1
    log(passed, total, "Device has been successfully selected")

    chart_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'levey-jennings-tab-container')))

    chart_tab.click()

    sleep(5)

    passed += 1
    log(passed, total, "User has landed on Levey Jennings module")

    baselineList = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'baseline-tab-btn-lv')))

    baselineList.click()

    sleep(5)

    passed += 1
    log(passed, total, "Baseline has been successfully loaded")

    driver.get_screenshot_as_file('baseline-tab-expanded.png')

    baseline = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#baseline-tab-btn-lv ul.list-group li:nth-of-type(2)')))

    baseline.click()

    passed += 1

    sleep(5)

    #click on plotting
    plottingList = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'plotting-statistics-btn')))

    plottingList.click()
    
    sleep(5)

    #click on 3rd option
    plotOption = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#plotting-statistics-btn ul.list-group  li:nth-of-type(3)')))
    
    plotOption.click()

    #seep 3 seconds
    sleep(5)
    
    #take a picture
    driver.get_screenshot_as_file('mfi-chart-loaded.png')

    # change color
    selectedChannel = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#channels-levey-jennings .channel-btn:nth-child(3)')))

    selectedChannel.click()

    sleep(5)

    driver.get_screenshot_as_file('toggleChartChannel.png')



    log(passed, total, "User has successfully selected a baseline from menu")

    sleep(5)

    driver.get_screenshot_as_file('baseline-click.png')

    test('ToggleBarChart', 'view-bar-chart', 5)

    test('ToggleMultipleChart', 'view-grid-chart', 5)

    print(driver.current_url)

except BaseException as e:

    error('An error has occurred')
    error(str(e))

finally:

    print("Status {} {}".format(passed, total))
    print("Finally.. closing web driver")
    driver.close()






