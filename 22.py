"""
给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
如：st="00:00:00", et="00:00:10", 则输出10.
"""
st="01:02:00"
et="01:01:10"
if et <st:
    ss=st
    st=et
    et=ss
##print(st)
##print(et)
hour   = (int(et[0:2]) - int(st[0:2]))
minute = (int(et[3:5]) - int(st[3:5]))
second = (int(et[6:8]) - int(st[6:8]))
##print(hour)
##print(minute)
#print(second)
result =second+minute*60+hour*3600
print(result)