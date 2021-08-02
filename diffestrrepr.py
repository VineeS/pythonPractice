import pytz
import datetime
a = [1, 2, 3]
b = 'sample string'

print(str(a))  # str goal is to be readable
# repr goal is to be unambiguos (not open to more than one interpretation.)
print(repr(a))

print(str(b))
print(repr(b))
print()


x = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

y = str(x)

print('str(x): {}'.format(str(x)))
print('str(y): {}'.format(str(y)))
print()

print('repr(x): {}'.format(repr(x)))
print('repr(y): {}'.format(repr(y)))

# https://www.youtube.com/watch?v=5cvM-crlDvg
