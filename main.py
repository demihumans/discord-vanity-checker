import discord

token=''

def i():
    client = discord.Client()

    @client.event
    async def on_ready():
        print('██   ██ ████████ ██   ██ \n ██ ██     ██    ██  ██  \n  ███      ██    █████   \n ██ ██     ██    ██  ██  \n██   ██    ██    ██   ██ \n\nEnter *exit to quit.')
        while True:
            x = input("Enter Vanity: ").strip()
            
            if x.lower() == '*exit':
                await client.close()
                break
            
            try:
                invite = await client.fetch_invite(f"https://discord.gg/{x}")
                print(f"[x] {x} is taken")
            except discord.NotFound:
                print(f"[✓] {x} is available")
            except Exception:
                pass

    client.run(token)

i()
