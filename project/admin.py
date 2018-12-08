from django.contrib import admin
from .models import *

class MemberDetails(admin.ModelAdmin):
    list_display = ['name', 'present_address']

    class Meta:
        model = Member_dtl

admin.site.register(Institute)
admin.site.register(PresentAddress)
admin.site.register(Member_dtl, MemberDetails)
