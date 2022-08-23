from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# DESCRIBE mice information tracking app MiceTrack

# variables
url = 'http://localhost:5000/'
create_mouse_id = 'test-id-1'
mouse_id = 'female-mouse-manual-id'
mating_date_id = 'mating-date'
create_btn_id = 'create-btn'
msg_status_id = 'msg-status'


def test_create_new_mouse(female_mouse_id, mating_date):
    """DESCRIBE: Create new mouse with most recent date"""

    # Confirm that new mice row can be added"

    browser = webdriver.Chrome()
    browser.get(url)

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, create_mouse_id))
        )
        create_btn = browser.find_element(By.ID, create_mouse_id)
        create_btn.click()
    except:
        print('problem with locating create button')

    female_id_input = browser.find_element(By.ID, mouse_id)
    female_id_input.click()
    female_id_input.send_keys(female_mouse_id)

    mating_date_input = browser.find_element(By.ID, mating_date_id)
    mating_date_input.send_keys(mating_date)

    create_btn = browser.find_element(By.ID, create_btn_id)
    create_btn.click()

    success_message = 'The info has been added to the table'

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, msg_status_id))
        )
        alert_status = browser.find_element(By.ID, msg_status_id)

        # verify if there is the success message "The info has been added to the table"
        # logging out the message to verify if test is passed or failed
        if success_message in alert_status.text:
            print('PASS', success_message)
        else:
            print('FAIL', success_message)
    except:
        print('problem with creating a mouse')

    browser.quit()


# run tests
test_create_new_mouse('AutoMouseID', '08-22-2022')

# todo: reporting
