from django.contrib import admin
from .models import CustomUser, Farmer, AddFarming,AgroProduct

admin.site.register(CustomUser)
admin.site.register(AddFarming)
admin.site.register(Farmer)
admin.site.register(AgroProduct)