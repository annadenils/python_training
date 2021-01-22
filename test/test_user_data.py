from model.users import Users

def test_user_data_on_homepage(app):
    app.open_home_page()
    user1 = Users(users_name="Специальный", users_lastname="Специальнов", address_company="СПб, Мира ул. 6 - 56", home_phone="2345678", mobile_phone="89655783498", work_phone="812-567-90-89", phone2="812-789-56-37")
    if app.user.count() == 0:
        app.user.add_new_user(user1)
    user_from_home_page = app.user.get_users_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.users_name == user_from_edit_page.users_name
    assert user_from_home_page.users_lastname == user_from_edit_page.users_lastname
    assert user_from_home_page.address_company == user_from_edit_page.address_company