"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from proyecto1.views import saludo, fecha, edadf, salcp
from proyecto1.views import salcf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo), # se puede poner el nombre que quieras pero se recomienda el mismo nombre de la vista
    path('saf/',salcf),
    path('sap/', salcp),
    path('hora/', fecha),
    path('edadf/<int:edad>/<int:agno>', edadf),
]
