from configparser import ConfigParser

ini = ConfigParser()
ini.read_file(open("config.ini", "r", encoding="utf-8"))
db = ini["db"]

config = {}

config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://" + db["user"] + ":" \
        + db["password"] + "@" + db["host"] + "/" + db["db"] \
        + "?charset=utf8mb4"
config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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
