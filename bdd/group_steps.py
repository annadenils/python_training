from pytest_bdd import given, when, then
from model.group import Group

@given("a group list", target_fixture="group_list")
def group_list(db):
    return db.get_group_list()

@given("a new group with <group_name>, <header> and <comment>", target_fixture="new_group")
def new_group(group_name, header, comment):
    return Group(group_name=group_name, header=header, comment=comment)

@when("i add the group to the list")
def add_new_group(app, new_group):
    app.group.init_group(new_group)

@then("the new group list is equal to the old list with the added group")
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)