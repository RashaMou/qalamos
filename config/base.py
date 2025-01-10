from pydantic import BaseModel


class BaseConfig(BaseModel):
    """Base configuration."""

    APP_NAME: str = "Qalamos"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS_COUNT: int = 4
    WORKER_TIMEOUT: int = 120
    RELOAD: bool = False
    LOG_LEVEL: str = "info"
