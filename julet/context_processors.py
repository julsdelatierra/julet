from datetime import datetime
from django.conf import settings

def default(request):
    return {
        'year':datetime.today().year,
        'product_name':settings.PRODUCT_NAME,
        'product_desc':settings.PRODUCT_DESCRIPTION,
        'product_url':settings.URL,
    }
