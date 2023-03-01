from django.urls import path
from business import views

urlpatterns = [
    path('business/', views.BusinessProfileList.as_view()),
    path('business/<int:pk>', views.BusinessProfileDetail.as_view()),
]
