# This is the main file for coding the UNTITLED Discord Bot

import os

import interactions
from dotenv import load_dotenv

# Load env file with Discord key. You won't have this file as it contains sensitive information, but it doesn't need to be changed.
load_dotenv()                                           
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))

client = interactions.Client(token=TOKEN)

# Trigger an event when client has successfully connected to Discord
@client.event
async def on_ready():
    print(f'Client has connected to Discord!')

# This is a pre-written command from IntoToPython for testing purposes only
@client.command(
    name="getstats",
    description="Get your player stats",
    scope=GUILD,
)
async def get_stats(ctx: interactions.CommandContext):
    await ctx.send("Here are your player stats!")

client.start()