import string
import random
from julet.weddings.models import Wedding

def wedding_code():
    letters = string.ascii_lowercase
    numbers = string.digits
    chars = letters+numbers
    code = ''.join(random.choice(chars) for x in range(8))
    while Wedding.objects.filter(id=code).count() != 0:
        code = ''.join(random.choice(chars) for x in range(8))
    return code
