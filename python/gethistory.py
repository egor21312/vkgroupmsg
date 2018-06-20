import vk
import time
import math
session = vk.Session(access_token='ENTER YOUR TOKEN')
vk_api = vk.API(session)
c = 10
oldmsg = 0
pid = int(input("Введите id беседы > "))
peer = 2000000000 + pid
while c > 0:
	history = vk_api.messages.getHistory(count=1, peer_id=peer, v='5.80')
	id = history['items'][0]['from_id']
	if id > 0:
		user = vk_api.users.get(user_ids=id, v='5.80')
		first_name = user[0]['first_name']
		last_name = user[0]['last_name']
		text = history['items'][0]['text']
		msg = first_name + ' ' + last_name + ' ' + '(' + '@' + 'id' + str(id) + ')' + ': ' + str(text)
		if msg == oldmsg:
 			time.sleep(0.8)
		else:
			print(msg)
			oldmsg = msg
			time.sleep(0.8)
	else:
		gid = math.fabs(id)
		modulegid = int(gid)
		group = vk_api.groups.getById(group_ids=gid, v='5.80')
		name = group[0]['name']
		text = history['items'][0]['text']
		msg = name + ' ' + '(' + '@' + 'club' + str(modulegid) + ')' + ': ' + str(text)
		if msg == oldmsg:
			time.sleep(0.8)
		else:
			print(msg)
			oldmsg = msg
			time.sleep(0.8)
