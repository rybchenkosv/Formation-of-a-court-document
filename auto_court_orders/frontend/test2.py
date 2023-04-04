from datetime import date
import datetime

a = '22.05.1995'
a = a.split('.')
aa = datetime.date(int(a[2]),int(a[1]),int(a[0]))
bb = datetime.date.today()
cc = abs(aa-bb)
dd = (str(cc)).split()[0]

print(dd)