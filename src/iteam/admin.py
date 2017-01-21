from django.contrib import admin

from iteam.models import Comment
from iteam.models import Order
from iteam.models import Product
from iteam.models import ShoppingCart
from iteam.models import Order
from iteam.models import Image
from django.contrib import admin
from iteam.models import User


class UserAdmin(admin.ModelAdmin):
    exclude = ["password", "is_active", "is_admin", "date_joined"]


admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Image)
