from django.contrib import admin
from childcare.apps.progress.models import Activity, ActivityCategory

admin.site.register(Activity)
admin.site.register(ActivityCategory)