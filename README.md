# selfdiscord
selfdiscord - seltbot api for discord, working at client token

# Fast-start:
```
import selfdiscord

client = selfdiscord.Client("mfa.token") # Ur discord token here

guilds = client.get_guilds() # Return list guilds
print(guilds) # Print dict
print(guilds[0]["name"]) # Return a guild name at first position (https://discord.com/developers/docs/resources/guild#guild-object)
```

# Docs:
|   Client        |Description|
|-----------|-----------------------------|
|get_guilds|Get guild list        |
|Dashes          |`-- is en-dash, --- is em-dash`
