
from Time import *
from links import *
sp="____________________________"
notify=['The last date to pay the Tution Fees for 2020-21 without fine is 28.09.2020. From 29.09.2020 to 15.10.2020 payment of tuition fee with a fine of Rs 100/-']
def notification():
   return(notify)
def check():
  y = day()
  t = gettime()
  if y=='0' or c[0]=='0':
    return('Today is a holiday !')

  elif t>='09:00:00' and t<'10:00:00' :
    return('Now :-'+y[0])
  elif t>='10:00:00' and t<'11:00:00' :
    return('Now :-\n'+y[1])
  elif t>='11:00:00' and t<'11:30:00' :
    return('Now :-\n'+y[2])
  elif t>='11:30:00' and t<'12:30:00' :
    return('Now :-\n'+y[3])
  elif t>='12:30:00' and t<'13:30:00' :
    return('Now :-\n'+y[4])
  elif t>='13:30:00' and t<'14:30:00' :
    return('Now :-\n'+y[5])
  elif t>='14:30:00' and t<'15:30:00' :
    return('Now :-\n'+y[6])
  elif t>='15:30:00' and t<'16:30:00' :
    return('Now :-\n'+y[7])
  elif t>='16:30:00' and t<'17:30:00' :
    return('Now :-\n'+y[8])
  else:
    return('Now there is no class scheduled !')
def nextcl():
  y = day()
  #z = link()
  t = gettime()
  if y=='0' or c[0]=='0':
    return('Today is a holiday !')
  elif t>='00:00:00' and t<'09:00:00':
    return('Next ->'+y[0])
  elif t>='09:00:00' and t<'10:00:00' :
    return('Next ->\n'+y[1])
  elif t>='10:00:00' and t<'11:00:00' :
    return('Next ->\n'+y[2])
  elif t>='11:00:00' and t<'11:30:00' :
    return('Next ->\n'+y[3])
  elif t>='11:30:00' and t<'12:30:00' :
    return('Next ->\n'+y[4])
  elif t>='12:30:00' and t<'13:30:00' :
    return('Next ->\n'+y[5])
  elif t>='13:30:00' and t<'14:30:00' :
    return('Next ->\n'+y[6])
  elif t>='14:30:00' and t<'15:30:00' :
    return('Next ->\n'+y[7])

  elif t>='15:30:00' and t<'16:30:00' and ( d=='Fri'or (c[0]=='1' and c[1]=='5') ):
    return('No classes scheduled next !')
  elif t>='15:30:00' and t<'16:30:00' :
    return('Next ->\n'+y[8])
  else:
    return('No classes scheduled next !')

def day():
  mon = ["\n\nTheory of computation\n\n"+toc()+"\n"+sp,"\nComputer graphics and multimedia\n\n"+cg()+"\n"+sp,"\nBREAK\n"+sp,"\nWeb technology\n\n"+wt()+"\n"+sp,"\n(Offline) Computer networks\n\n"+sp,"\nBREAK\n"+sp,"\nMobile app development\n\n"+mad()+"\n"+sp,"\nMicroprocessor\n\n"+mp()+"\n"+sp,"\nComputer graphics and multimedia  LAB\n\n"+cglab()+"\n\n"]
  tue = ["\n\nComputer graphics and multimedia\n\n"+cg()+"\n"+sp,"\nComputer networks\n\n"+cn()+"\n"+sp,"\nBREAK\n"+sp,"\nTheory of computation\n\n"+toc()+"\n"+sp,"\n(Offline) Mobile app development\n\n"+sp,"\nBREAK\n"+sp,"\nMicroprocessor\n\n"+mp()+"\n"+sp,"\nWeb technology\n\n"+wt()+"\n"+sp,"\nComputer networks LAB\n\n"+cnlab()+"\n\n"]
  wed = ["\n\nComputer networks\n\n"+cn()+"\n"+sp,"\nMobile app development\n\n"+mad()+"\n"+sp,"\nBREAK\n"+sp,"\nMicroprocessor\n\n"+mp()+"\n"+sp,"\n(Offline) Web technology\n\n"+sp,"\nBREAK\n"+sp,"\nComputer graphics and multimedia\n\n"+cg()+"\n"+sp,"\nTheory of computation\n\n"+toc()+"\n"+sp,"\nMicroprocessor LAB\n\n"+mplab()+"\n\n"]
  thu = ["\n\nMicroprocessor\n"+mp()+"\n"+sp,"\nWeb technology\n\n"+wt()+"\n"+sp,"\nBREAK\n"+sp,"\nMobile app development\n\n"+mad()+"\n"+sp,"\n(Offline) Computer graphics and multimedia\n\n"+sp,"\nBREAK\n"+sp,"\nTheory of computation\n\n"+toc()+"\n"+sp,"\nComputer networks\n\n"+cn()+"\n"+sp,"\nIndustrial training\n\n"+it()+"\n\n"]
  fri = ["\n\nWeb technology\n\n"+wt()+"\n"+sp,"\nMobile app development\n\n"+mad()+"\n"+sp,"\nBREAK\n"+sp,"\nComputer networks\n\n"+cn()+"\n"+sp,"\n(Offline) Theory of computation\n\n"+sp,"\nBREAK\n"+sp,"\nComputer graphics and multimedia\n\n"+cg()+"\n"+sp,"\nPlacement and training\n\n"+pt()+"\n"+sp,"\nPlacement and training\n\n"+pt()+"\n\n"]
  sat=' '
  if c[1]=='1':
    sat=mon
  elif c[1]=='2':
    sat=tue
  elif c[1]=='3':
    sat=wed
  elif c[1]=='4':
    sat=thu
  elif c[1]=='5':
    sat=fri

  if d() == 'Mon':
    return(mon)
  elif d() == 'Tue':
    return(tue)
  elif d() == 'Wed':
    return(wed)
  elif d() == 'Thu':
    return(thu)
  elif d() == 'Fri':
    return(fri)
  elif d() == 'Sat':
    return(sat)
  elif d() == 'Sun':
    return('0')
  else :
    return('0')
def table():
  g = day()
  k = gettime()
  print(k)
  if g == '0' or c[0]=='0':
    return('Today is a holiday')
  elif k <= '23:59:59' and k >= '17:30:00':
    return('Todays classes are over !')
  else :
    return("09:00 - 10:00   "+g[0]+"\n\n10:00 - 11:00   "+g[1]+"\n\n11:00 - 11:30   "+g[2]+"\n\n11:30 - 12:30   "+g[3]+"\n\n12:30 - 01:30   "+g[4]+"\n\n01:30 - 02:30   "+g[5]+"\n\n02:30 - 03:30   "+g[6]+"\n\n03:30 - 04:30   "+g[7]+"\n\n04:30 - 05:30   "+g[8])
