#!/bin/bash

[ "$UID" -eq 0 ] || exec sudo "$0" "$@"

sudo apt install libjpeg-dev git python3 python3-pip -y
git clone https://github.com/featherbear/trello-epd

pushd trello-epd
pip3 install -r requirements.txt
cronString="@reboot python3 `pwd`/runWebhook.py"
cp .env.sample .env
popd

crontab -l > /dev/null
ret=$?
if [ $ret -ne 0 ]; then
        echo "$cronString" | crontab -
else
        (crontab -l ; echo "$cronString" ) | sort - | uniq - | crontab -
fi

echo "Now edit the .env file"