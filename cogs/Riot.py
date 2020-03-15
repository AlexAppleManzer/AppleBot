import discord
from discord.ext import commands

import common.RiotApi as RiotApi

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def isTilted(self, ctx, summonerName):
        summoner = await RiotApi.getSummoner(summonerName)
        summonerId = summoner['id']
        summonerAccountId = summoner['accountId']
        match_history = await RiotApi.getSummonerHistory(summonerAccountId)
        loss_streak = 0

        for match in match_history['matches'][:5]:
            match_info = await RiotApi.getMatch(match['gameId'])
            participant_id = 0

            # find participant Identity number
            for identity in match_info['participantIdentities']:
                if summonerId == identity['player']['summonerId']:
                    participant_id = identity['participantId']
            
            # assumes team is 100 if identity is 1-5 else assume team 200  
            team_100 = True if participant_id <= 5 else False
            print(participant_id)
            team_100_win = match_info['teams'][0]['win'] == "Win"

            if team_100 == team_100_win:
                break

            loss_streak = loss_streak + 1
        
        if loss_streak > 0:
            await ctx.send(f'Ouch! {summonerName} is tilted! :slight_frown:\n:fire: {summonerName} is on a {loss_streak} game loss streak! :fire:')
        else:
            await ctx.send(f'Nice! :thumbsup:\n{summonerName} is not tilted :white_check_mark:')

def setup(bot):
    bot.add_cog(Test(bot))
