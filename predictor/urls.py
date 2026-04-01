from django.urls import path
from . import views

urlpatterns = [
    path('',           views.login_page, name='login'),
    path('home/',      views.home,       name='home'),
    path('predict/',   views.predict,    name='predict'),
    path('dashboard/', views.dashboard,  name='dashboard'),
    path('simulator/', views.simulator,  name='simulator'),
    path('analytics/', views.analytics,  name='analytics'),
    path('reports/',   views.reports,    name='reports'),   # FIX: added name='reports'
]