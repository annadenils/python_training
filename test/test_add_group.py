# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


def test_add_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.init_group(Group(group_name="new_group", header="logo", comment="comment"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(login_name="admin", password="secret")
    app.group.init_group(Group(group_name="", header="", comment=""))
    app.session.logout()
