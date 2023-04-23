import disnake
from disnake.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.slash_command()
    async def clear(self, intereaction, amount:int):
        embet = disnake.Embed(title = "Clear", description=f"Delted {amount} message", color = 0x00ff00)
        embet.set_thumbnail(url = self.bot.user.avatar.url)
        await intereaction.response.send_message(embed = embet,)
        await intereaction.channel.purge(limit = amount +1)



def setup(bot):
    bot.add_cog(Clear(bot))