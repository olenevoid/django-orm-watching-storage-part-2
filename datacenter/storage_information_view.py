from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from utils.time_utils import get_duration, format_duration


def storage_information_view(request):
    # Программируем здесь
    visits = Visit.objects.filter(leaved_at=None).all()

    non_closed_visits = []
    for visit in visits:
        duration = get_duration(visit.entered_at)
        
        non_closed_visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
        }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
