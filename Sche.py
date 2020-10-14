import schedule
from index import *
from check import *
#def bedtime():
  #print('yes')
schedule.every().day.at("08:57").do(niloner_bot.send_message,-440030144,nextcl())
schedule.every().day.at("09:57").do(niloner_bot.send_message,-440030144,nextcl())
schedule.every().day.at("10:57").do(niloner_bot.send_message,-440030144,nextcl())
schedule.every().day.at("11:27").do(niloner_bot.send_message,-440030144,nextcl())
schedule.every().day.at("12:27").do(niloner_bot.send_message,-440030144,nextcl())
schedule.every().day.at("13:27").do(niloner_bot.send_message,-440030144,nextcl())
schedule.every().day.at("14:27").do(niloner_bot.send_message,-440030144,nextcl())
schedule.every().day.at("15:27").do(niloner_bot.send_message,-440030144,nextcl())
schedule.every().day.at("16:27").do(niloner_bot.send_message,-440030144,nextcl())
schedule.every().day.at("17:30").do(niloner_bot.send_message,-440030144, 'Todays classes are over')
while True: 
   schedule.run_pending()