from django.urls import path, include


from order import views


urlpatterns = [

    path('checkout/', views.checkout),
    path('orders/', views.OrderList.as_view()),

]
