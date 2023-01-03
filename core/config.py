import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "dev"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_BASEURL: str = os.getenv("APP_BASEURL", "localhost")
    APP_PORT: int = os.getenv("APP_PORT", "8000") 
    IDP_SERVER_URL: str = os.getenv("IDP_SERVER_URL", "")
    IDP_CLIENT_ID: str = os.getenv("IDP_CLIENT_ID", "")
    IDP_CLIENT_SECRET : str = os.getenv("IDP_CLIENT_SECRET", "")
    IDP_ADMIN_CLIENT_SECRET : str = os.getenv("IDP_ADMIN_CLIENT_SECRET", "")
    IDP_REALM: str = os.getenv("IDP_REALM", "")
    CALLBACK_URI: str = os.getenv("IDP_REALM", f"http://{APP_BASEURL}:{APP_PORT}/auth/callback") 

class DevelopmentConfig(Config):
    DEBUG: bool = True

class ProductionConfig(Config):
    DEBUG: bool = False
    ENV: str = "prod"

def get_config():
    env = os.getenv("ENV", "dev")

    config_type = {
        "dev": DevelopmentConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
