from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

lucifer_GIF = "https://telegra.ph/file/278f5efdd347220c8a9c9.png"

lucifer_IMG = "https://telegra.ph/file/278f5efdd347220c8a9c9.png"

SOURCE_STRING = """
I'm built in python3, using the python-telegram-bot library, and am fully opensource - you can find what makes me tick [here](https://t.me/kavinduaj)
"""

buttons_about = [[InlineKeyboardButton(text="➕ Add me in your Group! ➕", url="t.me/mrjokerv3_bot?startgroup=true")]]
buttons_about += [[InlineKeyboardButton(text="❔ Commands", callback_data="help_back")]]
buttons_about += [[InlineKeyboardButton(text="📢 Support", url="https://t.me/cyberwordk"), InlineKeyboardButton(text="🔔 Updates", url="https://t.me/snewst")]]
buttons_about += [[InlineKeyboardButton(text="❣ About", url="https://visi.tk/kavinduaj"), InlineKeyboardButton(text="❣ Creator", url="https://t.me/kavinduaj")]]
buttons_about += [[InlineKeyboardButton(text="❔ How to use? ❔", url="t.me/mrjokerv3_bot?start=howto")]]


buttons_start = [[InlineKeyboardButton(text="➕ Add me in your Group! ➕", url="http://t.me/mrjokerv3_bot?startgroup=true")]]
buttons_start += [[InlineKeyboardButton(text="📢 Support", url="https://t.me/cyberwordk"), InlineKeyboardButton(text="❤ About me", url="t.me/mrjokerv3_bot?start=about")]]
buttons_start += [[InlineKeyboardButton(text="❔ Commands", callback_data="help_back")]]

HELP = """
Hey there! My name is *{}*.
I'm a modular group management bot with a few fun extras! Have a look at the following for an idea of some of \
the things I can help you with.
*Main* commands available:
 - /start: start the bot
 - /help: PM's you this message.
 - /help <module name>: PM's you info about that module.
 - /settings:
  - in PM: will send you your settings for all supported modules.
  - in a group: will redirect you to pm, with all that chat's settings.
{}
And the following:
"""

ABOUT = """
I am *{}* the *Demon King*!\n
I'm built in *python3*, using the *python-telegram-bot library*.\n
I'm a  Group Manager bot and will manage your group like *Rose,HarkukaAya,Sophie*,etc does but with more features!\n
Any issue or need more help?
Join our group [Lucifer Official Support](https://t.me/cyberwordk)!\n
Follow [Mr.Joker](https://t.me/snewst) if you want to keep up with the bot news, bot updates and bot downtime.\n
You can find the list of available commands with /help.\n
If you're enjoying using me, and/or would like to help me survive in the wild, hit /donate to help fund/upgrade my VPS!\n
*Want to add me to your group*? [Click here!](t.me/mrjokerv3_bot?startgroup=true)
"""

DONATE_STRING = """
Heya, glad to hear you want to donate!\n
Need a lot of work for [my creator](tg://user?id=1131653685) to take me to my place now, and \
every donation helps and motivates him to make me better.\n
All donated money will be given to a better VPS to host me, and or some food. \
He is just an ordinary person, so it will really help him!\n
If you really are interested in donating, please contact [my creator](tg://user?id=1131653685) , Thank you ❤
"""

#Inspired from @SaitamaRobot
KNIGHTS = """
Mr.Joker has bot access levels we call as *"Knights of Hell"*
\n*Vampires* - Devs who can access the bots server and can execute, edit, modify bot code. Can also manage other Knights
\n*Angel* - Only one Angel exist in this world that is my master my owner. 
Owner has complete bot access, including bot adminship in chats Mr.Joker is at.
\n*Dragons* - Have super user access coz they can fly, can gban, manage knights lower than them and are admins in Mr.Joker.
\n*Wizards* - Have access go globally ban users across Mr.Joker.
\n*Ghosts* - Cannot be seen through naked eye,So cannot be banned, muted flood kicked but can be manually banned by admins.
\n*Disclaimer*: The Knights in Mr.Joker are there for troubleshooting, support, banning potential scammers.
Report abuse or ask us more on these at [CYBERWORDK](https://t.me/cyberwordk).
"""
#Inspired from @SaitamaRobot
HOWTO = """
New to *Mr.Joker Bot*?
Here is all you should know!\n
Enable welcome security, soft or strong.
`/welcomemute strong`
Note: Permanent mutes a user until they press a button within `160seconds`, most bots will get stuck here and get auto-kicked before they can waste your time.
Soft restricts them to text only for 24hours after joining.\n
Protect accidental contact leakage
`/lock contact`\n
Stop letting users add bots (Ideally, disable the "add users" permission in group settings)
`/lock bots`\n
Private group? concerned of invite links?
`/disable invitelink`\n
Lock forwarding stuff into the group
`/disable forward`\n
Private group? Avoid users kicking themselves by mistake
`/disable kickme`\n
Users/Spammers flooding non stop? (Adjust the number to your needs)
`/setflood 7`\n
Don't want some Lucifer commands enabled in group?
`/listcmds` and then use `/disable <namehere>`
Note: if this conflicts with any other bot in group then use `/disable@mrjokerv3_bot` to send that message only to `Mr.Joker`.\n
Want to auto warn users when they say specific stuff?
See warns > `/addwarn command help`\n
Don't like some words to be spoken in group? Blacklist them using
`/addblacklist word1`
`word2`
`"entire sentence here"`\n
Note: You can use `"quotes for"` if there is a sentence and not a word.\n
Don't want to explain to each newbie? setup rules using 
`/setrules`
 Rules here\n
 Don't want our awesome welcome message? Use a custom one using
`/setwelcome Hi`, welcome to my group 
Note: This command has more stuff you can use, see `/welcomehelp` first.\n
Have multiple groups to handle? Setup Federations
Read help for this, this has a bit of a learning curve.\n
Enable reporting so that your users can report troublemakers to admins.
`/reports on`
Note: Send in group to enable group reports and send in Mr.Joker's pm so that he will report any enabled group to your pm.\n
Want to track which of your admins did what? who banned who? who joined?
Setup a log channel, see help for instructions.\n\n
Lastly, most of these would apply to almost any Lucifer like bot, please do spread the word around for basic chat control and protect yourself from spammers/scammers and troublemakers.\n
Visit us at @cyberwordk anytime in case of queries, suggestions or in need of help setting up Lucifer for your chat.\n
"""
