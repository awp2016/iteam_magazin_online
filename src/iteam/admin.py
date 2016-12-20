from iteam.models import User
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    exclude = ["password", "is_active", "is_admin", "date_joined"]


admin.site.register(User, UserAdmin)
