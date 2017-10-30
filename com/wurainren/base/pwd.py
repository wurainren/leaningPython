# import getpass
#
# username = input("username:")
# password = input("password:")

# If you have Python 2 >=2.7.9 or Python 3 >=3.4 installed from python.org,
# you will already have pip and setuptools, but will need to upgrade to the latest version




def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000


for i in gen():
    print(i)