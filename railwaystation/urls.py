"""railwaystation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from railway import views

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', views.showIndex),

    url(r'^register/', views.Register),
    url(r'^registeration/', views.Registration),

    url(r'^alreadyaccountexist/', views.AlreadyAccoutExist),

    url(r'^tickestsbooking/', views.TicketsBooking),

    url(r'^searchtrain/', views.searchtrain),

    url(r'^generalreservation/', views.GeneralReservation),

    url(r"^searchseatsavailabilty/", views.searchseatsavailabilty),

    url(r'^pay/', views.payment1),
    url(r'^payment/', views.paymentdetails),

    url(r'^ladies/', views.LadiesReservation),

    url(r'^tatkal/', views.TatkalReservation),

    url(r'^lowerberth/', views.LowerBerthReservation),
    url(r'^srcitizen/', views.SrCitizenReservation),
    url(r'^permiumtatkal/', views.PermimumTatkalReservation),

    url(r"^logout/", views.Logout),
    ]
