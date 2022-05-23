from django.urls import path
from restAPI.v1.views import account_views, news_views, contact_views
from rest_framework_simplejwt.views import token_refresh

urlpatterns = [
    # account
    path('users/', account_views.UserList.as_view()),
    path('users/<int:pk>', account_views.UserDetail.as_view()),
    path('users/me', account_views.CurrentUser.as_view()),
    path('register/', account_views.RegisterApi.as_view()),
    path("login/", account_views.Login.as_view()),
    path("token-refresh/", token_refresh),
    path('logout', account_views.LogoutView.as_view()),

    path('user-type/', account_views.UserTypeListCreateAPIView.as_view()),
    path('user-type/<int:pk>', account_views.UserTypeDetailAPIView.as_view()),

    path('customerID/', account_views.CustomerIDListCreateAPIView.as_view()),
    path('customerID/<int:pk>', account_views.CustomerIDDetailAPIView.as_view()),

    # news
    path('news/', news_views.NewsListCreateAPIView.as_view()),
    path("news/<slug:slug>", news_views.NewsDetailAPIView.as_view()),

    # contact
    path('contact/', contact_views.ContactListCreateAPIView.as_view()),
    path('contact/<int:pk>', contact_views.ContactDetailAPIView.as_view()),
]