"""
URL configuration for back_end_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include,re_path
from django_api import views
from rest_framework import routers
from django.conf.urls.static import static

from django.conf import settings

routers = routers.DefaultRouter()
routers.register(r'api/users',views.UsersViewSet)
routers.register(r'api/roles',views.RolesViewSet)
routers.register(r'api/categories',views.CategoriesViewSet)
# routers.register(r'^api/user/(?P<name>\w*)/$',views.GetUserViewSet.as_view())
routers.register(r'api/products',views.ProductsViewSet)
# routers.register(r'api/user/<username>',views.UserDetailViewSet)
# routers.register(r'login',views.LoginView.as_view())
# routers.register(r'user/<int:id>/',views.UserViewSet)
# routers.register(r'users',views.UsersViewSet.as_view()) 
# routers.register(r'login',views.UserViewGet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/login/', views.LoginView.as_view()),
    re_path('^api/user/(?P<name>\w+)/$', views.GetUserViewSet.as_view()),
    path('api/upload/', views.upload_image),
    # path('api/getcsrf/', views.get_csrf),

    # path('api/',include('rest_framework.urls', namespace='rest_framework'))
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += routers.urls
urlpatterns += static(settings.PICTURES_URL, document_root=settings.PICTURES_ROOT)
