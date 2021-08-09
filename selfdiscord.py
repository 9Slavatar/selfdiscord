import requests
from random import randint

# 4Discord stuff: pls remove the ur fucking T.O.S about selfbotings

# Headers for client requests
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "authorization": None,
    "origin": "https://discord.com",
    "content-type": "application/json",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9002 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"}

# Webhooks
class Webhook:
    def __init__(self, _url: str):
        web = requests.get(_url)
        if web.status_code != 200:
            return
        self.url = _url
        self.about = web.json()


    def execute(self, content: str, username: str, avatar_url: str = None, tts: bool = False, embeds: dict = {}, allowed_mentions: dict = {}):
        return requests.post(self.url, data={
            "content": content,
            "username": username,
            "avatar_url": avatar_url,
            "tts": tts,
            "embeds": embeds,
            "allowed_mentions": allowed_mentions
        }).status_code == 204

    def delete(self):
        return requests.delete(self.url).status_code == 204

    def modify(self, value: str, field: int = 0):
        fields = ["name", "avatar", "channel_id"]
        return requests.patch(self.url, data = '{"' +fields[field]+ '": "' +value+ '"}').status_code == 200

# Clients
class Client:
    def __init__(self, _token):
        self.token = _token

        self.headers = headers
        self.headers["authorization"] = self.token

    def get_guilds(self):
        return requests.get("https://discord.com/api/v9/users/@me/guilds", headers={"authorization": self.token}).json()

    def get_dms(self):
        return requests.get("https://discord.com/api/v9/users/@me/channels", headers={"authorization": self.token}).json()

    def get_user(self, user: int = "@me"):
        return requests.get(f"https://discord.com/api/v9/users/{user}", headers={"authorization": self.token}).json()

    def get_member(self, guild: int, member: int):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers={"authorization": self.token}).json()

    def get_members(self, guild: int):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/members", headers={"authorization": self.token}).json()

    def search_member(self, guild: int, member: str, limit: int = 50):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/members/search?query={member}&limit={limit}", headers={"authorization": self.token}).json()

    def join_guild(self, invite: str):
        return requests.post(f"https://discord.com/api/v9/invites/{invite}", headers={"authorization": self.token}).json()

    def leave_guild(self, guild: int):
        return requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}", headers=self.headers, data='{"lurking": false}').status_code == 204

    def check_invite(self, invite: str):
        return requests.get(f"https://discord.com/api/v9/invites/{invite}?with_counts=true&with_expiration=true", headers={"authorization": self.token}).json()

    def typing(self, channel: int):
        return requests.post(f"https://discord.com/api/v9/channels/{channel}/typing",
        headers=self.headers).json()

    def change_bio(self, text: str):
        return requests.patch("https://discord.com/api/v9/users/@me",
        headers=self.headers,
        data='{"bio": "' +text+ '"}').status_code == 200

    def create_guild(self, name: str, template: str = "2TffvPucqHkN"):
        return requests.post(f"https://discord.com/api/v9/guilds", headers=self.headers, 
        data='{"channels": [], "guild_template_code": "' +template+ '", "name": "' +name+ '", "system_channel_id": null}').json()

    def create_invite(self, channel: int, age: int = 0, uses: int = 0, temp: bool = False):
        return requests.post(f"https://discord.com/api/v9/channels/{channel}/invites", headers=self.headers, 
        data='{"max_age": ' +str(age)+ ', "max_uses": ' +str(uses)+ ', "temporary": ' +str(temp).lower()+ '}').json()

    def get_invites(self, guild: int):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/invites", headers={"authorization": self.token}).json()

    def create_webhook(self, channel: int, name: str = "nullptr"):
        return requests.post(f"https://discord.com/api/v9/channels/{channel}/webhooks", headers=self.headers, 
        data='{"name": "' +name+ '"}').status_code == 200

    def get_webhooks(self, channel: int):
        return requests.get(f"https://discord.com/api/v9/channels/{channel}/webhooks", headers={"authorization": self.token}).json()

    def delete_webhook(self, webhook: int):
        return requests.delete(f"https://discord.com/api/v9/webhooks/{webhook}", headers={"authorization": self.token}).status_code == 204

    def get_widget(self, guild: int):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/widget", headers={"authorization": self.token}).json()

    def control_widget(self, guild: int, enabled: bool = False, channel_id: int = "null"):
        return requests.patch(f"https://discord.com/api/v9/guilds/{guild}/widget", headers=self.headers,
        data='{"channel_id": "' +str(channel_id)+ '", "enabled": ' +str(enabled).lower()+ '}').json()

    def get_auditlog(self, guild: int, limit: int = 50):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/audit-logs?limit={limit}", headers={"authorization": self.token})

    def member_kick(self, guild: int, member: int):
        return requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers={"authorization": self.token}).status_code == 204

    def member_ban(self, guild: int, member: int, delete_message_days: int = 1):
        return requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=self.headers,
        data='{"delete_message_days": ' +str(delete_message_days)+ '}').status_code == 204

    def get_bans(self, guild: int):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/bans", headers={"authorization": self.token})

    def create_template(self, guild: int, name: str, description: str):
        return requests.post(f"https://discord.com/api/v9/guilds/{guild}/templates", headers=self.headers,
        data='{"name": "' +name+ '","description": "' +description+ '"}').json()

    def delete_template(self, guild: int, code: str):
        return requests.delete(f"https://discord.com/api/v9/guilds/{guild}/templates/{code}", headers={"authorization": self.token})

    def get_templates(self, guild: int):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/templates", headers={"authorization": self.token}).json()
 
    def get_emojis(self, guild: int):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/emojis", headers={"authorization": self.token}).json()

    def get_stickers(self, guild: int):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/stickers", headers={"authorization": self.token}).json()

    def delete_guild(self, guild: int, mfa: str):
        return requests.post(f"https://discord.com/api/v9/guilds/{guild}/delete", headers={"authorization": self.token}, data={"code": mfa}).json()

    def change_accentcolor(self, color: int):
        return requests.patch("https://discord.com/api/v9/users/@me",
        headers=self.headers,
        data='{"accent_color": "' +str(color)+ '"}').status_code == 200

    def create_role(self, guild: int, name: str):
        return requests.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers={"authorization": self.token}, data='{"name": "' +name+ '"}').json()

    def get_roles(self, guild: int):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/roles", headers={"authorization": self.token}).json()

    def edit_role(self, guild: int, role: int, name: str = "Role", permissions: int = 0, hoist: bool = False, mentionable: bool = False, color: int = 0):
        return requests.patch(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}", headers={"authorization": self.token}, 
        data='{"name": ' +name+ ', "permissions": ' +str(permissions)+ ', "color": ' +str(color)+ ', "hoist": ' +str(hoist).lower()+ ', "mentionable": ' +str(mentionable).lower()+ '}').json()

    def change_avatar(self, avatar: str):
        return requests.patch("https://discord.com/api/v9/users/@me",
        headers=self.headers,
        data='{"avatar": "' +avatar+ '"}').json()

    def change_login(self, login: str, password: str):
        return requests.patch("https://discord.com/api/v9/users/@me",
        headers=self.headers,
        data='{"password": "'+password+'", "username": "'+login+'"}').json()

    def change_password(self, new_password: str, password: str):
        return requests.patch("https://discord.com/api/v9/users/@me",
        headers=self.headers,
        data='{"new_password": "'+new_password+'", "password": "'+password+'"}').json()

    def change_nick(self, guild: int, nick: str, user = "@me"):
        return requests.patch(f"https://discord.com/api/v9/guilds/{guild}/members/{user}",
        headers=self.headers,
        data='{"nick": "' +nick+ '"}').status_code == 200

    def get_messages(self, channel: int, limit: int):
        return requests.get(f"https://discord.com/api/v9/channels/{channel}/messages?limit={limit}",
        headers={"authorization": self.token}).json()

    def send_message(self, channel: int, text: str, tts: bool = False):
        return requests.post(f"https://discord.com/api/v9/channels/{channel}/messages",
        data={"content": text},
        headers={"authorization": self.token}).json()

    def delete_message(self, channel: int, message: int):
        return requests.delete(f"https://discord.com/api/v9/channels/{channel}/messages/{message}", 
        headers={"authorization": self.token}).status_code == 204

    def edit_message(self, channel: int, message: int, text: str):
        return requests.patch(f"https://discord.com/api/v9/channels/{channel}/messages/{message}",
        data={"content": text},
        headers={"authorization": self.token}).json()

    def add_reaction(self, channel: int, message: int, reaction: str, user = "@me"):
        # (user: me) for make reaction for self message
        return requests.put(f"https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/{reaction}/{user}", 
        headers={"authorization": self.token}).status_code == 204

    def remove_reaction(self, channel: int, message: int, reaction: str, user = "@me"):
        # (user: me) for make reaction for self message
        return requests.put(f"https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/{reaction}/{user}", 
        headers=self.headers).status_code == 204

    def start_thread(self, channel: int, message: int, name: str, archive: int = 60, type: int = 11):
        return requests.post(f"https://discord.com/api/v9/channels/{channel}/messages/{message}/threads",
        headers=self.headers,
        data='{"auto_archive_duration": ' +str(archive)+ ', "name": "' +name+ '", "type": ' +str(type)+ '}').json()

    def get_activethreads(self, guild: int):
        return requests.get(f"https://discord.com/api/v9/guilds/{guild}/threads/active", headers={"authorization": self.token}).json()

    def create_wopchannel(self, guild: int, name: str, type: int):
        # Create channel without category
        return requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels",
        headers=self.headers,
        data='{"name": "' +name+ '", "permission_overwrites": [], "type": ' +str(type)+ '}').json()

    def create_channel(self, guild: int, name: str, type: int, parent_id: str):
        # Create channel in category
        return requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels",
        headers=self.headers,
        data='{"name": "' +name+ '", "parent_id": "' +str(parent_id)+ '", "permission_overwrites": [], "type": ' +str(type)+ '}').json()

    def edit_channel(self, channel: int, name: str = "NullPTR", type: int = 0, topic: str = "", bitrate: int = 64000, user_limit: int = 0, nsfw: bool = False, rate_limit_per_user: int = 0, default_auto_archive_duration: int = "null", rtc_region: str = "null"):
        return requests.patch(f"https://discord.com/api/v9/channels/{channel}",
        headers=self.headers,
        data='{"name": "' +name+ '", "type": ' +str(type)+ ', "topic": "' +topic+ '", "bitrate": ' +str(bitrate)+ ', "user_limit": ' +str(user_limit)+ ', "nsfw": ' +str(nsfw).lower()+ ', "rate_limit_per_user": ' +str(rate_limit_per_user)+ ', "default_auto_archive_duration": ' +default_auto_archive_duration+ ', "rtc_region": ' +rtc_region+ '}') == 200

    def delete_channel(self, channel: int):
        return requests.delete(f"https://discord.com/api/v9/channels/{channel}",
        headers={"authorization": self.token}).json()
