from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


with open('vars.json') as f:
    data = json.load(f)

    vars = []
    for each in data:
        vars.append(data[each])

url = vars[0]
createMouseId = vars[1]
mouseID = vars[2]
matingDateId = vars[3]
createBtnId = vars[4]
msgStatusID = vars[5]
successMsg = vars[6]


browser = webdriver.Chrome()
browser.get(url)


def locate_create_mouse_button():
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, createMouseId))
        )
        create_btn = browser.find_element(By.ID, createMouseId)
        create_btn.click()
    except:
        print('problem with locating create button')


def click_create_mouse_btn():
    create_btn = browser.find_element(By.ID, createBtnId)
    create_btn.click()


def enter_female_id(female_mouse_id):
    female_id_input = browser.find_element(By.ID, mouseID)
    female_id_input.click()
    female_id_input.send_keys(female_mouse_id)


def enter_mating_date(mating_date):
    mating_date_input = browser.find_element(By.ID, matingDateId)
    mating_date_input.send_keys(mating_date)


def verify_success_msg_present():
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, msgStatusID))
        )
        alert_status = browser.find_element(By.ID, msgStatusID)

        # verify if there is the success message "The info has been added to the table"
        # logging out the message to verify if test is passed or failed
        if successMsg in alert_status.text:
            print('PASS', successMsg)
        else:
            print('FAIL', successMsg)
    except:
        print('problem with creating a mouse')


def tearDown():
    browser.close()
    browser.quit()
