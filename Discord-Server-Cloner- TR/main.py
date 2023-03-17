from os import system
mytitle = "discord.gg/turknsfw"
system("title "+mytitle)
import psutil
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████║░░░████╚═╗░██░░░░░░██░░░██║░░██╗░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██║░░░░██║░░░██║░░░██░░██░░░░░░░░░░██║░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██║░░░░██║░░░██║░░░░░██══╗░░░░██║░░██║░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██║░░░░██║░░░██║░░░██░░██╚═╗░░██║░░██╚═════╗░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██║░░░░░░████╔═╝░██░░░░░░██║░░██║░░████████║░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╚═╝░░░░░░░╚══╝░░░░░░░░░░░╚═╝░░╚═╝░░╚═══════╝░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}discord.gg/turknsfw{Style.RESET_ALL}
        """)
token = input(f'Tokeninizi girin:\n >')
guild_s = input('Kopyalancak sunucu id:\n >')
guild = input('Nereye kopyalansın:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


                                            ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                            ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                            ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                            ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                            ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                            ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    await client.close()


client.run(token, bot=False)
