from datetime import datetime 

import pytz 

  

UTC = pytz.utc 

  



def gettime():
  timeZ_Kl = pytz.timezone('Asia/Kolkata')
  dt_Kl = datetime.now(timeZ_Kl)
  utc_Kl = dt_Kl.astimezone(UTC)
  d = dt_Kl.strftime('%a')
  return(dt_Kl.strftime('%H:%M:%S')) 
def d():
  timeZ_Kl = pytz.timezone('Asia/Kolkata')
  dt_Kl = datetime.now(timeZ_Kl)
  utc_Kl = dt_Kl.astimezone(UTC)
  d = dt_Kl.strftime('%a')
  return(d) 
  
print(d())
  
print(gettime())
  