from django.contrib import admin
from startproject.apps.progress.models import Activity, ActivityCategory

admin.site.register(Activity)
admin.site.register(ActivityCategory)