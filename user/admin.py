from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','first_name','last_name','is_active']
    search_fields = ['email','first_name','last_name']
    ordering = ['created_at']
    readonly_fields = ['created_at','updated_at']

    fieldsets=(
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','type','profile_pic')}),
        ('Permissions', {'fields':('is_active','is_staff','is_superuser')}),
        ('Time',{'fields':('created_at','updated_at')}),
    )

    def save_models(self, request, obj, form, change):

        if not change:
            obj.set_password(obj.password)

        else:
            if 'password' in form.cleaned_data:
                obj.set_password(obj.password)

        super().save_model(request, obj, form, change)
