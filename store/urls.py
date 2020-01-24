from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', store , name='store'),
    path("admin_products/restricted/",admin_restricted),
    path('admin_products/',admin_page, name='admin'),
    path('admin_products/upload/',upload),
    path('admin_products/upload/save/',uploaded_save),
    path('admin_products/edit/<int:id>',get_product),
    path('admin_products/edit/update/<int:id>', update_product),
    path('admin_products/delete/<int:id>', delete_product),
    path("admin_products/search/", search),
    path("search/",store_search),
    path('admin_products/uploaded_file/',upload_list),
    path('admin_products/upload_file/',upload_file),
    path("admin_products/uploaded_file/delete/<int:id>",run),
    path("page/<int:pageNo>/",pagination),
    path("admin_products/page/<int:pageNo>/",paginationForCRUD)
    
]



