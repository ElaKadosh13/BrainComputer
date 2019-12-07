# BrainComputer


An example package. See [full documentation](https://advanced-system-design-foobar.readthedocs.io/en/latest/).

## Installation

1. Clone the repository and enter it:

    ```sh
    $ git clone git@github.com:ElaKadosh13/BrainComputer.git
    ...
    $ cd braincomputer/
    ```

2. Run the installation script and activate the virtual environment:

    ```sh
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    ```

3. To check that everything is working as expected, run the tests:


    ```sh
    $ pytest tests/
    ...
    ```

## Usage

The `braincomputer` packages provides the following classes:

- `client`

- `server`

- `website`

- `web`

...........


The `braincomputer` package also provides a command-line interface:

```sh
$ python -m braincomputer
braincomputer, version 0.1.0
```

All commands accept the `-q` or `--quiet` flag to suppress output, and the `-t`
or `--traceback` flag to show the full traceback when an exception is raised
(by default, only the error message is printed, and the program exits with a
non-zero code).

The CLI provides the `braincomputer` command, with the `run_server`, `upload_thought`
subcommands:

```sh
$ python -m braincomputer run-server "127.0.0.1:5000" "tmp/data"

$ python -m braincomputer upload-thought "127.0.0.1:5000" 1 "my thought"
