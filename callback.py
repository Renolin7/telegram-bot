import json
import requests
from links import *
from check import *
def subquery(ch_id,m_id):
  key=json.dumps({'inline_keyboard':[[{'text':'Theory of computation','callback_data':'toc'},{'text':'Computer graphics and multimedia','callback_data':'cg'}],[{'text':'Computer networks','callback_data':'cn'},{'text':'Microprocessor','callback_data':'mp'}],[{'text':'Web technology','callback_data':'wt'},{'text':'Mobile app development','callback_data':'mad'}],[{'text':'Go back','callback_data':'0'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':'-- /toc - Theory of computation\n-- /cg - Computer graphics and multimedia\n-- /cn - Computer networks\n-- /mp - Microprocessor\n-- /wt - Web technology\n-- /mad - Mobile App development\n\n (OR) Click the buttons below','reply_markup':key,'parse_mode':'HTML'}
  return params
def notifying(ch_id,m_id):
  key=json.dumps({'inline_keyboard':[[{'text':'Fees payment','url':'www.google.com'}],[{'text':'Go back','callback_data':'0'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'message_id':m_id,'text':'<b>NOTIFICATION\n\n</b>'+notification(),'reply_markup':key,'parse_mode':'HTML'}
  return params
def subject(ch_id,m_id,data):
  #key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
  #text=' '
  #key = None
  if data == 'toc':
    
    text='<b><u>Theory of computation\n\n</u></b>'+toc()
    if 'todays classes are over' in toc().lower() or 'holiday' in toc().lower() or 'link not updated' in toc().lower() or 'offline class' in toc().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':toc()}],[{'text':'Go back','callback_data':'4'}]]})
      
  elif data == 'cg':
     text='<b><u>Computer graphics and multimedia\n\n</u></b>'+cg()
     if 'todays classes are over' in cg().lower() or 'holiday' in cg().lower() or 'link not updated' in cg().lower() or 'offline class' in cg().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
     else:
       
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cg()}],[{'text':'Go back','callback_data':'4'}]]})
  elif data == 'cn':
    text='<b><u>Computer networks\n\n</u></b>'+cn()
    if 'todays classes are over' in cn().lower() or 'holiday' in cn().lower() or 'link not updated' in cn().lower() or 'offline class' in cn().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cn()}],[{'text':'Go back','callback_data':'4'}]]})
  elif data == 'mp':
    text='<b><u>Microprocessor\n\n</u></b>'+mp()
    if 'todays classes are over' in mp().lower() or 'holiday' in mp().lower() or 'link not updated' in mp().lower() or 'offline class' in mp().lower() or 'today no class' in mp().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cg()}],[{'text':'Go back','callback_data':'4'}]]})
  elif data == 'wt':
    text='<b><u>Web technology\n\n</u></b>'+wt()
    if 'todays classes are over' in wt().lower() or 'holiday' in wt().lower() or 'link not updated' in wt().lower() or 'offline class' in wt().lower() or 'today no class' in wt().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':wt()}],[{'text':'Go back','callback_data':'4'}]]})
  elif data == 'mad':
    text='<b><u>Mobile app development\n\n</u></b>'+mad()
    if 'todays classes are over' in mad().lower() or 'holiday' in mad().lower() or 'link not updated' in mad().lower() or 'offline class' in mad().lower() or 'today no class' in mad().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'4'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mad()}],[{'text':'Go back','callback_data':'4'}]]})
  elif data == 'it':
    text='<b><u>Industrial training\n\n</u></b>'+it()
    if 'todays classes are over' in it().lower() or 'holiday' in it().lower() or 'link not updated' in it().lower() or 'offline class' in it().lower() or 'today no class' in it().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'6'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':it()}],[{'text':'Go back','callback_data':'6'}]]})
  elif data == 'pt':
    text='<b><u>Placement and training\n\n</u></b>'+pt()
    if 'todays classes are over' in pt().lower() or 'holiday' in pt().lower() or 'link not updated' in pt().lower() or 'offline class' in pt().lower() or 'today no class' in pt().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'6'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':pt()}],[{'text':'Go back','callback_data':'6'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':text,'reply_markup':key,'parse_mode':'HTML'}
  return params
def labsub(ch_id,m_id,data):
  #text=' '
  #key = None
  if data == 'cgl':
     text='<b><u>Computer graphics and multimedia LAB\n\n</u></b>'+cglab()
     if 'todays classes are over' in cglab().lower() or 'holiday' in cglab().lower() or 'link not updated' in cglab().lower() or 'offline class' in cglab().lower() or 'today no class' in cglab().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'5'}]]})
     else:
       
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cglab()}],[{'text':'Go back','callback_data':'5'}]]})
  elif data == 'cnl':
     text='<b><u>Computer networks LAB\n\n</u></b>'+cnlab()
     if 'todays classes are over' in cnlab().lower() or 'holiday' in cnlab().lower() or 'link not updated' in cnlab().lower() or 'offline class' in cnlab().lower() or 'today no class' in cnlab().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'5'}]]})
     else:
       key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cnlab()}],[{'text':'Go back','callback_data':'5'}]]})
  elif data == 'mpl':
    text='<b><u>Microprocessor LAB\n\n</u></b>'+mplab()
    if 'todays classes are over' in mplab().lower() or 'holiday' in mplab().lower() or 'link not updated' in mplab().lower() or 'offline class' in mplab().lower() or 'today no class' in mplab().lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'5'}]]})
    else:
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mplab()}],[{'text':'Go back','callback_data':'5'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':text,'reply_markup':key,'parse_mode':'HTML'}
  return params
def labquery(ch_id,m_id):
  key=json.dumps({'inline_keyboard':[[{'text':'Computer graphics and multimedia LAB','callback_data':'cgl'}],[{'text':'Computer networks LAB','callback_data':'cnl'}],[{'text':'Microprocessor LAB','callback_data':'mpl'}],[{'text':'Go back','callback_data':'0'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':'LAB CLASSES \n\n-- /cgl - Computer graphics and multimedia LAB\n-- /cnl - Computer networks LAB\n-- /mpl - Microprocessor LAB\n\n (OR) Click the buttons below','reply_markup':key,'parse_mode':'HTML'}
  return params
  
def nextnow(ch_id,m_id,data):
  #key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'0'}]]})
  if data=='2':
    text=check()
    if 'no class scheduled' in text.lower() or 'holiday' in text.lower() or 'link not updated' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'0'}]]})
    elif 'theory of computation' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':toc()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'web technology' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':wt()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'mobile app development' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mad()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'computer graphics and multimedia lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cglab()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'computer networks lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cnlab()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'microprocessor lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mplab()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'computer graphics' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cg()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'computer networks' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cn()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'microprocessor' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mp()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'industrial training' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':it()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'placement and training' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':pt()}],[{'text':'Go back','callback_data':'0'}]]})
  elif data=='3':
    text=nextcl()
    if 'no classes scheduled' in text.lower() or 'holiday' in text.lower() or 'link not updated' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Go back','callback_data':'0'}]]})
    elif 'theory of computation' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':toc()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'web technology' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':wt()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'mobile app development' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mad()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'computer graphics and multimedia lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cglab()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'computer networks lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cnlab()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'microprocessor lab' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mplab()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'computer graphics' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cg()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'computer networks' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':cn()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'microprocessor' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':mp()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'industrial training' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':it()}],[{'text':'Go back','callback_data':'0'}]]})
    elif 'placement and training' in text.lower():
      key=json.dumps({'inline_keyboard':[[{'text':'Join class','url':pt()}],[{'text':'Go back','callback_data':'0'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':text,'reply_markup':key,'parse_mode':'HTML'}
  return params
def noti(ch_id,m_id):
  key=json.dumps({'inline_keyboard':[[{'text': 'Notification','callback_data':'1'}],[{'text': 'Current class','callback_data': '2'},{'text': 'Next class','callback_data':'3'}],[{'text': 'Theory classes','callback_data': '4'}],[{'text': 'Lab classes','callback_data':'5'}],[{'text': 'Seminar classes','callback_data': '6'}],[{'text': 'Source code','url':'www.google.com'}]]})
 
  tex='Hey! My name is Syntax_error. I am an online class link management bot, here to help you get the class links and time table! PM me on @niloner_bot\n\nFor further queries use the buttons below.\n\n\nThis bot was created by @Renolin'
  params={'chat_id':ch_id,'message_id':m_id,'text':tex,'reply_markup':key,'parse_mode':'HTML'}
  return params
def seminar(ch_id,m_id):
  key=json.dumps({'inline_keyboard':[[{'text':'Industrial training','callback_data':'it'}],[{'text':'Placement and training','callback_data':'pt'}],[{'text':'Go back','callback_data':'0'}]]})
  params={'chat_id':ch_id,'message_id':m_id,'text':'\n\n-- /it - Industrial training\n-- /pt - Placement and training\n\n(OR) Click the buttons below.','reply_markup':key,'parse_mode':'HTML'}
  return params
