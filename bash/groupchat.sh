#!/bin/bash
## Сообщения от имени пабликов
## vk.com/vk.toaster крутой
token=$(cat token.conf)
res=64
read -p "id беседы: > " chat
function quickchat {
trap 'clear; read -p "Введите id стикера: > " stick; wget -q https://vk.com/images/stickers/$stick/$res.png && catimg -w 48 -r 2 $res.png && rm -rf $res.png; curl -s "https://api.vk.com/method/messages.send?chat_id=$chat&sticker_id=$stick&access_token=$token&v=5.80" >  /dev/null; quickchat' 3
trap 'clear; read -p "Адрес вложения: > " attach; curl -s "https://api.vk.com/method/messages.send?chat_id=$chat&attachment=$attach&access_token=$token&v=5.80" >  /dev/null; quickchat' SIGTSTP
read -p "Введите сообщение: > " msg
msg=$(echo $msg | sed 's/ /+/g' | sed 's/~/%0A/g')
curl -s "https://api.vk.com/method/messages.send?chat_id=$chat&message=$msg&attachment=&access_token=$token&v=5.80" >  /dev/null
quickchat
}
quickchat
fi
