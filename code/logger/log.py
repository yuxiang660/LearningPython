import logging
import logging.config

if __name__ == "__main__":
    # Configure the logging system
    # logging.basicConfig(
    #     # filename='app.log',
    #     level=logging.DEBUG,
    #     format='%(levelname)s:%(asctime)s:%(message)s'
    # )
    logging.config.fileConfig('config.ini')
    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'
    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')
