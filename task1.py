from datetime import datetime
t= input ("test")
t2 = datetime.strptime('Sun 10 May 2015 13:54:36 -0700', '%a %d %b %Y %H:%M:%S %z')
t1 = datetime.strptime('Sun 10 May 2015 13:54:36 -0000', '%a %d %b %Y %H:%M:%S %z')
diff = (t2 - t1).seconds
print (diff)

