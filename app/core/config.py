from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = "Process Events API"
    api_v1_prefix: str = "/v1"
    debug: bool = False
    environment: str = Field(default="development", env="ENVIRONMENT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instancia global
settings = Settings()
# Función para obtener la configuración global
def get_settings() -> Settings:
    return settings
