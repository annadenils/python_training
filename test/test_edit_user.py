from model.users import Users


def test_edit_user(app):
    app.open_home_page()
    if app.user.count() == 0:
        app.user.add_new_user(Users(users_name="специальный юзер"))
    app.user.edit_user(Users(users_name="Николай", name_company=u"ооо\"далеко и близко\""))