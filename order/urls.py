from django.urls import path, include


from order import views


urlpatterns = [

    path('checkout/', views.checkout),

]
