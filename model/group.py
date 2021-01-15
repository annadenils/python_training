class Group():
    def __init__(self, group_name=None, header=None, comment=None, id=None):
        self.group_name = group_name
        self.header = header
        self.comment = comment
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.group_name)