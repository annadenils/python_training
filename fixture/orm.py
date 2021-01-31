from pony.orm import *
from datetime import datetime
from model.group import Group
from model.users import Users

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMUsers(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), group_name=group.name, header=group.header, comment=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_user_list(self):
        return self.convert_users_to_model(select(c for c in ORMFixture.ORMUsers if c.deprecated is None))

    def convert_users_to_model(self, users):
        def convert(user):
            return Users(id=str(user.id), users_name=user.firstname, users_lastname=user.lastname)
        return list(map(convert, users))

