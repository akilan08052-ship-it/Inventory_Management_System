from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Supplier)
admin.site.register(Catogery)
admin.site.register(Unit)
admin.site.register(Product)
admin.site.register(Purchase)



