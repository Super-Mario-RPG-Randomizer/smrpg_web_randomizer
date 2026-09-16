from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/seed/status/<slug:seed_id>', consumers.SeedStatusConsumer.as_asgi(), name='ws-generate-status'),
]
