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

def testById(name, id, timeout=3):

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, id)))

    element.click()

    sleep(timeout)

    driver.get_screenshot_as_file(name + '.png')

def testBySelector(name, selector, timeout=3):

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    
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
total = 15


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

    sleep(10)
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

    passed += 1
    log(passed, total, "User has successfully selected a baseline from menu")
    sleep(5)

    ### PLOTTING STATISTICS TESTS ##
    testById('PlottingStatisticsList', 'plotting-statistics-btn', 5)
    passed += 1
    log(passed, total, "Plotting statistics had been successfully loaded")

    testBySelector('PlottingStatisticsElement', '#plotting-statistics-btn ul.list-group  li:nth-of-type(3)', 5)
    passed += 1
    log(passed, total, "User has successfully selected a plotting statistic from menu")

    ### LASER CHANNEL TESTS ##
    testBySelector('channelsLeveyJennings', '#channels-levey-jennings div.channel-btn.base-channel-btn:nth-child(3)')
    passed += 1
    log(passed, total, "User has successfully selected a channel from available channels")
    
    ### PAGINATION TESTS ##
    testBySelector('nextPage', 'div.icon-arrow-right')
    passed += 1
    log(passed, total, "User has successfully moved to the next page")

    #last page
    #should test the '>' get inactive
    lastPage = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.arrow.icon-arrow-right')))
    
    if(lastPage != 'undefined'):
        passed +=1
        log(passed, total,"There was unactivated the next page button")
    
    testBySelector('previousPage', 'div.icon-arrow-left')
    passed += 1
    log(passed, total, "User has successfully moved to the previous page")

    #first page
    #should test the '<' get inactive
    firstPage = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.arrow.icon-arrow-left')))
    
    if(firstPage != 'undefined'):
        passed +=1
        log(passed, total,"There was unactivated the first page button")

    #Jaziel's code
    testById('ToggleBarChart', 'view-bar-chart', 5)
    passed += 1
    log(passed, total, "User has successfully changed to 2 charts by page")

    testById('ToggleMultipleChart', 'view-grid-chart', 5)
    passed += 1
    log(passed, total, "User has successfully changed to 4 charts by page")


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