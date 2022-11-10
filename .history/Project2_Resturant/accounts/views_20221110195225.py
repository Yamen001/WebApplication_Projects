from django.shortcuts import render

# Create your views here.

def register(request):
    


def register(request):
    if request.method == 'POST':
        firstname = request.POST('firstname')
        lastname = request.POST('lastname')
        email = request.POST('email')
        password = request.POST('password')
        phone_number = request.POST('phone_number')
        address = request.POST('address')
        user = User.objects.create_user(firstname = firstname, lastname = lastname, email = email, password = password, phone_number = phone_number,address = address)
        user.save();
        print("user created")
        return redirect('/')
    return render(request, 'register.html')

    return render(request, 'register.html')