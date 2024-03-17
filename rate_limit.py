from datetime import  datetime, timedelta
from collections import deque

def to_time(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")

def rate_limit(logs, rate, request):
    if not logs:
        logs.append(request)
        return True
    
    while logs and to_time(logs[0]) < to_time(request) - timedelta(hours=1):
        logs.popleft()

    if len(logs) < rate:
        logs.append(request)
        return True
    return False

def main(rate, requests):
    logs = deque()
    for request in requests:
        if rate_limit(logs, rate, request):
            print("true")
        else:
            print("false")

rate = 3
requests = [
    "2022-01-20T00:13:05Z",
    "2022-01-20T00:27:31Z",
    "2022-01-20T00:45:27Z",
    "2022-01-20T01:00:49Z",
    "2022-01-20T01:15:45Z",
    "2022-01-20T01:20:01Z",
    "2022-01-20T01:50:09Z",
    "2022-01-20T01:52:15Z",
    "2022-01-20T01:54:00Z",
    "2022-01-20T02:00:00Z"
]

main(rate, requests)
