from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
# Create your views here.

#def home (request):
#    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')
        print(name, email, number, content)

        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'Name should be between 1 and 30 characters')
            return render(request, 'home.html')

        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'Email should be between 1 and 30 characters')
            return render(request, 'home.html')

        if len(number)>8 and len(number)<12:
            pass
        else:
            messages.error(request,'Invalid number try again')
            return render(request, 'home.html')

        yog = models.Contact(name=name, email=email, number=number, content=content)
        yog.save()
        messages.success(request, 'Your message has been sent successfully')
        print('Data saved')

    return render(request, 'home.html')
