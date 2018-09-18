from django.urls import path, include
from .views import (
    ListTripView,
    CreateTripView,
    RetrieveTripView,
    UpdateStartTripView,
    UpdateEndTripView
)

urlpatterns = [
    path('', ListTripView.as_view(), name='list-trips'),
    path('create/', CreateTripView.as_view(), name='create-trip'),
    path('trip/<int:pk>/', RetrieveTripView.as_view(), name='retrieve-trip'),
    path('trip/<int:pk>/start/', UpdateStartTripView.as_view(), name='update-start-trip'),
    path('trip/<int:pk>/end/', UpdateEndTripView.as_view(), name='update-end-trip')
]