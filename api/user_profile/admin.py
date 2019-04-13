from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ('username', 'email')
    fieldset = (
        (
            None,
            { 'fields': ('username', 'email', 'password', 'full_name')}
        ),
    )


class JournalInline(admin.TabularInline):
    model = models.Journals
    extra = 1

class ConfrenceInline(admin.TabularInline):
    model = models.Confrences
    extra = 1

class ProfileLinkInline(admin.TabularInline):
    model = models.ProfileLinks


@admin.register(models.Profile)
class User_Profile(admin.ModelAdmin):
    list_display = ('user', )
    fieldsets = (
        (
            'Detail',
            {'fields': ('bio', 'area_of_interests', 'department', 'institution')}
        ),
    )
    inlines = (JournalInline, ConfrenceInline, ProfileLinkInline)