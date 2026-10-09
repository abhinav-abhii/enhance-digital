from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lead


def home(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        message = request.POST.get('message')

        if name and email and message:

            Lead.objects.create(
                name=name,
                email=email,
                company=company,
                message=message
            )

            messages.success(
                request,
                'Thanks! Your message has been sent successfully.'
            )

            return redirect('home')

        messages.error(
            request,
            'Please fill in all required fields.'
        )

    return render(request, 'website/home.html')