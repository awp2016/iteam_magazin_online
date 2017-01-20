from iteam.models import User
from iteam.models import Product
from iteam.models import ShoppingCart
from iteam.models import Order
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    exclude = ["password", "is_active", "is_admin", "date_joined"]


admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(Order)
