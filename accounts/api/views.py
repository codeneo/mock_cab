from accounts.models import Account
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView
)
from .serializers import (
    ListAccountSerializer,
    CreateAccountSerializer,
    RetrieveAccountSerializer
)

class ListAccountView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = ListAccountSerializer

class CreateAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializer

class RetrieveAccountView(RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = RetrieveAccountSerializer