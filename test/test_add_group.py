# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.init_group(Group(group_name="new_group", header="logo", comment="comment"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.init_group(Group(group_name="", header="", comment=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
