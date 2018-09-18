from django.urls import path, include
from .views import (
    ListAccountView,
    CreateAccountView,
    RetrieveAccountView
)

urlpatterns = [
    path('', ListAccountView.as_view(), name='list-accounts'),
    path('create/', CreateAccountView.as_view(), name='create-account'),
    path('account/<int:pk>/', RetrieveAccountView.as_view(), name="retrieve-account")
]