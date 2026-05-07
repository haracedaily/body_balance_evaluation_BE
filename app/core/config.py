from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_KEY: str
    OPENAI_API_KEY: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()