"""notification_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from service.views import *

router = SimpleRouter()

router.register('api/mailinglist', MailinglistAPIView)
router.register('api/mailinglist/<int:id>/', MailinglistAPIView)
router.register('api/client', ClientAPIView, basename='Clients')
router.register('api/client/<int:id>/', ClientAPIView, basename='Clients_put')
router.register('api/message', MessageAPIView, basename='Messages')
router.register('api/message/<int:id>/', MessageAPIView, basename='Messages_put')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/client/', ClientAPIView.as_view),
    # path('api/mailinglist/', MailinglistAPIView.as_view)
]

urlpatterns += router.urls

# ?format=json
