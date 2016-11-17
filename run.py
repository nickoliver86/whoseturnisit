from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

def main():
    bot = Bot()
    bot.run()

@listen_to('whoseturnisit')
def help(message):
    message.reply('Yes, I can!')

if __name__ == "__main__":
    main()
