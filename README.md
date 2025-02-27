![](botpfp.jpg)

# Bot

## About
Bot is a discourse bot that responds automatically to pings. It automates access to the discourse and was taken inspiration from discobot, a bot native to discourse. It is made in python selenium, using chromedriver. <br>
There is a bot currently being hosted on replit for the X-Camp Discourse.
<br><br>
*Note: Bot has only been tested on the X-Camp Discourse. Therefore, it is not guaranteed that it will work in other discourses.*
## Current Features
### Access:
The bot has the ability to post in topics and chat in DMs or chats. It also can post in PMs as long as you invite the bot into the PM. <br>
Bot can also only reply to topics in categories that the bot is in. It cannot reply in private categories that the bot doesn't have access to, for example.
### Commands:
`@bot display help` or `@bot help`: Makes the bot output the various commands it can do and a short explanation of them.
<br><br>
`@bot ai [PROMPT HERE]`: This will generate an AI response based on the prompt. Currently, I am using Gemini-2.0-Flash Experimental. 
<br><br>
`@bot say [SOMETHING]`: The bot will parrot whatever text is after the word `say`.
<br><br>
`@bot xkcd`: This command will generate a random XKCD comic that is not a blacklisted one.
<br><br>
`@bot xkcd last` or `@bot xkcd latest`: Outputs the most recent [xkcd](https://xkcd.com) comic. 
<br><br>
`@bot xkcd blacklist`: Outputs the current list of blacklisted XKCD comics. If it's in a topic, it will additionally output the reasons a XKCD may be blacklisted.
<br><br>
`@bot xkcd comic [ID HERE]`: This will give you the xkcd comic with the ID given along with some info on the comic.
### Other
**NO COMMAND:** If no recognizable command is detected, then the bot will output one of the following at random:
* Hi!
* Hello!
* I want to take over the world!
* How dare you ping me
<br>

**XKCD BLACKLIST:** There is a XKCD blacklist in place to block NSFW XKCD content. This blacklist is still growing, meaning you may still see a NSFW XKCD.
<br><br>

**FAIL SAFE:** Thanks to [ethandacat](https://github.com/ethandacat) for this idea in the first place; This feature basically allows the code to run itself again if it runs into an error. 
<br><br>

**REPLYING:** The bot "replies" to your post. If the bot replies to no user, then it is replying to the message directly above it. Otherwise, there will be a "reply" dialog on the top of the message that shows who the bot is replying to. It works in both chat and topics!

## Anticipated Features:
The following features may or may not come out in the future. Stay tuned!
* A command which the bot will give you all the information of an account on the forum given the username.
* More documentation (here)

## Credits:
Special thanks to [ethandacat](https://github.com/ethandacat) for helping me a lot, including the original idea and various snippets of code!
<br>
Development: Me and [ethandacat](https://github.com/ethandacat)
<br>
Logo: Generated by Imagen 2
<br>
Assistance and help: ChatGPT, DeepSeek, Gemini, and [ethandacat](https://github.com/ethandacat).
<br><br>
Also go check out [ethandacat](https://github.com/ethandacat)'s [catscobot](https://github.com/ethandacat/catscobott)!

## Changelog:
```
February 26, 2025
Version 1.4.0: Added (unfinished) XKCD comic command, and reply functions for chat. Edits to the display help command, including also adding XKCD help to do the same thing as display help.

February 21, 2025
Version 1.3.2: Fixed a typo

February 21, 2025
Version 1.3.1: MORE STUFF LIKE A LOT. I FORGOT TO KEEP TRACK OF WHAT I DID.

February 21, 2025
Version 1.3.0: Added huge optimizations for chats/direct messaging.

February 21, 2025
Version 1.2.4: More blacklisted XKCDs

February 18, 2025
Version 1.2.3: Blacklisted XKCD 812

February 16, 2025
Version 1.2.2: Fixed the bug where `1m` is shows up as the username. Created command `XKCD BLACKLIST`

February 4, 2025
Version 1.2.1: Updated AI context

February 4, 2025
Version 1.2.0: Added FailSafe, `XKCD LAST`, updated AI context. 

February 4, 2025
Version 1.1.3: Updated AI to Gemini-2.0-Flash Experimental

February 3, 2025
Version 1.1.2: Added buffer for errors

February 3, 2025
Version 1.1.1: Optimized XKCD by A LOT, added blacklist.

February 3, 2025
Version 1.1.0: Added user recognition

December 29, 2024
Version 1.0.0: Stable version with the AI, SAY, and XKCD commands, with support for the chats.

--- (not recorded)

Version 0.5.0: Added XKCD command and bug fixes

Version 0.4.1: More error prevention.

Version 0.4.0: Added AI

Version 0.3.1: Minor change to the display help.

Version 0.3.0: Added display help and updated all outputs.

Version 0.2.0: Added first command!

Version 0.1.1: Minor patch.

Version 0.1.0: First version. 

SEPTEMBER 19, 2024
```
