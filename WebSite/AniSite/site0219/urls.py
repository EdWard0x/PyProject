"""
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
from django.urls import path
from site0219.views import index, data, login

urlpatterns = [
    path('', index.content),
    path('index/', index.main),
    path('data/list/', data.list),
    path('data/rank/', data.rank),
    path('data/piechart/', data.pie_chart),
    path('data/histogramchart/', data.histogram_chart),

    path('login/', login.main),
    path('imgcode/', login.imgcode),
    path('logout/', login.logout),
]

