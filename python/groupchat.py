import vk
session = vk.Session(access_token='ENTER YOUR ONE HERE')
vk_api = vk.API(session)
b = 1
chatid = input("Введите ID беседы > ")
def stick():
	stk=input("Введите id стикера > ")
	vk_api.messages.send(sticker_id=stk, chat_id=chatid, v='5.80')
while b > 0:
	msg=" "
	msg=input("Введите сообщение > ")
	if msg == '!stick':
		stick()
	else:
		vk_api.messages.send(message=msg, chat_id=chatid, v='5.80')
