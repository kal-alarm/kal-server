from channels.routing import route
from kalalarm.consumers import ws_message, ws_add, ws_disconnect

channel_routing = [
    route("http.request", "kalalarm.consumers.http_consumer"),
    route("websocket.receive", ws_message),
    route("websocket.connect", ws_add),
    route("websocket.disconnect", ws_disconnect),
]