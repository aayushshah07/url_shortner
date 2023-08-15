from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name = "Local"
    db_url  = "sqlite:///./shortener.db"
    base_url = "http://localhost:8000"


def get_settings():
    settings = Settings()
    print("Loading setting from %s ", settings.env_name)
    return settings