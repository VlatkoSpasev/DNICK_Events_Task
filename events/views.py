from django.shortcuts import render
from .forms import EventForm
from .models import BandEvent, Bands, Event
from datetime import datetime

def add_event(request):
    form = EventForm()
    all_events_in_future = Event.objects.filter(date__gte=datetime.now().date()).all()
    extra_context = {'form': form, 'all_events': all_events_in_future}
    if request.method == 'POST':
        event_form = EventForm(request.POST, files = request.FILES)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.poster = event_form.cleaned_data['poster']
            event.user = request.user
            event.save()
            bands = event_form.cleaned_data['bands']
            band_list = bands.split(",")
            for band in band_list:
                band_obj = Bands.objects.filter(name=band).first()
                if band_obj:
                    band_obj.n_events = band_obj.n_events+1
                    band_obj.save()
                    BandEvent.objects.create(band=band_obj, event=event)
    return render(request, 'add_event.html', context=extra_context)