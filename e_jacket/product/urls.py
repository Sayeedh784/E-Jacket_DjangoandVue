from django.urls import path,include

from product import views

urlpatterns = [
  path('latest-product/',views.LatestProductList.as_view(),name="")
]