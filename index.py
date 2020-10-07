from os import environ
import json
from Time import *
import requests
import datetime
from check import *
from links import *
import random
ani=['CAACAgUAAxkBAAPbX3cWYLOlxfEYYsWb8IKFTVwpuFoAApIBAALoFSciftxS2UkI1IobBA','CAACAgUAAxkBAAPLX3cQ_75Ct09Mtpz1cf1mUSh4py8AAosCAAJ5XhciU-n9Mxtky70bBA','CAACAgUAAxkBAAPKX3cQjjCL_B1y_DmIwme-3tXxqBAAAmoCAAJ5XhciTfXzxzK074kbBA','CAACAgEAAxkBAAPJX3cP5hHEvaiLovbwA_NrGkDK9DYAAhgBAAI4DoIRW2biLrLrCn0bBA','CAACAgUAAxkBAAIGC192tgcAAYx9rNj9oluH0EaiUfTQmAACggEAAugVJyLWkLvD3xo6OBsE','CAACAgIAAxkBAAIGDV92tiyxNHjGdmL2nRMR7iPTVZBNAAJHAwACtXHaBjV7c9kAAYsdpBsE','CAACAgEAAxkBAAIGD192tknJG2aYoMyIp6z8TB9MQxRAAAJICgACv4yQBHUk1z4LX5nUGwQ','CAACAgIAAxkBAAIGEV92tmiajEMIuUrSpAoUGB1WSeF9AAKBAAPBnGAM6PbLODBd3jcbBA','CAACAgIAAxkBAAIGE192tpHLj8uDtrdFr7vN2WflsDVlAAJ-AAOWn4wOcYMRnixctuUbBA','CAACAgIAAxkBAAIGFV92trKOjqUs6r8ewX1nZE26yoLUAAJhAAMK_MIFpvt8LfVaOa4bBA','CAACAgEAAxkBAAIGF192ttsoH2v0oHXdUqdggeDYVtT2AAJgCgACv4yQBLW3hUMCnp-QGwQ','CAACAgIAAxkBAAIGGV92tzS4WyxEdXzlDcKtabFy7xZjAAJUAwACtXHaBkKqUvDfaej1GwQ','CAACAgIAAxkBAAIGG192t2ywB6YRujxfhpj2yg2vBuErAAJnAAOvxlEayZCJx70BigIbBA','CAACAgIAAxkBAAIGHV92uMwDmIaA45NiLAhx1_oucQWnAAIeAANZu_wlsg0_9KjFvagbBA','CAACAgIAAxkBAAIGH192uSsdPrTFfm0ShdtUQnJ3_RvRAAIvAAP7g6klITd39eao4jYbBA','CAACAgIAAxkBAAIGIV92uUFn1Du_4zewI0HmD7M-vW1eAAI4AAP7g6klOy_Bp3Iw890bBA','CAACAgIAAxkBAAIGI192uaHX5J51qhtdMXrtxBXEXYRpAAKtAwAC8n6CDGSNpbcqwW--GwQ']
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
    def send_notify(self,chat_id,m_id,text):
         key={'inline_keyboard':[[{'text': 'Fees payment','url':'https://annamalaiuniversity.ac.in/studport/epayment_rgl_tfee.php?mode=oNln' }]]}
         keyys=json.dumps(key)
         params = {'chat_id': chat_id, 'text': text,'parse_mode':'HTML','reply_markup':keyys}
         method = 'sendMessage'
         resp = requests.post(self.api_url + method, params)
         return resp
    def send_greet(text):
        params = {'chat_id': '-327423546','text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        
        return resp
    def send_message(self, chat_id,m_id,text):
        t_day=d()
        u=random.randint(0,16)
        met='sendchataction'
        para={'chat_id':chat_id ,'action' : 'typing'}
        respons=requests.post(self.api_url + met, para)
        if 'holiday' in text.lower() and (c[0]=='0' or t_day=='Sun' ):  
                par={'chat_id': chat_id, 'animation': ani[u], 'parse_mode': 'HTML'}
                meth='sendAnimation'
                res = requests.post(self.api_url + meth, par)
        else:
            par={'chat_id': chat_id, 'animation': 'CAACAgUAAxkBAAPfX3cXDnmVYxOa7XLvKNPBMZ0t4xEAAgcAA1cSKR0oHhl84pXJtRsE', 'parse_mode': 'HTML'}
            meth='sendAnimation'
            res = requests.post(self.api_url + meth, par)
        params = {'chat_id': chat_id,'reply_to_message_id' : m_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        
        return resp
    def send_pinned(self, chat_id,m_id,text):
        met='sendchataction'
        para={'chat_id':chat_id ,'action' : 'typing'}
        respons=requests.post(self.api_url + met, para)
        par={'chat_id': chat_id, 'animation': 'CAACAgUAAxkBAAPfX3cXDnmVYxOa7XLvKNPBMZ0t4xEAAgcAA1cSKR0oHhl84pXJtRsE', 'parse_mode': 'HTML'}
        meth='sendAnimation'
        res = requests.post(self.api_url + meth, par)
        params = {'chat_id': chat_id,'reply_to_message_id': m_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        
        return resp
    def send_photo(self, chat_id,m_id, text) :
        met='sendchataction'
        para={'chat_id':chat_id ,'action' : 'upload_photo'}
        respons=requests.post(self.api_url + met, para)
        params = {'chat_id': chat_id,'reply_to_message_id':m_id, 'photo': text, 'parse_mode': 'HTML'}
        method = 'sendPhoto'
        resp = requests.post(self.api_url + method, params)
        return resp
    def send_button(self,chat_id,m_id,text):
         key={'keyboard':[[{'text':'/tt'},{'text':'/ftt'},{'text':'/now'},{'text':'/next'}],[{'text':'/toc'},{'text':'/cg'},{'text':'/cn'}],
      [{'text':'/mp'},{'text':'/wt'},{'text':'/mad'}],[{'text':'/cgl'},{'text':'/cnl'},{'text':'/mpl'}],[{'text':'/it'},{'text':'/pt'}],[{'text':'/help'},{/notify}]]}
         keyys=json.dumps(key)
         params = {'chat_id': chat_id, 'text': text,'parse_mode':'HTML','reply_markup':keyys}
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

def main():
    new_offset = 0
    print('Launching the bot...')

    while True:
        
        all_updates=niloner_bot.get_updates(new_offset)
       
        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                
                m_id = current_update['message']['message_id']
                if 'text' not in current_update['message'] :
                    first_chat_text='New member'
                    #new_offset = first_update_id + 1
                else:
                  first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"
                





                if 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['first_name']
                    niloner_bot.send_message(first_chat_id,m_id,'Welcome '+'<b><i>'+first_chat_name+'</i></b>'+'\nHope this group will help you.\nType /list for list of commands\n\nI am a bot created by @Renolin\n'+sp)
                    new_offset = first_update_id + 1
                elif 'left_chat_participant' in current_update['message'] :
                   temp_name=current_update['message']['from']['first_name']
                   name=current_update['message']['left_chat_participant']['first_name']
                   rid=current_update['message']['left_chat_participant']['id']
                   pid=current_update['message']['from']['id']
                   if rid==pid :
                         niloner_bot.send_message(first_chat_id,m_id,'<b><i>'+ name+'</i></b>'+' left the group chat.')
                   else :
                       niloner_bot.send_message(first_chat_id,m_id,'<b><i>'+name+'</i></b>'+' was removed by '+'<b><i>'+temp_name+'</i></b>')
                   new_offset = first_update_id + 1
                elif 'pinned_message' in current_update['message']:
                        niloner_bot.send_pinned(first_chat_id,m_id,first_chat_name+' pinned a message\n')
                        new_offset = first_update_id + 1

                elif first_chat_text == 'Hi' or first_chat_text == 'hi':
                  niloner_bot.send_pinned(first_chat_id,m_id, 'Hi '  +first_chat_name)
                  new_offset = first_update_id + 1
                
                elif first_chat_text == '/notify' :
                  niloner_bot.send_notify(first_chat_id,m_id, '<b>NOTIFICATION</b>\n\n'+'<i>'+notification()+'</i>')
                  new_offset = first_update_id + 1
                 
                elif first_chat_text == '/start':
                  niloner_bot.send_message(first_chat_id,m_id, 'Hi '  +'<b><i>' +first_chat_name+'</i></b>'+'\n Type /help for list of commands\n\n\n\nThis bot was created by @Renolin')
                  new_offset = first_update_id + 1
                
                else :
                  flag=1
                  if first_chat_text == '/tt':
                    flag=0
                    niloner_bot.send_message(first_chat_id,m_id, table())
                    new_offset = first_update_id + 1
                  if first_chat_text == '/help':
                      flag=0
                      niloner_bot.send_button(first_chat_id,m_id, '<b>List of Commands</b>\n\n-- /tt - Time table\n\n-- /now - Current period\n\n-- /next - Next period\n\n-- /toc - Theory of computation\n\n-- /cg- Computer graphics and multimedia\n\n-- /cn - Computer networks\n\n-- /mp - Microprocessor\n\n-- /wt - Web technology\n\n-- /mad - Mobile App\n\n-- /cgl - Computer graphics and multimedia LAB\n\n-- /cnl - Computer networks LAB\n\n-- /mpl - Microprocessor LAB\n\n-- /it - Industrial training\n\n-- /pt - Placement and training\n\n')
                      new_offset = first_update_id + 1
                  if first_chat_text == '/now':
                        flag=0
                        niloner_bot.send_message(first_chat_id,m_id, check())
                        new_offset = first_update_id + 1
                  if first_chat_text == '/next':
                          flag=0
                          niloner_bot.send_message(first_chat_id,m_id, nextcl())
                          new_offset = first_update_id + 1
                  if first_chat_text == '/toc':
                            flag=0
                            niloner_bot.send_message(first_chat_id,m_id, '<b><u>Theory of computation</u></b>\n\n'+toc())
                            new_offset = first_update_id + 1
                                              
                  if first_chat_id in ID and '/ch_toc'== first_chat_text[ :7]:
                              flag=0
                              h=first_chat_text[7:]
                              change(h,1)
                              niloner_bot.send_message(first_chat_id,m_id, '<b>Theory of computation</b> link updated \n\n'+temp[1])
                              new_offset = first_update_id + 1
                  if first_chat_text == '/cg':
                                flag=0
                                niloner_bot.send_message(first_chat_id,m_id, '<b><u>Computer graphics and multimedia</u></b>\n\n'+cg())
                                new_offset = first_update_id + 1
                  if first_chat_id in ID and '/ch_cg'== first_chat_text[ :6]:
                                  flag=0
                                  h=first_chat_text[6:]
                                  change(h,2)
                                  niloner_bot.send_message(first_chat_id,m_id, '<b>Computer graphics and multimedia</b> link updated \n\n'+temp[2])
                                  new_offset = first_update_id + 1
                                                  
                  if first_chat_text == '/cn':
                                    flag=0
                                    niloner_bot.send_message(first_chat_id,m_id, '<b><u>Computer networks</u></b>\n\n'+cn())
                                    new_offset = first_update_id + 1
                  if first_chat_id in ID and '/ch_cn'== first_chat_text[:6]:
                                      flag=0
                                      h=first_chat_text[6:]
                                      change(h,3)
                                      niloner_bot.send_message(first_chat_id,m_id, '<b>Computer networks</b> link updated\n\n'+temp[3])
                                      new_offset = first_update_id + 1
                  if first_chat_text == '/mad':
                                        flag=0
                                        niloner_bot.send_message(first_chat_id,m_id,'<b><u>Mobile app development</u></b>\n\n'+mad())
                                        new_offset = first_update_id + 1
                  if first_chat_id in ID and '/ch_mad'==first_chat_text[ :7]:
                                          flag=0
                                          h=first_chat_text[7:]
                                          change(h,6)
                                          niloner_bot.send_message(first_chat_id,m_id, '<b>Mobile app development</b> link updated\n'+temp[6])
                                          new_offset = first_update_id + 1
                  if first_chat_text == '/wt':
                                            flag=0
                                            niloner_bot.send_message(first_chat_id,m_id,'<b><u>Web technology</u></b>\n\n'+wt())
                                            new_offset = first_update_id + 1
                  if first_chat_text == '/mp':
                                              flag=0
                                              niloner_bot.send_message(first_chat_id,m_id,'<b><u>Microprocessor</u></b>\n\n'+mp())
                                              new_offset = first_update_id + 1
                                                              
                  if first_chat_id in ID and '/ch_sat'== first_chat_text[:7]:
                                                flag=0
                                                h=first_chat_text[7: :9]
                                                j=first_chat_text[8:]
                                                l=changesat(h,j)
                                                niloner_bot.send_message(first_chat_id,m_id, l)
                                                new_offset = first_update_id + 1
                  if first_chat_id in ID and '/ch_mp'== first_chat_text[:6]:
                    flag=0
                    h=first_chat_text[6:]
                    change(h,4)
                    niloner_bot.send_message(first_chat_id,m_id, '<b>Microprocessor</b> link updated\n\n'+temp[4])
                    new_offset = first_update_id + 1
                  if first_chat_text == '/cgl':
                      flag=0
                      niloner_bot.send_message(first_chat_id,m_id,'<b><u>Computer graphics LAB</u></b>\n\n'+cglab())
                      new_offset = first_update_id + 1
                  if first_chat_id in ID and '/ch_lcg'== first_chat_text[ :7]:
                        flag=0
                        h=first_chat_text[7:]
                        change(h,7)
                        niloner_bot.send_message(first_chat_id,m_id, '<b>Computer graphics and multimedia LAB</b> link updated\n\n'+temp[7])
                        new_offset = first_update_id + 1
                  if first_chat_text == '/cnl':
                          flag=0
                          niloner_bot.send_message(first_chat_id,m_id,'<b><u>Computer networks LAB</u></b>\n\n'+cnlab())
                          new_offset = first_update_id + 1
                                          
                  if first_chat_id in ID and '/ch_lcn' == first_chat_text[ :7]:
                            flag=0
                            h=first_chat_text[7:]
                            change(h,8)
                            niloner_bot.send_message(first_chat_id,m_id, '<b>Computer networks LAB</b> link updated\n\n'+temp[8])
                            new_offset = first_update_id + 1
                                            
                  if first_chat_text == '/mpl':
                              flag=0
                              niloner_bot.send_message(first_chat_id,m_id,'<b><u>Microprocessor LAB</u></b>\n\n'+mplab())
                              new_offset = first_update_id + 1
                                              
                  if first_chat_id in ID and '/ch_lmp' == first_chat_text[ :7]:
                                flag=0
                                h=first_chat_text[7:]
                                change(h,9)
                                niloner_bot.send_message(first_chat_id,m_id, '<b>Microprocessor LAB</b> link updated\n\n'+temp[9])
                                new_offset = first_update_id + 1
                                                
                  if first_chat_text == '/it':
                                  flag=0
                                  niloner_bot.send_message(first_chat_id,m_id,'<b><u>Industrial training</u></b>\n\n'+it())
                                  new_offset = first_update_id + 1
                                                  
                  if first_chat_id in ID and '/ch_it' == first_chat_text[ :6]:
                                    flag=0
                                    h=first_chat_text[6: ]
                                    change( h,10 )
                                    niloner_bot.send_message(first_chat_id,m_id, '<b>Industrial training </b>link updated\n\n'+temp[10])
                                    new_offset = first_update_id + 1
                                                    
                  if first_chat_text == '/pt':
                                      flag=0
                                      niloner_bot.send_message(first_chat_id,m_id,'<b><u>Placement and training</u></b>\n\n'+pt())
                                      new_offset = first_update_id + 1
                                                      
                  if first_chat_id in ID and '/ch_pt' == first_chat_text[: 6]:
                                        flag=0
                                        h=first_chat_text[6:]
                                        change(h,11)
                                        niloner_bot.send_message(first_chat_id,m_id, '<b>Placement and training </b>link updated\n'+temp[11])
                                        new_offset = first_update_id + 1
                  if first_chat_text == '/ftt' :
                                flag=0  
                                niloner_bot.send_photo(first_chat_id,m_id, 'AgACAgUAAxkBAAIF_V92plbUjrx94tYKodyeNQmdWPjbAAKaqjEbo6GxV-x6we6XqVjA-3rra3QAAwEAAwIAA3gAA5lYBAABGwQ')
                                new_offset = first_update_id + 1
                  if '/ch_notify' in first_chat_text and first_chat_id in ID :
                              flag=0
                              h=first_chat_text[10: ]
                              change_notify(h)
                              niloner_bot.send_message(first_chat_id,m_id, 'Notification updated\n'+notification())
                              new_offset = first_update_id + 1
                  if flag==1 :
                                          niloner_bot.send_message(first_chat_id,m_id, 'My brain does not have a response for that.')
                                          new_offset = first_update_id + 1
                  
                
                


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
