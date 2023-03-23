import discord
import datetime
from redbot.core import commands, tasks

class DayReminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.send_day_message.start()

    def cog_unload(self):
        self.send_day_message.cancel()

    @tasks.loop(hours=24)
    async def send_day_message(self):
        today = datetime.datetime.today()
        day_of_week = today.strftime('%A')
        message = ''
        if day_of_week == 'Monday':
            message = 'Happy Monday everyone!'
        elif day_of_week == 'Tuesday':
            message = 'Happy Taco Tuesday!'
        elif day_of_week == 'Wednesday':
            message = 'Happy Hump Day!'
        elif day_of_week == 'Thursday':
            message = 'Happy Friday Eve!'
        elif day_of_week == 'Friday':
            message = 'Happy Friday everyone!'
        elif day_of_week == 'Saturday':
            message = 'Happy Saturday! Enjoy your weekend!'
        elif day_of_week == 'Sunday':
            message = 'Happy Sunday! Relax and enjoy the day!'
        channel = self.bot.get_channel(1088298679066173612)
        await channel.send(message)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user}!')

def setup(bot):
    bot.add_cog(DayReminder(bot))
