from django.urls import path, include
from .views import HomePageView, PostDetailsView,PortalPageView

# Set the app name for namespacing
app_name = "home"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("portal", PortalPageView.as_view(), name="portal"),
    path('news/<int:news_id>/', PostDetailsView.as_view(), name='news_details'),
]