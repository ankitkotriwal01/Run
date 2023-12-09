# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import streamlit_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('streamlit/', streamlit_view, name='streamlit_view'),
]
