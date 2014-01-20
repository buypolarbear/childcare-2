from django.contrib import admin

# Register your models here.
from childcare.apps.membermanagement.models import Student, Note, Tenant, UserProfile


class StudentAdmin(admin.ModelAdmin):
    pass


class GuardianAdmin(admin.ModelAdmin):
    pass


class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Tenant)
admin.site.register(UserProfile)