# BrainComputer
[![Build Status](https://travis-ci.org/ElaKadosh13/BrainComputer.svg?branch=master)](https://travis-ci.org/ElaKadosh13/BrainComputer)
![coverage](https://codecov.io/gh/ElaKadosh13/BrainComputer/branch/master/graph/badge.svg)

An example package. See [full documentation](https://advanced-system-design-foobar.readthedocs.io/en/latest/).

## Installation

1. Clone the repository and enter it:

    ```
    $ git clone git@github.com:ElaKadosh13/BrainComputer.git
    $ cd braincomputer/
    ```

2. Run the installation script and activate the virtual environment:

    ```
    $ ./scripts/install.sh
    $ source .env/bin/activate
    ```

3. To check that everything is working as expected, run the tests:

    ```
    $ pytest tests/
    ```
4. To deploy: 
    ```
    $ ./scripts/run-pipelines.sh
    ```
5. Run the client manually or using:
    ```
    $ ./scripts/run-client-cli.sh
    ```
## Usage

The `braincomputer` package also provides a command-line interface:

```sh
Cli commands:
$ python -m braincomputer
Usage: braincomputer.[Class] [OPTIONS] COMMAND [ARGS]...

Options:
  --version        Show the version and exit.
  -q, --quiet
  -t, --traceback
  --help           Show this message and exit.

Commands:
  1. Server    run-server       run server forever
  2. Client    upload-sample    upload client snapshots
  3. Saver     run-saver        run saver forever
               save             saves one object
  4. Parsers   run-parser       run parsers forever
               parse            parses one object
  5. Api       run-server       run api server forever
  6. Gui       run-server       run gui server forever       

Cli:
```sh
$ python -m braincomputer.cli get-users
$ python -m braincomputer.cli get-user 1
$ python -m braincomputer.cli get-snapshots 1
$ python -m braincomputer.cli get-snapshot 1 2
$ python -m braincomputer.cli get-result 1 2 'pose'
```

All commands accept the `-q` or `--quiet` flag to suppress output, and the `-t`
or `--traceback` flag to show the full traceback when an exception is raised
(by default, only the error message is printed, and the program exits with a
non-zero code).

## Gui
Navigate to http://127.0.0.1:8080.

##Adding a parser
Just add it to the parsers directory, parser x should have a single parsing function 'parse_x'
and a field - parse_x.field = 'x' 
also - add the parser name x to the config fields in the server, and to the listening queues topics (key) in the saver