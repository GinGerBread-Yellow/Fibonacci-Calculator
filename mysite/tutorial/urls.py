from django.urls import path, re_path

from .views import EchoView

urlpatterns = [
    re_path(r'^tutorial/?$', EchoView.as_view()),
    re_path(r'^fibonacci/?$', EchoView.as_view()),
    re_path(r'^logs/?$', EchoView.as_view())
]
