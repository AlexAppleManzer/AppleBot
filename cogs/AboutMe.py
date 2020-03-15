import discord
from discord.ext import commands

class AboutMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aboutMe(self, ctx):
        """Gives a summary of who I am!"""
        await ctx.send(
            'Hello! I am a discord bot that is designed to do random stuff.\n' 
            'My creator is <@138747841068793856>.\n'
            'I am completely open source! My code is here https://github.com/AlexAppleManzer/AppleBot.\n'
            'Feel free to open up a PR or fork it for your own needs/desires.\n'
            'If you have any feature requests, submit an issue on github.'
        )

def setup(bot):
    bot.add_cog(AboutMe(bot))
