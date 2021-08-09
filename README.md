# About SELFDISCORD

selfdiscord is a set of methods for working with the discord api using your own account token (not a bot).
**selfboting is officially banned by T.O.S discord,** but nobody cares about that. Have you seen thousands of users with animated statuses? Welcome to the world of illegal botting

> **from developer:**    
in two entries and exits from any guild in a short period of time - your account will be disabled.

## How to start

Download `selfdiscord.py` and move it to your project folder, then just add the file to your script with `import selfdiscord`

## Fast start

```
import selfdiscord

client = selfdiscord.Client("mfa.token") # Ur discord token here

guilds = client.get_guilds() # Return list guilds
print(guilds) # Print dict
print(guilds[0]["name"]) # Return a guild name at first position (https://discord.com/developers/docs/resources/guild#guild-object)
```
Use https://discord.com/developers/docs/resources/ for get response structure

## Methods list

| Webhook | Description |
|-------------|---------|
|execute(text, nick, avatar_url, tts, embeds, allowed_mentions)| Send message
|delete() | Delete webhook
|modify(value, field) | https://discord.com/developers/docs/resources/webhook#modify-webhook
-------------------------
`Based on webhook token, client token not needed`

#

|   Client        |Description|
|-----------|-----------------------------|
|get_guilds()|Get guild list        |
|get_dms() | Get private channels (ur friends)
|get_user(uid) | Get information about user by id
|get_member(gid, uid) | Get information about guild member
|get_members(gid) | Get guild member list
|search_member(gid, nick, limit=50)| Search member by nick in guild
|join_guild(invite) | Join in guild by invite
|leave_guild(gid) | Leave from guild
|check_invite(invite) | Get information about invite and guild
|typing(cid) | Set fake typing effect in channel
|change_bio(text) | Set new bio text
|create_guild(name, template = default) | Create a new guild with template
|create_invite(cid, age, uses, temp) | Create invite in guild (default: unlimited)
|get_invites(gid) | Get all invites in guild
|create_webhook(cid, name) | Create webhook in channel
|get_webhooks(cid) | Get webhooks in channel
|delete_webhook(wid) | Delete weebhook with id
|get_widget(gid) | Get web widget information
|control_widget(gid, enabled, cid) | Edit widget information
|get_auditlog(gid, limit=50) | Get audit log from guild
|member_kick(gid, uid) | Kick member from guild
|member_ban(gid, uid, delete_message=1)|Ban member from guild with delete messages
|get_bans(gid)|Get banned members
|create_template(gid, name, description) | Create server template
|delete_template(gid, code) | Delete guild template
|get_templates(gid) | Get guild templates
|get_emojis(gid)| Get emojis list from guild
|get_stickers(gid) | Get stickers list from guild
|delete_guild(gid, mfa) | Delete guild with 2FA code
|change_accentcolor(color) | Change background color by HEX->Integer code
|create_role(gid, name) | Create role with name in guild
|get_roles(gid) | Get all roles
|edit_role(gid, rid, name, perms, hoist, ment) | Edit role (for permission use https://discord.com/developers/docs/topics/permissions)
|change_avatar(avatar) | Change ur avatar
|change_login(login, password) | Change login
|change_password(newpass, password) | Change password
|change_nick(gid, nick, user="@me" | Change user nick on guild
|get_messages(cid, limit=50) | Get messages in channel
|send_message(cid, text, tts=False)| Send message
|delete_message(cid, mid) | Delete message
|edit_message(cid, mid, text) | Edit message
|add_reaction(cid, mid, reaction) | Add reaction to message
|remove_reaction(cid, mid, reaction, user="@me") | Remove reaction from message by user
|start_thread(cid, mid, name, auto_archive_time=60) | Start thread
|get_activethreads(gid) | Get active threads list
|create_wopchannel(gid, name, type) | Create channel without category
|create_channel(gid, name, type, parent_id) | Create channel with category
|edit_channel(cid, name, type, topic, bitrate, user_limit, nsfw, slowmode, rate_limit_per_user, rtc_region) | Edit channel params
|delete_channel(cid) | Delete channel
-------------------------
`Based on client token`
