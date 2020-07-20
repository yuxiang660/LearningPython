from configparser import ConfigParser

if __name__ == "__main__":
    cfg = ConfigParser()
    cfg.read('config.ini')
    print(cfg.sections())
    print(cfg.get('server', 'signature'))