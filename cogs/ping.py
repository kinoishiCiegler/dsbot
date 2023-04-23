from disnake.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.slash_command()
    async def ping(interaction):
        await interaction.response.send_message("PONG!")

def setup(bot):
    bot.add_cog(Ping(bot))        