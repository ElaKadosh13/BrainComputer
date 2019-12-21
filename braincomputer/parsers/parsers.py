import pathlib
import sys
import importlib
import inspect
from os.path import dirname, abspath


# NOTICE - counting on each parser class to have 1 parsing function exactly

class Parsers:

    def __init__(self):
        self.parsers_functions = {}
        self.get_all_parsers()

    def parse(self, context, snapshot):
        for parser in self.parsers_functions.keys():
            self.parsers_functions[parser](context, snapshot)

    def get_all_parsers(self):
        path_to_import = pathlib.Path((dirname(abspath(__file__)))).absolute()
        sys.path.insert(0, str(path_to_import.parent))
        for p in path_to_import.iterdir():
            if p.name != "parsers.py" and p.name != "__init__.py":
                import_module_name = f'braincomputer.{path_to_import.name}.{p.stem}'
                importlib.import_module(f'{import_module_name}', package=__package__)
                module = sys.modules[import_module_name]
                function_name, function_value = [(name, value) for name, value
                                                 in inspect.getmembers(module)
                                                 if inspect.isfunction(value)][0]
                module_field = getattr(function_value, "field")
                self.parsers_functions[module_field] = function_value
        print(self.parsers_functions)
