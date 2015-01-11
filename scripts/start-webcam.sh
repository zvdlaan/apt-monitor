#! /bin/bash

cd /home/zvdlaan/mjpg-streamer

./mjpg_streamer -i "./input_uvc.so -d /dev/video0 -n -f 15 -r 1080x600" -o "./output_http.so -n -p 8087 -w ./www"
