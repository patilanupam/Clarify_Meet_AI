"""
Configuration settings for ClarifyMeet AI application
"""
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    APP_NAME: str = "ClarifyMeet AI - Meeting Minutes Generator"
    API_PREFIX: str = "/api/v1"

    # Ollama LLM settings
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "tinyllama"

    # File upload limits
    MAX_TRANSCRIPT_SIZE_MB: int = 10

    # CORS settings
    CORS_ORIGINS: list = ["*"]

    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"  # Allow extra fields from environment
    )


settings = Settings()

