from django.urls import path,include
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView


from . import views
from .routers import router

app_name = "data"

urlpatterns = [
    path("", views.index, name="index"),
    # path("<int:id>/", views.profile, name="profile"),
    path('api/', include(router.urls)),
    path('api/auth/password/reset/',PasswordResetView.as_view(),name='rest_password_reset_override'),
    path('api/auth/password/reset/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm_override'),
    path('api/auth/',include('dj_rest_auth.urls')),
    path('api/auth/registration/',include('dj_rest_auth.registration.urls')),
    path('api/auth/social/',include('allauth.socialaccount.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # path('api/test/',views.TestView.as_view())
    path('api/myspaceshare/',views.MySpaceShareView.as_view()),
    path('api/myspaceall/',views.MySpaceAllView.as_view()),
    path('api/orgspace/',views.OrgSpaceView.as_view()),
]