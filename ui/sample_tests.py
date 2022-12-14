
import actions

# DESCRIBE mice information tracking for MiceTrack app


def test_create_new_mouse(female_mouse_id, mating_date):
    """DESCRIBE: Create new mouse with most recent date"""

    # Confirm that new mice row can be added"

    actions.locate_create_mouse_button()

    actions.enter_female_id(female_mouse_id)

    actions.enter_mating_date(mating_date)

    actions.click_create_mouse_btn()

    actions.verify_success_msg_present()

    actions.tearDown()

# TODO: delete, update


# run tests
test_create_new_mouse('AutoMouseID', '08-22-2022')

# todo: reporting
