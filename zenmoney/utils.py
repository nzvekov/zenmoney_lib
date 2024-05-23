from datetime import datetime


def timestamp(date: datetime = None) -> int:
    if date:
        return int(datetime.timestamp(date))

    return int(datetime.timestamp(datetime.now()))
