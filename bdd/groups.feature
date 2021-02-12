Scenario Outline: Add new group
  Given a group list
  Given a group with <group_name>, <header> and <comment>
  When i add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  | group_name  | header  | comment  |
  | group_name1 | header1 | comment1 |
  | group_name2 | header2 | comment2 |
