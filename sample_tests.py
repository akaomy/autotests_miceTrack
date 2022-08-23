from ast import Assert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create new mouse with recent date
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

# verify if there is the success message "The info has been added to the table"
try:
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'msg-status'))
    )
    alert_status = browser.find_element(By.ID, 'msg-status')
    print('alert_status.text', alert_status.text)
    assert 'The info has been added to the table' in alert_status.text
except:
    print('problem with locating alert message')


# TODO: verify if newly created row is present in the table

# browser.quit()
