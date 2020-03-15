import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 135634124340854784:
            await message.add_reaction('😬')

def setup(bot):
    bot.add_cog(Test(bot))