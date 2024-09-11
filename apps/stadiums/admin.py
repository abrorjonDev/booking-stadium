from django.contrib import admin
from django import forms
from mapwidgets.widgets import GoogleMapPointFieldWidget
from .models import Stadium


class StadiumAdminForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = '__all__'
        widgets = {
            'location': GoogleMapPointFieldWidget,
        }

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    form = StadiumAdminForm
    list_display = ('id', 'name', 'price')
    raw_id_fields = ('creator', 'updater', 'deleter')
