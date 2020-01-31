from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)               

def about(request):
<<<<<<< HEAD
    context_dict = {'boldmessage': 'This tutorial has been put together by Alana Grant'}

    return render(request, 'rango/about.html', context=context_dict)

    
=======
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>.")
                       
>>>>>>> 36559b69b2f3fac92cc2e1f4188d43eb2ec8d20c
