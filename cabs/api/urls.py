from django.urls import path, include
from .views import (
    ListCabView,
    CreateCabView,
    RetrieveCabView,
    UpdateCabView
)

urlpatterns = [
    path('', ListCabView.as_view(), name='list-cabs'),
    path('create/', CreateCabView.as_view(), name='create-cab'),
    path('cab/<int:pk>/', RetrieveCabView.as_view(), name='retrieve-cab'),
    path('cab/<int:pk>/update/', UpdateCabView.as_view(), name='update-cab')
]