import datetime
import pytz
import random
import string


r = random.SystemRandom()

def random_string(length=127):
    return ''.join(r.choices(string.ascii_letters + string.digits, k=length))


def utc_now():
    return pytz.utc.localize(datetime.datetime.utcnow())
