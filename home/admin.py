from django.contrib import admin
from .models import (
                     PDFUpload,
                     AboutMe,
                     Ability,
                     WhatIOffer,
                     MyOfferHints,
                     App,
                     Contact,
                     WhoAmIPicture
                     )


@admin.register(PDFUpload)
class PDFUploadAdmin(admin.ModelAdmin):
    ...


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'experience_years', 'completed_project')


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('name',)


class OffersInline(admin.TabularInline):
    model = MyOfferHints


@admin.register(WhatIOffer)
class MyOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [OffersInline]


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(WhoAmIPicture)
class WhoAmIAdmin(admin.ModelAdmin):
    ...
