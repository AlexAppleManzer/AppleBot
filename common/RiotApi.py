import aiohttp
import logging

logger = logging.getLogger(__name__)

from common.AppSettings import AppSettings

settings = AppSettings()
RIOT_API_KEY = settings['RIOT_API_KEY']
base_urls = settings['riot-api']['base-urls']

headers = {'X-Riot-Token': RIOT_API_KEY}

async def getSummoner(summonerName):
    return await fetch(f"{base_urls['na']}/lol/summoner/v4/summoners/by-name/{summonerName}")

async def getSummonerHistory(accountId):
    return await fetch(f"{base_urls['na']}/lol/match/v4/matchlists/by-account/{accountId}")

async def getMatch(matchId):
    return await fetch(f"{base_urls['na']}/lol/match/v4/matches/{matchId}")
    

async def fetch(url, headers=headers, params=None, expectedResponse=200):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as resp:
            if resp.status == expectedResponse:
                return await resp.json()
            else:
                logger.error(f'Riot Api returned a {resp.status} from endpoint {url} with details {await resp.text()}')
                raise Exception('Error Calling Riot Api')
            
