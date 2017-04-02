from django.contrib import admin
from .models import User
from .models import Categories
from .models import Spectacles
from .models import Artistes

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Spectacles)
admin.site.register(Artistes)
# Register your models here.
