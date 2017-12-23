from channels import Group

__author__ = 'ziven'


def ws_add(message):
    Group("chat").add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    Group("chat").send({
        "text": "connect success!",
    })

    Group("aa").send({
        "text": "connect success!",
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
