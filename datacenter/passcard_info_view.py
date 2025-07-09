from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from utils.time_utils import get_duration, format_duration, is_over_time_limit
from project.settings import VISIT_TIME_LIMIT_IN_MINUTES as TIME_LIMIT
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    
    visits = Visit.objects.filter(passcard=passcard).all()
    this_passcard_visits = []
    for visit in visits:
        if visit.leaved_at:
            duration = get_duration(visit.entered_at, visit.leaved_at)
            visit_has_ended = True
        else:
            duration = get_duration(visit.entered_at)
            visit_has_ended = False

        this_passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
            'has_ended': visit_has_ended,
            'is_strange': is_over_time_limit(duration, TIME_LIMIT)            
        }

        this_passcard_visits.append(this_passcard_visit)    

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
