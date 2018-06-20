#!/bin/bash
## Егор красава
echo "Stickview v1 by egor21312"
function stickview2 {
clear
read -p "Введите id стикера: > " stick
if [[ $lim == y ]]; then
wget -q https://vk.com/images/stickers/$stick/$res.png && catimg -w 48 -r 2 $res.png && rm -rf $res.png
read -p "Нажмите Enter для повтора"
stickview2
elif [[ $lim == n ]]; then
wget -q https://vk.com/images/stickers/$stick/$res.png && catimg -r 2 $res.png && rm -rf $res.png
read -p "Нажмите Enter для повтора"
stickview2
fi
}
function stickview1 {
read -p "Введите id стикера: > " stick
read -p "Введите качество стикера (64/128/256/512) > " res
read -p "Ограничить ширину? (y/n) > " lim
if [[ $lim == y ]]; then
wget -q https://vk.com/images/stickers/$stick/$res.png && catimg -w 48 -r 2 $res.png && rm -rf $res.png
read -p "Нажмите Enter для повтора"
stickview2
elif [[ $lim == n ]]; then
wget -q https://vk.com/images/stickers/$stick/$res.png && catimg -r 2 $res.png && rm -rf $res.png
read -p "Нажмите Enter для повтора"
stickview2
fi
}
stickview1
fi
