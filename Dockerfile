FROM resin/rpi-raspbian
RUN sudo apt-get install python3-pip python3-dev
RUN sudo pip3 install unicornhat
ADD demo.py /demo.py
ENTRYPOINT ["/demo.py"]
