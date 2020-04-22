from functools import wraps
from django.db.models import F
from django.db import transaction
from .models import BaseProduct

def counted(f):
    @wraps(f)
    def decorator(request, region,category, slug):
        with transaction.atomic():
            counter, created = BaseProduct.objects.get_or_create(slug=slug)
            counter.views = F('views') + 1
            counter.save()
        return f(request, region,category, slug)
    return decorator