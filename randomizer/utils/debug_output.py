"""Developer-only console output and file dumps, off outside DEBUG."""

import logging
from typing import Any

from django.conf import settings

DEBUG_FILE_DUMPS: bool = bool(settings.DEBUG)
DEBUG_PRINTS: bool = bool(settings.DEBUG)

logger = logging.getLogger(__name__)


def debug_print(*args: Any, **kwargs: Any) -> None:
    """Print only when DEBUG_PRINTS is on."""
    logging.debug(*args, **kwargs)
