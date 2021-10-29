# stream-cloud

demo : [downloader_star_bot](https://t.me/downloader_star_bot)


# Run :

* Docker :

    > install docker , docker-compose
    
    > set Environment or edit Config/__init__.py
    
    `docker-compose up`

* Heroku :

    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/musa-42/stream-cloud)

    `git clone https://github.com/musa-42/stream-cloud`
    
    > edit Config/__init__.py
    
    `heroku create` or `heroku git:remote -a appname`
    
    `git push heroku master`

* Cli :

    > install python3.8+
    
    `git clone https://github.com/musa-42/stream-cloud`
    
    > set Environment or edit Config/__init__.py
    
    `pip install -r requirements.txt`
    
    run web : 
        `gunicorn main:main --workers 4 --threads 4 --bind 0.0.0.0:$PORT --timeout 86400 --worker-class aiohttp.GunicornWebWorker`
        
    run bot :
        `python -m bot`
        
    run web and bot :
        `./start`


Environment :
|env|description|Example|
|-|-|-|
|api_id|api_id Telegram to develop a robot to receive my.telegram.org|12345|
|api_hash|api_hash Telegram to develop a robot to receive my.telegram.org|21ab7cb0a453b5e60016dc7bbeb701cb|
|channel_files_chat_id|Telegram channel chat ID for storing and managing files|-10012345466|
|channel_username|Telegram channel username for support|Userlandapp|
|token|Telegram robot token for launch|0000000:AAFFMMgYoL9Vjb5KUU0bXxVReUI81xuU|
|domain|application domain|https://newdlstar.herokuapp.com|



Management guide:

    If a file is deleted from the storage channel, the link will expire
    If a file is replayed in the storage channel and a message is sent, that message will be sent to the sender of the file
    If a file is edited in the storage channel and replaced by another file, the link will download the new file
    If a user is blocked from the support channel, he can no longer use the robot

# Donate:

btc:
    `bc1qzw6l9a43f26epyme0yskz2zqzd7fppjnumnfv8`

trc20:
    `TJRA6PZoNZP5shdeJVLvGfEqWR7X4kXfuW`

bep20, erc20:
    `0x8B988133D96150a3324D0BE8124A65fB6A09612C`
    
