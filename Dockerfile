FROM resin/rpi-raspbian
RUN apt update
RUN apt-get install python3-pip python3-dev build-essential libyaml-dev
RUN pip3 install unicornhat kubernetes
ADD unicorn.py /unicorn.py
ENTRYPOINT ["/unicorn.py"]
