from .base import BaseConfig


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG: bool = True
    RELOAD: bool = True
    WORKERS_COUNT: int = 1
    LOG_LEVEL: str = "debug"
