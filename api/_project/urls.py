from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import SignUp, Email, PasswordChange
from recipes.views import RecipeList, RecipeDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('signup/', SignUp.as_view()),
    path('user/', Email.as_view()),
    path('password/change/', PasswordChange.as_view()),
    path('password/reset/', include('django_rest_passwordreset.urls')),
    path('recipes/', RecipeList.as_view()),
    path('recipes/<int:pk>/', RecipeDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
