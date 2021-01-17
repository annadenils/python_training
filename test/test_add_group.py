# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="new_group", header="logo", comment="comment")
    app.group.init_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="", header="", comment="")
    app.group.init_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
