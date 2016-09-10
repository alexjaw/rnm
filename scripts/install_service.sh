#!/usr/bin/env bash
# ref: http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/
script_name=rnm.py
script=/home/pi/rnm/rnm/$script_name
service_name=rnm.service
service=/home/pi/rnm/scripts/$service_name

echo install service $service_name...

echo copy $service to /lib/systemd/system/ ...
sudo cp $service /lib/systemd/system/

echo configure $service_name...
sudo chmod 644 /lib/systemd/system/$service_name
chmod +x $script
sudo systemctl daemon-reload
sudo systemctl enable $service_name
sudo systemctl start $service_name

echo finished