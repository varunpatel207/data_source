from django.conf.urls import url
from apps.views.android_app_views import AndroidAppViews

app_name = "android-app"

urlpatterns = [
    url('', AndroidAppViews.dashboard, name='dashboard'),
]
