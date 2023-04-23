import disnake
from disnake.ext import commands

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    
    @commands.slash_command()
    async def embed(self,interecation, amount:int):
        embed = disnake.Embed(title="Clear", description = f"Deleted {amount} messages", color=0x00ff00)
        embed.add_field(name = "Field 1", value = "Value 1", inline = False)
        embed.add_field(name = "Field 2", value = "Value 2", inline = False)
        embed.add_field(name = "Field 3", value = "Value 3", inline = False)
        embed.set_footer(text = "Embed footer")
        embed.set_author(name = "Embed Author")
        embed.set_thumbnail(url = self.bot.user.avatar.url)
        await interecation.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Embed(bot))