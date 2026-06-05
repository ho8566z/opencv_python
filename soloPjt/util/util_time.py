from datetime import datetime

def getCurrentTime():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')