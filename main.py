import discord
import a2s
from discord.ext import commands
import asyncio

TOKEN = '$TOKENHERE'
CHANNEL_ID = $CHANNELIDHERE

servers = {
    ('$IPHERE', 27015): {"fqdn": "ttt.test.com", "Game": "Garry's Mod"}, 
    ('$IP2HERE', 27015): {"fqdn": "bhop.test.com", "Game": "Counter-Strike 2"},  

}

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

async def query_servers():
    embed = discord.Embed(title="Server Status", description="Current server status for each game server.", color=discord.Color.blue())
    embed.set_thumbnail(url="$THUMBNAIL IF WANTED")
    for address, info in servers.items():
        try:
            server_info = a2s.info(address)
            player_count = len(a2s.players(address))
            field_value = f"**Game:** {info['Game']}\n**Map:** {server_info.map_name}\n**Player Count:** {player_count}/{server_info.max_players}"
            embed.add_field(name=info['fqdn'], value=field_value, inline=False)
        except Exception as e:
            embed.add_field(name=info['fqdn'], value=f"Error querying server: {e}", inline=False)
    return embed

async def update_server_status():
    while True:
        channel = bot.get_channel(CHANNEL_ID)
        if channel is None:
            print(f"Channel with ID {CHANNEL_ID} not found.")
            return

        last_bot_message = None
        async for message in channel.history(limit=100):
            if message.author == bot.user and message.embeds:
                last_bot_message = message
                break

        status_embed = await query_servers()

        if last_bot_message:
            await last_bot_message.edit(embed=status_embed)
            print("Message edited.")
        else:
            await channel.send(embed=status_embed)
            print("Message sent.")

        await asyncio.sleep(300)  # Wait for 5 minutes

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    bot.loop.create_task(update_server_status())

bot.run(TOKEN)
