FROM resin/rpi-raspbian
RUN apt update
RUN apt-get install python3-pip python3-dev build-essential
RUN pip3 install unicornhat
ADD demo.py /demo.py
ENTRYPOINT ["/demo.py"]
