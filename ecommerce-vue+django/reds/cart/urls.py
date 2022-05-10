from django.urls import path, include

from cart import views
urlpatterns = [
    path("createCart/",views.createcart),
    path("updatecart/", views.updatecart),
    path("cart/",views.cart_.as_view())
    # path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),

]
