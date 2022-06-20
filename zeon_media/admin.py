from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from .models import *

class AboutUsForm(forms.ModelForm):
    decription = forms.CharField(label='Описание', widget=CKEditorUploadingWidget)
    class Meta:
        models = AboutUs
        fields = '__all__'

class AboutUsImageInline(admin.TabularInline):
    model = AboutUsImage
    min_num = 1
    max_num = 3
    extra = 0

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [AboutUsImageInline, ]
    form = AboutUsForm

class SliderImageInline(admin.TabularInline):
    model = SliderImage
    min_num = 1
    max_num = 5
    extra = 0

class SliderAdmin(admin.ModelAdmin):
    inlines = [SliderImageInline, ]


class NewsAdminForm(forms.ModelForm):
    descrintion = forms.CharField(label='Описание', widget=CKEditorUploadingWidget)
    class Meta:
        models = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    form = NewsAdminForm

class PublicOffertForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget)
    class Meta:
        models = PublicOffert
        fields = '__all__'

class PublicOffertAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    form = PublicOffertForm

admin.site.register(CallBack)
admin.site.register(PublicOffert, PublicOffertAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(HelpImage)
admin.site.register(Helpers)
admin.site.register(Slider, SliderAdmin)
admin.site.register(OurAdvantages)


