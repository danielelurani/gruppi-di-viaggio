from django.contrib import admin
from .models import CustomUser, Travel, Invitation, Comment, Stage, Expense

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Travel)
admin.site.register(Invitation)
admin.site.register(Comment)
admin.site.register(Stage)
admin.site.register(Expense)

