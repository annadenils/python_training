# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application_group import Application_group

@pytest.fixture
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(user_name="admin", password="secret")
    app.init_group(Group(group_name="new_group", header="logo", comment="comment"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(user_name="admin", password="secret")
    app.init_group(Group(group_name="", header="", comment=""))
    app.session.logout()
