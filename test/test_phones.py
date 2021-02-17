from model.users import Users
import allure


def test_phones_on_view_page(app):
    with allure.step('Open home page'):
        app.open_home_page()
    with allure.step('Given a user list. Empty - add user'):
        user1 = Users(users_name="специальный юзер", home_phone="2345678", mobile_phone="89655783498", work_phone="812-567-90-89", phone2="812-789-56-37")
        if app.user.count() == 0:
            app.user.add_new_user(user1)
    with allure.step('Given users phones from view page'):
        user_from_view_page = app.user.get_users_from_view_page(0)
    with allure.step('Given users phones from edit page'):
        user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    with allure.step('Сomparing phones from view page and edit page'):
        assert user_from_view_page.home_phone == user_from_edit_page.home_phone
        assert user_from_view_page.mobile_phone == user_from_edit_page.mobile_phone
        assert user_from_view_page.work_phone == user_from_edit_page.work_phone
        assert user_from_view_page.phone2 == user_from_edit_page.phone2
