from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import timedelta, datetime


def get_duration(entered_at: datetime) -> timedelta:
    duration = localtime() - localtime(entered_at)
    return duration


def format_duration(duration: timedelta):
    total_seconds = int(duration.total_seconds())
    total_minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(total_minutes, 60)
    return f'{hours}:{minutes:02}:{seconds:02}'


def storage_information_view(request):
    # Программируем здесь

    non_closed_visits = [
        {
            'who_entered': 'Richard Shaw',
            'entered_at': '11-04-2018 25:34',
            'duration': '25:03',
        }
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
