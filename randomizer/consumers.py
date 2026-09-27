import logging

from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)


class SeedStatusConsumer(AsyncJsonWebsocketConsumer):
    seed_id: str
    group_name: str

    async def connect(self) -> None:
        self.seed_id = self.scope["url_route"]["kwargs"]["seed_id"]
        self.group_name = f"seed-status-{self.seed_id}"

        # Join seed status group.
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code: int) -> None:
        # Leave seed status group.
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def seed_status(self, event: dict) -> None:
        await self.send_json(event)

    async def seed_finished(self, event: dict) -> None:
        await self.send_json(event)

    async def seed_failed(self, event: dict) -> None:
        await self.send_json(event)
