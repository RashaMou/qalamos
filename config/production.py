from .base import BaseConfig


class ProductionConfig(BaseConfig):
    """Production configuration."""

    # Production-specific settings
    WORKERS_COUNT: int = 4  # Adjust based on CPU cores
    LOG_LEVEL: str = "error"
