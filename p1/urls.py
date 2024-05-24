"""p1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from p1App.views import *
from p1App.investor_views import *
from p1App.innovator_views import *
from rest_framework.authtoken.views import ObtainAuthToken
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
=======
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
>>>>>>> 2c68e8e (messgage)

router.register('messages/', MessageViewSet,basename="msg")


urlpatterns = [
    
    
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('innovator/register/',InnovatorReg.as_view(),name="innovator_reg"),
    path('invester/register/',InvesterReg.as_view(),name="invester_reg"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(),name="logout"),
    
    #innovator Urls
    
    path("project/",ProjectApi.as_view(),name="pjct"),
    path("project/<int:pk>",ProjectApi.as_view(),name="pjct"),
    path("category/",CatogariView.as_view(),name="category"),
    path("update/<int:pk>",UpdateView.as_view(),name="update"), #updates of projects from innovator
    
    #investor Urls
    path("projectview/<int:pk>",ProjectView.as_view(),name="prjview"),
<<<<<<< HEAD

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path("update/",UpdateView.as_view(),name="update"),
]+router.urls
>>>>>>> 2c68e8e (messgage)
