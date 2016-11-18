from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import pdb

@listen_to('whosezturnisit')
def help(message):

    name_dict = {

        "Matthew Billie": "matthew.billie",
        "Taylor Bird": "tayor",
        "Kevin Ellis": "kevin.ellis",
        "Erland Kelley": "erland",
        "Harrison Lavin": "harrison.lavin",
        "Bryce Lively": "brycelively",
        "Samir Mehta": "samir.mehta",
        "Daniel Neumann": "daniel.neumann.ctr",
        "Brian Palladino": "brian.palladino",
        "Allen Tuggle": "allen.tuggle",
        "Allison Zentmayer": "allisonzent"
        
    }

    with open("current_name.txt") as current_name:
        name = current_name.readline().strip("\n")
        current_name.close()

    with open("mylist.txt") as names:
        rd = names.readline()
        while rd != name:
            rd = names.readline().strip("\n")
        rd = names.readline().strip("\n")
        names.close()

    with open("current_name.txt", "w") as current_name:
        current_name.write(rd)
        current_name.close()

    print (rd)
    username = name_dict[rd]
    message.send("@{0}, your time to shine!".format(username))

def main():
    print("Running Main")
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
