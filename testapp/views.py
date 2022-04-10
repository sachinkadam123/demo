from django.shortcuts import render
from .models import Employee


# Create your views here.
def empdata(request):
    emp_list=Employee.object.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/emp.html',context=my_dict)
