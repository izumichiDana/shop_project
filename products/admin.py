from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 12
    min_num = 1
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [ProductImageInline,]
    form = ProductAdminForm

admin.site.register(Product, ProductAdmin)
admin.site.register(Collections)




