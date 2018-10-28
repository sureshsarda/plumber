import logging
import argparse
import yaml
import time
from steps.step import Step, Echo

STEPS_TYPES = {
    'echo': Echo()
}


class Plumber:

    def execute(self, conf):
        name = conf.get('name', 'Name not present')
        LOGGER.info('Running configuration: ' + name)

        for step_obj in conf.get('steps', []):

            s = step_obj['step']
            LOGGER.info('Executing Step: ' + s.get('name', 'No name present'))

            step_args = s['arguments']

            for i in range(s.get('repeat', 1)):
                STEPS_TYPES.get(s['type'], Step).execute(**step_args)
                time.sleep(s.get('wait', 0))

            LOGGER.info('Step[{0}] execution complete'.format(s['name']))


def read_configuration(filepath):
    with open(filepath, 'r') as f:
        return yaml.load(f)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('config_path', help='File to read the configuration from', type=str)
    parser.add_argument('--log-level', dest='log_level', help='Log level', type=str, default='DEBUG')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    logging.basicConfig(level=args.log_level)
    LOGGER = logging.getLogger(__name__)

    LOGGER.debug('Loading configuration...')
    conf = read_configuration(args.config_path)
    LOGGER.debug('Configuration loading successful')

    Plumber().execute(conf)
