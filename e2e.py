from config import E2E
from colorama import init
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

screenshot = os.path.abspath(os.getcwd().join(['screenshots']))

config = E2E().config

init()

def error(message):

    print(Fore.RED + message)


def log(of, out, message):

    print(Fore.BLUE + "[{}/{}] {}".format(of, out, message))


def testById(name, id, timeout=3):

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, id)))

    element.click()

    sleep(timeout)

    driver.get_screenshot_as_file(screenshot + '/' + name + '.png')


def testBySelector(name, selector, timeout=3):

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    element.click()

    sleep(timeout)

    driver.get_screenshot_as_file(screenshot + '/' + name + '.png')


driver = webdriver.Remote(config['url']['webdriver'],
                          webdriver.DesiredCapabilities.CHROME.copy())

passed = 0

total = 17

driver.get(config['url']['login'])

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

driver.get(config['url']['homepage'])

sleep(10)
# collapse
sidebar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'collapse-button')))

sidebar.click()

passed += 1
log(passed, total, "Instrument List sidebar has been successfully collapsed")

devices = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.device-item')))

current_device = devices[0]
current_device.click()

sleep(8)

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
log(passed, total, "Baselines had been successfully loaded")

driver.get_screenshot_as_file('baseline-tab-expanded.png')

baseline = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#baseline-tab-btn-lv ul.list-group li:nth-of-type(2)')))

baseline.click()

passed += 1
log(passed, total, "User has successfully selected a baseline from menu")

# resize
driver.set_window_size(1450, 855)

testById('ButtonDeviation', 'svg_FSC_button_deviation', 5)
passed +=1
log(passed, total, "Toggle Deviation")

testById('ButtonAverage', 'svg_FSC_button_average', 5)
passed +=1
log(passed, total, "Toggle Average")

### PLOTTING STATISTICS TESTS ##
testById('PlottingStatisticsList', 'plotting-statistics-btn', 5)
passed += 1
log(passed, total, "Plotting statistics had been successfully loaded")

sleep(5)
testBySelector('PlottingStatisticsElement', '#plotting-statistics-btn ul.list-group  li:nth-of-type(3)', 5)
passed += 1
log(passed, total, "User has successfully selected a plotting statistic from menu")

sleep(5)
### LASER CHANNEL TESTS ##
testBySelector('channelsLeveyJennings', '#channels-levey-jennings div:nth-child(3)')
passed += 1
log(passed, total, "User has successfully selected a channel from available channels")

sleep(5)
### PAGINATION TESTS ##
testBySelector('nextPage', 'div.icon-arrow-right')
passed += 1
log(passed, total, "User has successfully moved to the next page")

sleep(5)
testBySelector('nextPage', 'div.icon-arrow-right')

#last page
#should test the '>' get inactive
lastPage = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.arrow.icon-arrow-right')))

passed += 1
log(passed, total,"There was unactivated the next page button")

sleep(5)
testBySelector('previousPage', 'div.icon-arrow-left')
passed += 1
log(passed, total, "User has successfully moved to the previous page")

testBySelector('previousPage', 'div.icon-arrow-left')
#first page
#should test the '<' get inactive
firstPage = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.arrow.icon-arrow-left')))

passed += 1
log(passed, total, "There was unactivated the first page button")
sleep(5)

#Jaziel's code
testById('ToggleBarChart', 'view-bar-chart', 5)
passed += 1
log(passed, total, "User has successfully changed to 2 charts by page")
sleep(5)

testById('ToggleMultipleChart', 'view-grid-chart', 5)
passed += 1
log(passed, total, "User has successfully changed to 4 charts by page")

print(driver.current_url)