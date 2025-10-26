from urllib.parse import quote_plus
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_HOST: str
    MONGO_DB: str
    MONGO_APPNAME: str
    

    @property
    def mongo_uri(self) -> str:
        user = quote_plus(self.MONGO_USER)
        pwd = quote_plus(self.MONGO_PASSWORD)
        return f"mongodb+srv://{user}:{pwd}@{self.MONGO_HOST}/{self.MONGO_DB}?appName={self.MONGO_APPNAME}"

    class Config:
        env_file = ".env"

settings = Settings()
