import re

def test_phones_on_homepage(app):
    user_from_home_page = app.user.get_users_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.home_phone == clear(user_from_edit_page.home_phone)
    assert user_from_home_page.mobile_phone == clear(user_from_edit_page.mobile_phone)
    assert user_from_home_page.work_phone == clear(user_from_edit_page.work_phone)
    assert user_from_home_page.phone2 == clear(user_from_edit_page.phone2)

def clear(s):
    return re.sub("[() -]", "", s)

def test_phones_on_view_page(app):
    user_from_view_page = app.user.get_users_from_view_page(0)
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_view_page.home_phone == user_from_edit_page.home_phone
    assert user_from_view_page.mobile_phone == user_from_edit_page.mobile_phone
    assert user_from_view_page.work_phone == user_from_edit_page.work_phone
    assert user_from_view_page.phone2 == user_from_edit_page.phone2