from rest_framework import viewsets
from .serializer import EmployeeSerializer
from .models import Employee
# Create your views here.
class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()