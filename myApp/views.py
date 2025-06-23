from django.shortcuts import render
from .models import TrackDatas
from .models import Testimonial
from .models import Contacts
from .models import Newsletter
from django.contrib import messages



# Create your views here.
def index(request):
    if request.method == 'POST':
       
        email = request.POST['email']
        
        news = Newsletter(email=email)
        news.save()
        messages.success(request, f'Hurray!!! You will now receive hot offers and new updates from us')
    return render(request, 'index.html')

def track(request):
    if request.method == "POST":
        tracking_id = request.POST.get('tracking_id')
        print (tracking_id)
        try:
            tracking_data = TrackDatas.objects.get(track_Number=tracking_id)
            return render(request, "test.html", {"tracking_data": tracking_data})
        except TrackDatas.DoesNotExist:
            return render(request, 'error.html')

    return render(request, 'track.html')

def details(request):

    return render(request, 'details.html')

def test(request):

    return render(request, 'test.html')

def testimony(request):


    test = Testimonial.objects.all()
    return render(request, 'testimony.html', {"test":test})

def error(request):

    return render(request, 'error.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        user_request = Contacts(name=name, email=email, subject=subject, message=message)
        user_request.save()
        messages.success(request, f'We have received your message, We will get back to you shortly via the email provided')

    return render(request, 'contact.html')