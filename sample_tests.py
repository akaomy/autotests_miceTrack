from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# DESCRIBE mice information tracking app MiceTrack


def test_create_new_mouse():
    """DESCRIBE: Create new mouse with most recent date"""

    # it "confirms that new mice row can be added"
    browser = webdriver.Chrome()
    browser.get('http://localhost:5000/')

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

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'msg-status'))
        )
        alert_status = browser.find_element(By.ID, 'msg-status')

        # verify if there is the success message "The info has been added to the table"
        # temp logging out this message to the console to verify that test passed or failed
        if success_message in alert_status.text:
            print('PASS', success_message)
        else:
            print('FAIL', success_message)
    except:
        print('problem with creating a mouse')

    browser.quit()


# run tests
test_create_new_mouse()

# todo: reporting
