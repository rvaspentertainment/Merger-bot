FROM python:3.10

WORKDIR /usr/src/mergebot

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y git wget curl pv jq ffmpeg neofetch mediainfo \
    && apt-get clean

# To enable rclone upload, uncomment the following line
# RUN curl https://rclone.org/install.sh | bash

COPY requirements.txt .

RUN python -m venv venv && venv/bin/pip install --no-cache-dir -r needs.txt

COPY . .

RUN chmod +x start.sh

CMD ["bash", "start.sh"]
