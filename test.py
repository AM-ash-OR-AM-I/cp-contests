n=int(input())
d=''
while n:d=['GA','BU','ZO','MEU'][n%4]+d;n//=4
print(d+'GA'*(d==''))