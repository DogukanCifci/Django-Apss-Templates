from .base import * 
 
 
env_name = config("ENV_NAME")   #.env den cekiyoruz. Hangi processteysem .env de o prosesi degisitiririm.
 
if env_name == "prod": 
 
    from .prod import * 
 
elif env_name == "dev": 
 
    from .dev import *