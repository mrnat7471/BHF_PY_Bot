import discord
from discord.ext import commands
import asyncio
import datetime
import ffmpeg

class joinCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='urlplay')
    async def join(self, ctx, message):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        await ctx.message.delete()
        vc.play(discord.FFmpegPCMAudio(message))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 1.0
def setup(bot):
    bot.add_cog(joinCog(bot)) 