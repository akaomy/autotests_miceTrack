
import actions
# DESCRIBE mice information tracking app MiceTrack


# class CRUD_table:

#     # css selectors
#     URL = 'http://localhost:5000/'
#     create_mouse_id = 'test-id-1'
#     mouse_id = 'female-mouse-manual-id'
#     mating_date_id = 'mating-date'
#     create_btn_id = 'create-btn'
#     msg_status_id = 'msg-status'

#     def __init__(self, driver):
#         self.driver = driver


def test_create_new_mouse(female_mouse_id, mating_date):
    """DESCRIBE: Create new mouse with most recent date"""

    # Confirm that new mice row can be added"

    actions.locate_create_mouse_button()

    actions.enter_female_id(female_mouse_id)

    actions.enter_mating_date(mating_date)

    actions.click_create_mouse_btn()

    actions.verify_success_msg_present()

    actions.cleanUp()


# run tests
test_create_new_mouse('AutoMouseID', '08-22-2022')

# todo: reporting
