from discord.ext import commands


class RandomStuff:
    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/randomstuff/images/'

    @commands.command(pass_context=True)
    async def furry(self, context):
        await self.bot.send_file(context.message.channel, '{}furry.png'.format(self.base))

def setup(bot):
    n = RandomStuff(bot)
    bot.add_cog(n)
