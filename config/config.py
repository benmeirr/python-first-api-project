from pydantic import BaseSettings


class Config(BaseSettings):
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "root_password"
    MYSQL_DATABASE: str = "main"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: str = "3306"
    DATABASE_URL: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    TOKEN_EXPIRY_TIME: float = 20.0
    SECRET_KEY: str = "user_app"
    ALGORITHM: str = "HS256"
