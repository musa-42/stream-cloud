FROM python

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN pip3 install -U https://github.com/LonamiWebs/Telethon/archive/v1.24.zip

ENV PORT = 8000
EXPOSE 8000

CMD sh start.sh
