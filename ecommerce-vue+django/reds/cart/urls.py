from django.urls import path, include

from cart import views
urlpatterns = [
    path("createCart/",views.createCart)
    path("addtocart/", views.addtocart),
    # path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),

]
