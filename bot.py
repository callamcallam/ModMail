import nextcord, os
from nextcord.ext import commands
from api.sqliteapi import SqliteAPI

version = "1.0.0"
db = SqliteAPI()

if not db.fetch_token():
    print("You need to set your token in the database.")
    token = input("Enter your token: ")
    if token: db.execute("UPDATE config SET token = ?;", (token,), commit=True)
    else: exit()

bot = commands.Bot(command_prefix=db.fetch_prefix(), intents=nextcord.Intents.all(), case_insensitive=False, help_command=None)

cmds = 0
events = 0
os.system(f"title ModMail - Commands [{cmds}] - Events [{events}]")
# time.sleep(2)

for folder in os.listdir("cogs"):
    for subfolder in os.listdir(f"cogs/{folder}"):
        for file in os.listdir(f"cogs/{folder}/{subfolder}"):
            if file.endswith(".py"):
                if folder == "commands":
                    cmds += 1
                    os.system(f"title ModMail - Commands [{cmds}] - Events [{events}]")
                elif folder == "events":
                    events += 1
                    os.system(f"title ModMail - Commands [{cmds}] - Events [{events}]")
                bot.load_extension(f"cogs.{folder}.{subfolder}.{file[:-3]}")
bot.run(db.fetch_token())
