import re
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
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(user_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(users):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [users.home_phone, users.mobile_phone, users.work_phone, users.phone2]))))

def merge_email_like_on_home_page(users):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [users.email, users.email2,
                                                                               users.email3]))))