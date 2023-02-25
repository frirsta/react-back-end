from django.urls import path
from follow import views

urlpatterns = [
    path('follow/', views.FollowList.as_view()),
    path('follow/<int:pk>', views.FollowDetail.as_view()),
]
