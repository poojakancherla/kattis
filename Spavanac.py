from datetime import datetime, timedelta
H, M = map(int, input().split(' '))
given_time = datetime(2017,1,1,hour=H, minute=M)
actual_time = given_time - timedelta(minutes=45)
print (actual_time.hour, actual_time.minute)
