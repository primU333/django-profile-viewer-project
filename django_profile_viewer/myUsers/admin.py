from django.contrib import admin
from myUsers.models import Profile
from django.contrib.auth.admin import UserAdmin


class ProfileAdmin(UserAdmin):
	list_display = ('email','username','first_name','gender', 'last_name', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('first_name', 'last_name')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Profile, ProfileAdmin)