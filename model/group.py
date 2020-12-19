class Group():
    def __init__(self, group_name, header, comment):
        self.group_name = group_name
        self.header = header
        self.comment = comment

class EditGroup():
    def __init__(self, new_group_name, new_comment):
        self.new_group_name = new_group_name
        self.new_comment = new_comment