import json

from flask import Flask 

from threading import Thread
import discord
import asyncio


app = Flask(__name__)
app.debug = False

class MyClient(discord.Client):
    def hello_world(self):
        return 'Username: {0.name}\nID: {0.id}'.format(self.user)

    async def on_ready(self):
        print('Connected!')
        print('Username: {0.name}\nID: {0.id}'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('!editme'):
            msg = await message.channel.send('10')
            await asyncio.sleep(3.0)
            await msg.edit(content='40')

    async def on_message_edit(self, before, after):
        fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
        await before.channel.send(fmt.format(before, after))

client = MyClient()

@app.route('/')
def hello_world():
    return '<a href="/ping">a</div>'

@app.route('/ping')
def ping():
    return client.hello_world()

def startFlask():
    app.run()

def startDiscord():
    with open("auth.json") as auth:
        client.run(json.load(auth)['TOKEN'])


if __name__ == "__main__":
    flask_thread    = Thread(target=startFlask)
    flask_thread.start()
    print('started flask')

    discord_thread = Thread(target=startDiscord)
    discord_thread.start()
    print('started discord')