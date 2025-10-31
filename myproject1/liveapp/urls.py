from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_session, name='start_session'),
    path('session/<str:unique_id>/', views.session_view, name='session_view'),
]
