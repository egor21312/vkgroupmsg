import vk
session = vk.Session(access_token='360c93fb76c48e6b29f35ff8a7551c3a971e1d87eb65c0131d2c8a12e75a4eec9792032d7b2305a611e37')
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
