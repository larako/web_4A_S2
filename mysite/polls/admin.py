from django.contrib import admin
#from .models import User
from .models import Categories
from .models import Spectacles
from .models import Artistes
from .models import Purchase
from .models import Resource
#from django.contrib.auth.models import User

#admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Spectacles)
admin.site.register(Artistes)
admin.site.register(Purchase)
admin.site.register(Resource)
# Register your models here.
