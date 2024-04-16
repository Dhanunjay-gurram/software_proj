from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth import get_user_model

class CustomLoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = get_user_model()  # Fetch the custom user model
        user = User.objects.filter(username=username).first()
        if user is not None and (user.password==password):
            login(request, user)
            user_type = user.user_type
            if user_type == 1:
                return redirect('/manager/dashboard/')
            elif user_type == 2:
                return redirect('/accountclerk/dashboard/')
            elif user_type == 3:
                return redirect('/salesperson/dashboard/')
            elif user_type == 4:
                return redirect('/spectators/dashboard/')
            else:
                return redirect('default_dashboard')
        else:
            return redirect('login')
