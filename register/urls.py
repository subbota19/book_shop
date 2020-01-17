from django.urls import path, include
from .views import ViewSubscribersForm, sign_up
from .views import redirect_register

urlpatterns = [
    path('sign_in', ViewSubscribersForm.as_view(), name='sign_in'),
    path('sign_up', sign_up, name="sign_up")
]
