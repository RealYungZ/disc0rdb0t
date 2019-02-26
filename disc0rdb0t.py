from discord import Client
from random import randint
from time import sleep


TOKEN = '***YOUR TOKEN HERE***'

client = Client()
zboy = '<:swag:549054020170547210>' #represents a custom emoji

GREETINGS = [
                "Hello there " + zboy,
                "Yooooooooooooo wut's up?",
                "How YOU doin? " + zboy,
                "Yooo wanna play some fort? JK im a bot (pun intended)" + zboy,
                "Howdy partner " + zboy,
                "CaN i GeT sOmE zBoYs In ThE cHaT fOr"
            ]
COMMANDS = [
                "!hello",
                "!randclip",
                "!twitch",
                "!twitter",
                "!youtube",
                "!fortstats",
                "!code"
           ]


def get_rand_clip():
    with open("clips.txt", "r") as f:
        lines = f.readlines()
        return lines[randint(0, len(lines) - 1)]


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = GREETINGS[randint(0, len(GREETINGS) - 1)] + ' {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!randclip'):
        clip = 'https://www.twitch.tv/realyungz/clip/' + get_rand_clip()
        await client.send_message(message.channel, clip)
    elif message.content.startswith('!twitch'):
        msg = 'https://www.twitch.tv/realyungz'
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!twitter'):
        msg = 'https://www.twitter.com/realyungz'
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!youtube'):
        msg = 'https://www.youtube.com/channel/UCJ4gj3c0hJwIgQfAmSTIjug'
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!fortstats'):
        msg = 'https://fortnitetracker.com/profile/pc/Twitch%20RealYungZ'
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!code'):
        msg = 'I am currently running on my master\'s raspberry pi ' + zboy + \
              '\n\nVersion: 1.1 - added commands: !randclip !twitch !twitter !youtube !fortstats !code '\
              '\nhttps://github.com/RealYungZ/disc0rdb0t'
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!commands'):
        msg = ""
        for c in COMMANDS:
            msg += c + " "
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)


client.run(TOKEN)
