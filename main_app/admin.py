from django.contrib import admin

# Register your models here.

from .models import Visit, Study, SampleType, Group, GroupSet, VisitType

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
	list_display = ('name', 'timepoint')
	
@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
	list_display = ('name',)
	
@admin.register(SampleType)
class SampleTypeAdmin(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	list_display = ('name',)
	
@admin.register(GroupSet)
class GroupSetAdmin(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(VisitType)
class VisitTypeAdmin(admin.ModelAdmin):
	list_display = ('name',)