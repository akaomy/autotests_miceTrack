from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# DESCRIBE: Create new mouse with recent date
def test_create_new_mouse():
    browser = webdriver.Chrome()
    browser.get('http://localhost:5000/')

    # add explicit wait to fix issue
    # no such element: Unable to locate element: {"method":"css selector","selector":"[id="test-id-1"]
    # wait untill button got rendered to click on it
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'test-id-1'))
        )
        create_btn = browser.find_element(By.ID, 'test-id-1')
        create_btn.click()
    except:
        print('problem with locating create button')

    female_id_input = browser.find_element(By.ID, 'female-mouse-manual-id')
    female_id_input.click()
    female_id_input.send_keys('AutoTest1')

    mating_date_input = browser.find_element(By.ID, 'mating-date')
    mating_date_input.send_keys('08-22-2022')

    create_btn = browser.find_element(By.ID, 'create-btn')
    create_btn.click()

    success_message = 'The info has been added to the table'

    # verify if there is the success message "The info has been added to the table"
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'msg-status'))
        )
        alert_status = browser.find_element(By.ID, 'msg-status')
        # temp logging out this message to the console to verify that test passed
        if success_message in alert_status.text:
            print('PASS', success_message)
        else:
            print('FAIL', success_message)
    except:
        print('problem with creating a mouse')

    browser.quit()


test_create_new_mouse()
