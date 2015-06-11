from django.contrib import admin
from .models import Flat
from .models import House
from .models import Hostel

# Register your models here.

admin.site.register(Flat)
admin.site.register(House)
admin.site.register(Hostel)


