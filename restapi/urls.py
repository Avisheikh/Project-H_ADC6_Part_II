from django.urls import path
from restapi.views import *
urlpatterns=[
    path('VC',View_And_Create),
    path('VDU/<int:Id>',ViewId_Delete_Update),
    path('Page/<int:pageNo>/<int:Size>',pagination)
]