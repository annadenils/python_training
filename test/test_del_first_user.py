from model.users import Users

def test_del_first_user(app):
    if app.user.count() == 0:
        app.user.add_new_user(Users(users_name="специальный юзер"))
    app.user.del_first_user()