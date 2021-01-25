from model.users import Users
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).replace('  ', ' ').strip(' ')

testdata = [Users(users_name=random_string("", 10), users_lastname=random_string("", 20), users_middlename=random_string("", 20), nickname=random_string("", 15), name_company=random_string("", 15), address_company=random_string("", 30), home_phone="812-567-89-90", mobile_phone="89655783498", work_phone="812-567-90-89", fax="-", email="dfghj@dfgh.ru", email2="rtyu@rt.ru", email3="poiuyt@jg.tu", bday="7", bmonth="March", byear="1971", address2="Спб, Приморский пр. 56", phone2="812-789-56-37") for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
