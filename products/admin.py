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

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug','created_at', )
    inlines = [ProductImageInline,]
    form = ProductAdminForm
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)
admin.site.register(Collections, CollectionAdmin)




