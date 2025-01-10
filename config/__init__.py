import os
from typing import Dict, Any

from .development import DevelopmentConfig
from .production import ProductionConfig


def get_config() -> Dict[str, Any]:
    """Return the appropriate configuration based on environment."""
    env = os.getenv("ENVIRONMENT", "development")

    if env == "production":
        return ProductionConfig().dict()
    return DevelopmentConfig().dict()


config = get_config()
