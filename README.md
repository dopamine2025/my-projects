import discord
def run_discord_bot():
    masterkey = "MTA5MDk4MjQyOTE4MDgyMTU2OQ.Gj__U4.WLhNvwvo6DpvhG1ZPqiFyZ8-69vYWba0UQVjBY"
    client = discord.Client()
    @client.event
    async def on_ready():
        print(f'{client.user} maybe working but not sure')
    @client.event
    async def on_message(message):
            author = str(message.author)
            content = str(message.content)
            userid = str(message.author.id)
            messageid = str(message.id)
            time = str(message.created_at)
            link = str(message.jump_url)
            channel = str(message.channel)
            row = [userid, author, content, time, messageid, link, channel]
    @client.event
    async def on_message_edit(before, after):
        row = [before, after]
    client.run(masterkey)
