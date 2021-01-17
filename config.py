from configparser import ConfigParser
from dotenv import load_dotenv
import os

load_dotenv()

load_dotenv(verbose=True)

ini = ConfigParser()
ini.read_file(open("config.ini", "r", encoding="utf-8"))

config = {}

config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://" + os.getenv("DB_USER") + ":" \
        + os.getenv("DB_PASSWORD") + "@" + os.getenv("DB_HOST") + "/" + os.getenv("DB_DB") \
        + "?charset=utf8mb4"
config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print("Connecting to MySQL", "\nUser:",os.getenv("DB_USER"),"\nPassword:",os.getenv("DB_PASSWORD"),"\nHost:",os.getenv("DB_HOST"),"\nDatabase:",os.getenv("DB_DB"))

config.update(ini["hcaptcha"])
config.update(ini["flask"])
config.update(ini["http"])
config.update(ini["site"])

new_config = {}

for key, value in config.items():
    if value == "no":
        value = False
    elif value == "yes":
        value = True
    new_config[key.upper()] = value

config = new_config
