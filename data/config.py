from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str('ip')

banned_users = []