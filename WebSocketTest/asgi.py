import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import mainapp.routing


# os.environ['DJANGO_SETTINGS_MODULE'] = 'WebSocketTest.settings'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebSocketTest.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            mainapp.routing.websocket_urlpatterns
        )
    ),
})