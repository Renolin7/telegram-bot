from Time import *


temp=['Link not updated !','Link not updated !','Link not updated !','Link not updated !','Link not updated !','Link not updated !','Link not updated !','Link not updated !','Link not updated !','Link not updated !','Link not updated !','Link not updated !']
const='Link not updated !'
c=['x','x']
def change(li,n):
  temp[n]=li
def changesat(h,j):
  day=d()
  time=gettime()
  if j=='1' or j=='2' or j=='3' or j=='4' or j=='5' or j=='x' and (h=='1' or h=='0' or h=='x'):
    c[0]=h
    c[1]=j
    mess='Saturdays time table updated.'
    return(mess)
  else:
    mess='Saturdays time table not updated.'
    return(mess)

def toc():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a Holiday !')
  elif time>'17:30:00' and time<='23:59:59':
    temp[1]=const
    return('Todays classes are over !')
  elif day=='Fri' or ( c[1]=='5' and c[0]=='1' ):
    return('Today is an offline class !')
  else:
    return(temp[1])
def cg():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a holiday !')
  elif time>'17:30:00' and time<='23:59:59':
    temp[2]=const
    return('Todays classes are over !')
  elif day=='Thu' or ( c[1]=='4' and c[0]=='1'):
    return('Today is an offline class')
  else:
    return(temp[2])
def cn():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a Holiday !')
  elif time>'17:30:00' and time<='23:59:59':
    temp[3]=const
    return('Todays classes are over !')
  elif day=='Mon' or ( c[1]=='1' and c[0]=='1') :
    return('Today is an offline class')
  else:
    return(temp[3])
def mp():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a Holiday !')
  elif time>='17:30:00' and time<='23:59:59':
    temp[4]=const
    return('Todays classes are over !')
  elif day=='Fri' or ( c[1]=='5' and c[0]=='1'):
    return('Today no class for Microprocessor')
  else:
    return(temp[4])
def wt():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a Holiday !')
  elif time>'17:30:00' and time<='23:59:59':
    return('Todays classes are over !')
  elif day=='Mon' or day=='Tue':
    temp[5]='https://meet.google.com/qmz-msrn-aoh'
    return(temp[5])
  elif day=='Wed':
    return('Today is an offline class')
  elif day=='Thu' or day=='Fri' :
    temp[5]='https://meet.google.com/epe-wnhb-sra'
    return(temp[5])
  elif day=='Sat' and c[0]=='1' and (c[1]=='1' or c[1]=='2'):
    temp[5]='https://meet.google.com/qmz-msrn-aoh'
    return(temp[5])
  elif day=='Sat' and c[0]=='1' and c[1]=='3':
    return('Today is an offline class !')
  elif day=='Sat' and c[0]=='1' and (c[1]=='4' or c[1]=='5') :
    temp[5]='https://meet.google.com/epe-wnhb-sra'
    return(temp[5])
  else :
    temp[5]=const
    return('Link not updated !')
def mad():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a Holiday !')
  elif time>'17:30:00' and time<='23:59:59':
    temp[6]=const
    return('Todays classes are over !')
  elif day=='Tue' or ( c[1]=='2' and c[0]=='1'):
    return('Today is an offline class')
  else:
    return(temp[6])
def cnlab():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a Holiday !')
  elif time>'17:30:00' and time<='23:59:59':
    temp[8]=const
    return('Todays classes are over !')
  elif day=='Tue' or ( c[1] =='2' and c[0]=='1'):
    return(temp[8])
  else:
    temp[8]=const
    return('Today no classes scheduled for Computer networks LAB !')
def cglab():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a Holiday !')
  elif time>'17:30:00' and time<='23:59:59' :
    temp[7]=const
    return('Todays classes are over !')
  elif day== 'Mon' or (c[1]=='1' and c[0]=='1'):
    return(temp[7])
  else:
    temp[7]=const
    return('Today no classes scheduled for Computer graphics and multimedia LAB !')
def mplab():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a Holiday !')
  elif time>'17:30:00' and time<='23:59:59' :
    temp[9]=const
    return('Todays classes are over !')
  elif day=='Wed' or ( c[1]=='3' and c[0]=='1'):
    return(temp[9])
  else:
    temp[9]=const
    return('Today no class scheduled for Microprocessor LAB !')
def it():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a Holiday !')
  elif time>'17:30:00' and time<='23:59:59':
    temp[10]=const
    return('Todays classes are over !')
  elif day=='Thu' or ( c[1]=='4' and c[0]=='1'):
    return(temp[10])
  else:
    temp[10]=const
    return('Today no classes scheduled for Industrial training !')
def pt():
  day=d()
  time=gettime()
  if day=='Sun' or c[0]=='0':
    return('Today is a Holiday !')
  elif time>'17:30:00' and time<'23:59:59':
    temp[11]=const
    return('Todays classes are over !')
  elif day == 'Fri' or ( c[1]=='5' and c[0]=='1'):
    return(temp[11])
  else:
    temp[11]=const
    return('Today no classes scheduled for Placement and training !')
