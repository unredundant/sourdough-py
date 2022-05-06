# Sourdough.py

Welcome to the Python Sourdough starter ❤️

## Pre-requisites

This template repository relies on a number of dependencies that you will need before you start developing your
application

- [Python](https://www.python.org/) (duh). You will need a base python interpreter in order to run this project
- [PyEnv](https://github.com/pyenv/pyenv). Optional, but very useful as a layer on top of your base interpreter to
  provide seamless version management.
- [Poetry](https://python-poetry.org/). Python dependency manager
- [Changie](https://changie.dev/). (Optional) Automated CHANGELOG management
- [Just](https://github.com/casey/just).  (Optional, but _highly_ recommended) Just a command runner
- [Docker](https://www.docker.com/). Used to provision local infrastructure
- [Act](https://github.com/nektos/act) (Optional) Allows you to run GitHub Actions locally to debug pipeline issues

## Local Development

### Set up

Once you have installed the pre-requisites, you are ready to start running the app locally.

Go ahead and run

```shell
just setup
```

The first command will install all dependencies, while the second will install the pre-configured git hooks to ensure
that your code is linted and formatted prior to pushing.

### Running the API

To run the API

```shell
just api
```

This will launch your shiny new API ✨ head on over to `localhost:8080/docs` and you should be greeted with beautiful,
autoconfigured API documentation

### Running the CLI

To run the CLI

```shell
just cli -h
```

### Running tests

Tests are managed via pytest, and are set up to be run via

```shell
just test
```

### Misc

For additional available commands, run

```shell
just --list
```