from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pages)
admin.site.register(Posts)
admin.site.register(Replys)
admin.site.register(Comments)
admin.site.register(UserProfile)
