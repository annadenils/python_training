from model.users import EditUsers


def test_edit_user(app):
    app.session.login(login_name="admin", password="secret")
    app.user.edit_user(EditUsers(new_users_name="Пантелеймон", new_name_company=u"ооо \"далеко-далеко\""))
    app.session.logout()