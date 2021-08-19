import os

from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# Для вк
token = os.getenv("TOKEN")
public = os.getenv("PUBLIC_ID")
phone = os.getenv("LOGIN_VK")
password = os.getenv("PASSWORD_VK")
admin_id = os.getenv("ADMIN")


# Для базы данных
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
