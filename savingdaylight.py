from datetime import datetime
from datetime import timedelta
import sys

for line in sys.stdin:
    line=line[:-1]
    month, day, year, s1, s2 = map(str, line.split())
    FMT = '%H:%M'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    if tdelta.days < 0:
        tdelta = timedelta(days=0,
                    seconds=tdelta.seconds, microseconds=tdelta.microseconds)
    s=str(tdelta)
    s=s[:-3]
    h1,m1=s.split(":")
    if m1[0]=="0":
        m1=m1[-1]
    print(month, day, year, h1+' hours '+m1+' minutes')
