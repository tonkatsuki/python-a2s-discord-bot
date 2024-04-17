Quick and dirty python script that leverage discord's bot functionality to query a2s servers and find (if available) old post in a channel and edit or makes a new one

```
TOKEN = $'TOKENHERE'
CHANNEL_ID = $CHANNELIDHERE

servers = {
    ('$IPHERE', 27015): {"fqdn": "ttt.test.com", "Game": "Garry's Mod"}, 
    ('$IP2HERE', 27015): {"fqdn": "bhop.test.com", "Game": "Counter-Strike 2"},  

}
```

Edit these vars in the script.


For discord bot setup go to discord.com/developers/ and make a new application. Get the client secret from the OAuth2 tab and use that for the token.
Join the discord bot by making a Oauth2 URL Generator and select 'bot' for the scope.
Once joined, I scoped the bot to only have access to the channel used for the channel_ID (you can get this via right clicking a channel and clicking copy channel id)

So far the permissions it just needs are
  View Channel
  Send Messages
  Embed Links
  Manage Messages
  Read Message History
