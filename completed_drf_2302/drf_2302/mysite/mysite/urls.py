"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from movies import views as mviews
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.SimpleRouter()
router.register("movies", mviews.MovieViewSet, basename = "movies")
router.register("action", mviews.ActionViewSet, basename = "action")
router.register("comedy", mviews.ComedyViewSet, basename = "comedy")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    
]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
