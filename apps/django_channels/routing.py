from apps.django_channels.customer import ws_add, ws_message, ws_disconnect
from channels.routing import route

__author__ = 'ziven'

channel_routing = [
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]