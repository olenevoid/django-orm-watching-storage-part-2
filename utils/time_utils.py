from datetime import timedelta, datetime
from django.utils.timezone import localtime


def get_duration(entered_at: datetime) -> timedelta:
    duration = localtime() - localtime(entered_at)
    return duration


def format_duration(duration: timedelta):
    total_seconds = int(duration.total_seconds())
    total_minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(total_minutes, 60)
    return f'{hours}:{minutes:02}:{seconds:02}'
