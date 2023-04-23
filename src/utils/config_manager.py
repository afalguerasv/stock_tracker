import json

config_file = "C:\\test\\stockproject\\config\\config.json"

def get_conf(group: str, elem: str):
    with open(config_file,'r') as cf:
        config = json.load(cf)
        return config[group][elem]

if __name__ == '__main__':
    value = get_conf("DB","DB_NAME")
    print(value)