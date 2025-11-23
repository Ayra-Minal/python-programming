#
from math import floor
def find_angle(H,M):
    hour_angle=(30*H)+(M/2)
    min_angle=M*6
    diff = abs(min_angle-hour_angle)
    if diff > 180:
        new_diff=360-diff
        diff=new_diff
    return floor(diff)        

H=2
M=30
print (f"Angle between the hands is : ",find_angle(H,M),"degrees.")