import configparser

def readConfig(config_file = "sample_config.ini"):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config