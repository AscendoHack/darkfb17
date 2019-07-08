#!/bin/bash

clear
figlet Ascendo v.2 | lolcat
sleep 2
echo "•••••••••••••••••••••••••••••••••••••••••
#Code By Ascendo Team
#Contact Ascendohack@gmail.com                 
•••••••••••••••••••••••••••••••••••••••••" | lolcat
echo "Tools Dark Fb V1.7                " | lolcat
echo "Jangan Salah Gunakan Tools Ini    " | lolcat
echo "Jika Anda Salah Gunakan " | lolcat
echo "Saya Tidak Akan Tanggung Jawab" | lolcat
echo "•••••••••••••••••••••••••••••••••••••••••" | lolcat

read -p "Masuk Ke Dark Fb V1.7 y/n : " masuk | lolcat

if [ $nomor =y ] || [ $nomor =ya ]
then
clear
toilet -f pagga " Dark Fb V1.7 " -F gay
sleep 4
pkg install python2
pip2 install requests
pip2 install mechanize
pkg install git
git clone https://github.com/perijoko14/Dark-fb
cd dark
sleep 3
python2 dark.py
fi