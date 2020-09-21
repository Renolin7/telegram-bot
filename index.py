from os import environ
import requests
import datetime
from check import *
from links import *
#from test import *
#wel= 'hey'

class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)


    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = environ['token']
niloner_bot = BotHandler(token)
ID= [750862502,817947468]
#def change(x,n,ar):
  #ar[n]=x
  
  
#def getbbb(n):
  #return(bbb[1])
#bbb=['  ','   ','   ']
def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=niloner_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                
                                
                if 'text' not in current_update['message'] :
                    first_chat_text='New member'
                    #new_offset = first_update_id + 1
                else:
                  first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == 'Hi' or first_chat_text == 'hi':
                  niloner_bot.send_message(first_chat_id, 'Hi '  + first_chat_name)
                  new_offset = first_update_id + 1
                  break
                #elif 'Hi' in first_chat_text:
                  #wel='Mm'
                  #Renolin_bot.send_message(first_chat_id, wel+ first_chat_name)
                  #new_offset = first_update_id + 1
                 
                
                  
              #  if first_chat_text=='/test':
                  #Renolin_bot.send_message(first_chat_id, 'test link is \n'+getbbb(1))
                  #new_offset = first_update_id + 1
                #if first_chat_text == 'New member':
                  #  Renolin_bot.send_message(first_chat_id, 'Hi '  + first_chat_name+'\nHow can help you.')
                   # new_offset = first_update_id + 1
                if first_chat_text == '/start':
                  niloner_bot.send_message(first_chat_id, 'Hi '  + first_chat_name +'\n Type /list for list of notes')
                  new_offset = first_update_id + 1
                    
                else :
                  flag=1
                  if first_chat_text == '/tt':
                    flag=0
                    niloner_bot.send_message(first_chat_id, table())
                    new_offset = first_update_id + 1
                  if first_chat_text == '/list':
                      flag=0
                      niloner_bot.send_message(first_chat_id, 'List of Commands\n\n/tt - Time table\n\n/now - Current period\n\n/next - Next period\n\n/toc - Theory of computation\n\n/cg- Computer graphics\n\n/cn - Computer networks\n\n/mp - Microprocessor\n\n/wt - Web technology\n\n/mad - Mobile App\n\n/cgl - Computer graphics and multimedia LAB\n\n/cnl - Computer networks LAB\n\n/mpl - Microprocessor LAB\n\n/it - Industrial training\n\n/pt - Placement and training\n\n')
                      new_offset = first_update_id + 1
                  if first_chat_text == '/now':
                        flag=0
                        niloner_bot.send_message(first_chat_id, check())
                        new_offset = first_update_id + 1
                  if first_chat_text == '/next':
                          flag=0
                          niloner_bot.send_message(first_chat_id, nextcl())
                          new_offset = first_update_id + 1
                  if first_chat_text == '/toc':
                            flag=0
                            niloner_bot.send_message(first_chat_id, 'Theory of computation\n\n'+toc())
                            new_offset = first_update_id + 1
                                              
                  if first_chat_id in ID and '/ch_toc'== first_chat_text[ :7]:
                              flag=0
                              h=first_chat_text[7:]
                              change(h,1)
                              niloner_bot.send_message(first_chat_id, 'Theory of computation link updated \n\n'+temp[1])
                              new_offset = first_update_id + 1
                  if first_chat_text == '/cg':
                                flag=0
                                niloner_bot.send_message(first_chat_id, 'Computer graphics and multimedia\n\n'+cg())
                                new_offset = first_update_id + 1
                  if first_chat_id in ID and '/ch_cg'== first_chat_text[ :6]:
                                  flag=0
                                  h=first_chat_text[6:]
                                  change(h,2)
                                  niloner_bot.send_message(first_chat_id, 'Computer graphics and multimedia link updated \n\n'+temp[2])
                                  new_offset = first_update_id + 1
                                                  
                  if first_chat_text == '/cn':
                                    flag=0
                                    niloner_bot.send_message(first_chat_id, 'Computer networks\n\n'+cn())
                                    new_offset = first_update_id + 1
                  if first_chat_id in ID and '/ch_cn'== first_chat_text[:6]:
                                      flag=0
                                      h=first_chat_text[6:]
                                      change(h,3)
                                      niloner_bot.send_message(first_chat_id, 'Computer networks link updated\n\n'+temp[3])
                                      new_offset = first_update_id + 1
                  if first_chat_text == '/mad':
                                        flag=0
                                        niloner_bot.send_message(first_chat_id,'Mobile app development\n\n'+mad())
                                        new_offset = first_update_id + 1
                  if first_chat_id in ID and '/ch_mad'==first_chat_text[ :7]:
                                          flag=0
                                          h=first_chat_text[7:]
                                          change(h,6)
                                          niloner_bot.send_message(first_chat_id, 'Mobile app development link updated\n'+temp[6])
                                          new_offset = first_update_id + 1
                  if first_chat_text == '/wt':
                                            flag=0
                                            niloner_bot.send_message(first_chat_id,'Web technology\n\n'+wt())
                                            new_offset = first_update_id + 1
                  if first_chat_text == '/mp':
                                              flag=0
                                              niloner_bot.send_message(first_chat_id,'Microprocessor\n\n'+mp())
                                              new_offset = first_update_id + 1
                                                              
                  if first_chat_id in ID and '/ch_sat'== first_chat_text[:7]:
                                                flag=0
                                                h=first_chat_text[7: :9]
                                                j=first_chat_text[8:]
                                                l=changesat(h,j)
                                                niloner_bot.send_message(first_chat_id, l)
                                                new_offset = first_update_id + 1
                  if first_chat_id in ID and '/ch_mp'== first_chat_text[:6]:
                    flag=0
                    h=first_chat_text[6:]
                    change(h,4)
                    niloner_bot.send_message(first_chat_id, 'Microprocessor link updated\n\n'+temp[4])
                    new_offset = first_update_id + 1
                  if first_chat_text == '/cgl':
                      flag=0
                      niloner_bot.send_message(first_chat_id,'Computer graphics LAB\n\n'+cglab())
                      new_offset = first_update_id + 1
                  if first_chat_id in ID and '/ch_lcg'== first_chat_text[ :7]:
                        flag=0
                        h=first_chat_text[7:]
                        change(h,7)
                        niloner_bot.send_message(first_chat_id, 'Computer graphics and multimedia LAB link updated\n\n'+temp[7])
                        new_offset = first_update_id + 1
                  if first_chat_text == '/cnl':
                          flag=0
                          niloner_bot.send_message(first_chat_id,'Computer networks LAB\n\n'+cnlab())
                          new_offset = first_update_id + 1
                                          
                  if first_chat_id in ID and '/ch_lcn' == first_chat_text[ :7]:
                            flag=0
                            h=first_chat_text[7:]
                            change(h,8)
                            niloner_bot.send_message(first_chat_id, 'Computer networks LAB link updated\n\n'+temp[8])
                            new_offset = first_update_id + 1
                                            
                  if first_chat_text == '/mpl':
                              flag=0
                              niloner_bot.send_message(first_chat_id,'Microprocessor LAB\n\n'+mplab())
                              new_offset = first_update_id + 1
                                              
                  if first_chat_id in ID and '/ch_lmp' == first_chat_text[ :7]:
                                flag=0
                                h=first_chat_text[7:]
                                change(h,9)
                                niloner_bot.send_message(first_chat_id, 'Microprocessor LAB link updated\n\n'+temp[9])
                                new_offset = first_update_id + 1
                                                
                  if first_chat_text == '/it':
                                  flag=0
                                  niloner_bot.send_message(first_chat_id,'Industrial training\n\n'+it())
                                  new_offset = first_update_id + 1
                                                  
                  if first_chat_id in ID and '/ch_it' == first_chat_text[ :6]:
                                    flag=0
                                    h=first_chat_text[6: ]
                                    change( h,10 )
                                    niloner_bot.send_message(first_chat_id, 'Industrial training link updated\n\n'+temp[10])
                                    new_offset = first_update_id + 1
                                                    
                  if first_chat_text == '/pt':
                                      flag=0
                                      niloner_bot.send_message(first_chat_id,'Placement and training\n\n'+pt())
                                      new_offset = first_update_id + 1
                                                      
                  if first_chat_id in ID and '/ch_pt' == first_chat_text[: 6]:
                                        flag=0
                                        h=first_chat_text[6:]
                                        change(h,11)
                                        niloner_bot.send_message(first_chat_id, 'Placement and training link updated\n'+temp[11])
                                        new_offset = first_update_id + 1
                                                        
                  if flag==1 :
                                          niloner_bot.send_message(first_chat_id, 'My brain does not have a response for that.')
                                          new_offset = first_update_id + 1
                  
                
                


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()