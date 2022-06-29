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

    def has_add_permission(self, request):
        # check if generally has add permission
        permissions = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if permissions and AboutUs.objects.exists():
            permissions = False
        return permissions

class SliderImageInline(admin.TabularInline):
    model = SliderImage
    min_num = 1
    max_num = 5
    extra = 0

class SliderAdmin(admin.ModelAdmin):
    inlines = [SliderImageInline, ]
    list_display = ('urlka',)

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

    def has_add_permission(self, request):
        permissions = super().has_add_permission(request)
        if permissions and PublicOffert.objects.exists():
            permissions = False
        return permissions

class CallBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_num', 'created_at', 'callback_type', 'status_call',)

class HelpersInline(admin.TabularInline):
    model = Helpers
    min_num = 1
    max_num = 12
    extra = 0

class HelpAdmin(admin.ModelAdmin):
    fields = ('images', )
    list_display = ('images', )
    inlines = [HelpersInline, ]

# class HelpersAdmin(admin.ModelAdmin):
#     list_display = ('question', 'answer', 'help')

class FuterLinkAdmin(admin.ModelAdmin):
    fields = ('num', 'whatsapp', 'instagram', 'mail', 'telegram', 'name' , 'number')
    list_display = ('num', 'whatsapp', 'instagram', 'mail', 'telegram', 'name' , 'number')

    def has_add_permission(self, request):
        permissions = super().has_add_permission(request)
        if permissions and FuterLink.objects.exists():
            permissions = False
        return permissions

class FuterAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'information', 'heder_image', 'futer_image')

    def has_add_permission(self, request):
        permissions = super().has_add_permission(request)
        if permissions and Futer.objects.exists():
            permissions = False
        return permissions

admin.site.register(CallBack, CallBackAdmin)
admin.site.register(PublicOffert, PublicOffertAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(OurAdvantages)
admin.site.register(HelpImage, HelpAdmin)
admin.site.register(Futer, FuterAdmin)
admin.site.register(FuterLink, FuterLinkAdmin)


