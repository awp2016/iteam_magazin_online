from django.contrib import admin
from iteam.models import Product
from iteam.models import User
from iteam.models import Review


class UserAdmin(admin.ModelAdmin):
    exclude = ["password", "is_active", "is_admin", "date_joined"]


admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Review)
