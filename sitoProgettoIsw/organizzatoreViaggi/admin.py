from django.contrib import admin
from .models import CustomUser, Travel, Invitation, Comment

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Travel)
admin.site.register(Invitation)
admin.site.register(Comment)

