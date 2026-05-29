from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Registration

def home(request):
    all_events = Event.objects.all()
    return render(request, 'events/home.html', {'events': all_events})

# @login_required ensures only logged-in users can trigger this function
@login_required(login_url='/admin/')
def register_event(request, event_id):
    if request.method == 'POST':
        # Find the specific event they clicked
        event = get_object_or_404(Event, id=event_id)
        
        # Create the registration linking the current user and the event
        # get_or_create prevents duplicate registrations if they click twice
        Registration.objects.get_or_create(participant=request.user, event=event)
        
        # Send them back to the homepage
        return redirect('home')