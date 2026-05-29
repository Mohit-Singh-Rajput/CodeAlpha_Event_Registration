from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # This new path passes the specific event ID to our view function
    path('register/<int:event_id>/', views.register_event, name='register_event'),
]