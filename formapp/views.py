from django.shortcuts import render
from formapp import forms
from .models import Emp
from django.urls import reverse
from django.http import HttpResponseRedirect
def empview(request):
    form=forms.EmpForm()
    if request.method=='POST':
        form=forms.EmpForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            form.save(commit=True)
            # redirect to another page after submission
            return HttpResponseRedirect(reverse('view'))


    return render(request,'registration.html',{'form':form})
def viewemp(request):
    detail=Emp.objects.all()
    mydict={'emp':detail}
    return render(request,'detailpage.html',context=mydict)

