import hashlib
from urllib.parse import urlencode

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = 'https://scontent.fmnl2-1.fna.fbcdn.net/v/t1.0-9/24068238_163359881065578_3444445912592642334_n.jpg?_nc_cat=0&oh=3785f51bdf0b42f71f5a500d5a21180c&oe=5B766D35'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )
    return url