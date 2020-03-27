import pathlib
import sys
import importlib
import inspect
from os.path import dirname, abspath
import pika
import json

# NOTICE - counting on each parser class to have 1 parsing function exactly
from braincomputer.mq import Mq
from braincomputer.protocol import Snapshot


class Parsers:

    def __init__(self):
        self.parsers_functions = {}
        self.get_all_parsers()

    def parse(self, snapshot):
        for parser in self.parsers_functions.keys():
            self.parsers_functions[parser](snapshot)

    def get_all_parsers(self):
        path_to_import = pathlib.Path((dirname(abspath(__file__)))).absolute()
        sys.path.insert(0, str(path_to_import.parent))
        for p in path_to_import.iterdir():
            if p.name != "parsers.py" and not p.name.startswith("__"):
                import_module_name = f'braincomputer.{path_to_import.name}.{p.stem}'
                importlib.import_module(f'{import_module_name}', package=__package__)
                module = sys.modules[import_module_name]
                function_name, function_value = [(name, value) for name, value
                                                 in inspect.getmembers(module)
                                                 if inspect.isfunction(value)][0]
                module_field = getattr(function_value, "field")
                self.parsers_functions[module_field] = function_value
        print(self.parsers_functions)


class Parser:
    def __init__(self, parsing_function, parser_type, mq_url):
        self.parsing_function = parsing_function
        self.parser_type = parser_type
        self.mq = Mq(mq_url)

    def callback(self, ch, method, properties, body):
        print("in callback, parsed data:")
        parsed = self.parsing_function[self.parser_type](body)
        print(parsed)
        self.mq.send_to_queue('parsed', parsed)

    def create_queue(self):
        queue_name = 'queue'
        self.mq.create_queue(queue_name)
        parsed_queue_name = 'parsed'
        self.mq.create_queue(parsed_queue_name)
        self.mq.consume_queue(queue_name, self.callback)


def run_parser(parser_type, mq_url):
    parsers = Parsers()
    print('parsing...')
    print(parser_type)
    parser = Parser(parsers.parsers_functions, parser_type, mq_url)
    parser.create_queue()
