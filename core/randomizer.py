import string
import random

"""Class to generate random data, which can be used in tests"""


class Randomizer(object):
    def number(size=10, chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def word(size=10, chars=string.ascii_uppercase + string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))

    def text(min_size=50, max_size=100, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + " "):
        return ''.join(random.choice(chars) for _ in range(random.randint(min_size, max_size)))

    # Same to text but with "\n" (new line) char.
    def page_of_text(min_size=50, max_size=100, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + " " + "\n"):
        return ''.join(random.choice(chars) for _ in range(random.randint(min_size, max_size)))

    def email(base_email='test+', base_domain ='ciklum.com'):
        email = base_email
        email += ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
        email += '@'
        email += 'gmail.com'
        return email

    def password(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(size))