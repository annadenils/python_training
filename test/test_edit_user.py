from model.users import Users

def test_edit_user(app):
    app.session.login(login_name="admin", password="secret")
    app.user.edit_user(Users(users_name="Пантелеймон", users_middlename="Иванов", users_lastname="Иванович", nickname="ivan-ivan", name_company=u"ооо \"далеко-далеко\"",
                          address_company="СПб, Мира ул. 6 - 56", home_phone="812-567-89-90", mobile_phone="89655783498", work_phone="812-567-90-89", fax="-",
                          email="dfghj@dfgh.ru", bday="7", bmonth="March", byear="1971", address2="Спб, Приморский пр. 56"))
    app.session.logout()