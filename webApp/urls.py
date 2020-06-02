from django.conf.urls import url
from django.urls import path
from .views import categoryView, tagView, productView, signupView, loginView, logoutView

app_name = "webapp"


urlpatterns = [
    path(r'category/', categoryView.as_view(), name='category'),
    path(r'tag/', tagView.as_view(), name='tag'),
    path(r'product/', productView.as_view(), name='product'),
    path("", loginView, name="login"),
    url(r'signup/', signupView, name='signup'),
    path("logout", loginView, name="logout"),
]