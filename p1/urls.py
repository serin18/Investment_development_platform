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
from django.urls import path
from p1App.views import *
from p1App.investor_views import *
from p1App.innovator_views import *    
from rest_framework.authtoken.views import ObtainAuthToken
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()

# router.register("project/",Project,basename="pjct")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('innovator/register/',InnovatorReg.as_view(),name="innovator_reg"),
    path('invester/register/',InvesterReg.as_view(),name="invester_reg"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(),name="logout"),
    path("project/",ProjectApi.as_view(),name="pjct"),
<<<<<<< HEAD
    path("category/",CatogaryView.as_view(),name="category")

]
=======
    path("project/<int:pk>",ProjectApi.as_view(),name="pjct"),
    path("category/",CatogariView.as_view(),name="category"),
    path("projectview/<int:pk>",ProjectView.as_view(),name="prjview"),
    path("update/",UpdateView.as_view(),name="update"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> f6a76b6aeb9cd02726da79bdb8c653eeead6875f
