from sys import maxsize

class Group():
    def __init__(self, group_name=None, header=None, comment=None, id=None):
        self.group_name = group_name
        self.header = header
        self.comment = comment
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.group_name, self.header, self.comment)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.group_name == other.group_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize