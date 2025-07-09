from datetime import timedelta, datetime
from django.utils.timezone import localtime


def get_duration(
        entered_at: datetime,
        leaved_at: datetime | None = None
    ) -> timedelta:

    if leaved_at:
        leaved_at = localtime(leaved_at)
    else:
        leaved_at = localtime()

    duration = leaved_at - localtime(entered_at)
    return duration


def format_duration(duration: timedelta) -> str:
    total_seconds = int(duration.total_seconds())
    total_minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(total_minutes, 60)

    return f'{hours}:{minutes:02}:{seconds:02}'


def is_over_time_limit(
        duration: timedelta,
        time_limit_in_minutes: int
    ) -> bool:
    time_limit = timedelta(minutes=time_limit_in_minutes)
    return duration > time_limit
