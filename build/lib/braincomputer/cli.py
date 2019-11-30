import sys
import inspect

class CommandLineInterface:
    functions_mapping = {}

    def command(self, f):
        expected_args = inspect.getfullargspec(f)[0]
        self.functions_mapping[f.__name__] = (f, expected_args)
        return f

    def main(self):
        if len(sys.argv) < 3:
            self.usage_mistake()
        function_name = sys.argv[1]
        function_arguments = self.parse_arguments()
        if function_name in self.functions_mapping:
            function = self.functions_mapping[function_name][0]
            expected_args =  self.functions_mapping[function_name][1]
            args = self.verify_and_get_arguments(expected_args, function_arguments)
            function(*args)
        sys.exit(0)

    def usage_mistake(self):
        print("USAGE: python example.py <command> [<key>=<value>]*")
        sys.exit(1)

    def parse_arguments(self):
        function_arguments = {}
        for item in sys.argv[2:]:
            if (item.find("=") == -1):
                self.usage_mistake()
            kv = item.split("=")
            if (kv[0] == '' or kv[1] == ''):
                self.usage_mistake()
            function_arguments[kv[0]] = kv[1]
        return function_arguments

    def verify_and_get_arguments(self, expected_args, args):
        function_arguments = []
        for item in expected_args:
            if(item not in args.keys()):
                print(args.keys())
                print("4")
                self.usage_mistake()
            else:
                function_arguments.append(args[item])
        return function_arguments

