from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import MyUser, MyUserProfile

from accounts.forms import UserChangeForm, UserCreationForm


         
class UserAdmin(BaseUserAdmin):
    # The forms to add and change
    # user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'nom', 'prenom', 'entreprise', 'candidat', 'admin',)
    list_filter = ('admin', 'entreprise', 'candidat',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('nom', 'prenom',)}),
        ('Permissions', {'fields': ('active', 'admin', 'staff', 'candidat', 'entreprise',)}),
        # (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nom', 'prenom', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    

# Register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
admin.site.register(MyUserProfile)
# Since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
