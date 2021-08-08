import selfdiscord
from time import sleep

if __name__ == "__main__":
    client = selfdiscord.Client("Token here")

    # Making own example server
    server = client.create_guild("NullPTR [selfdiscord]")

    category = client.create_wopchannel(server["id"], "NULLPTR", 4)
    chat = client.create_channel(server["id"], "nullchat", 0, category["id"])
    voice = client.create_channel(server["id"], "nullvoice", 2, category["id"])

    sleep(0.1)
    client.edit_channel(chat["id"], chat["name"], topic="This channel created from selfdiscord api!")

    msg = client.send_message(chat["id"], "selfdiscord api - developed by slavatar")
    sleep(1)
    client.edit_message(chat["id"], msg["id"], "selfdiscord edited this message")
    client.change_accentcolor(16767488)
    #client.change_login("NULLPTR", "UrPassword")
    #client.change_password("NewPassword", "UrPassword")
    client.change_nick(server["id"], "NullPTR") # Set local nickname on server
    thread = client.start_thread(msg["channel_id"], msg["id"], "NULLPTR")
    
    client.create_webhook(chat["id"])
    webhook = client.get_webhooks(chat["id"])[0]
    webhook = selfdiscord.Webhook(f"https://discord.com/api/webhooks/{webhook['id']}/{webhook['token']}")
    webhook.execute("Hello world!", "Slavatar")

    print(client.delete_guild(server["id"], str(input("Enter 2FA: "))))

    """
    OR U CAN TRY THIS: (rainbow background on ur profile)
    while True:
        sleep(3)

        if (cur_color >= 16777215):
            step = -step
        if (cur_color <= step):
            step = step + step
        
        cur_color += step
        client.change_accentcolor(cur_color)
    """
