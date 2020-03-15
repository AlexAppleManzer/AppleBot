import os

import discord
from discord.ext import commands

import datetime
import asyncio
import logging
from pathlib import Path
from dotenv import load_dotenv

from common.AppSettings import AppSettings

client = discord.Client()

async def run():
    load_dotenv()
    settings = AppSettings()
    bot = Bot(config=settings)

    try:
        await bot.start(settings['DISCORD_TOKEN'])
    except KeyboardInterrupt:
        await bot.logout()

class Bot(commands.Bot):
    def __init__(self, config):
        super().__init__(
            command_prefix=config['command-prefix'],
            description=config['description']
        )
        self.start_time = None
        self.app_info = None

        self.loop.create_task(self.track_start())
        self.loop.create_task(self.load_all_extensions())

    async def track_start(self):
        await self.wait_until_ready()
        self.start_time = datetime.datetime.utcnow()

    async def load_all_extensions(self):
        await self.wait_until_ready()
        await asyncio.sleep(1)
        cogs = [x.stem for x in Path('cogs').glob('*.py')]
        for extension in cogs:
            try:
                self.load_extension(f'cogs.{extension}')
                print(f'loaded {extension}')
            except Exception as e:
                error = f'{extension}\n {type(e).__name__} : {e}'
                print(f'failed to load extension {error}')
            print('-' * 10)

    async def on_ready(self):
        print('-' * 10)
        self.app_info = await self.application_info()
        print(f'Logged in as: {self.user.name}\n'
              f'Using discord.py version: {discord.__version__}\n'
              f'Owner: {self.app_info.owner}')
        print('-' * 10)

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
