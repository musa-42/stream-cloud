FROM python

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt


ENV PORT = 8000
EXPOSE 8000

CMD sh start.sh
