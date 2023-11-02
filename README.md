# pydiner

Keep your [development environments] clean.

<img
  alt="The Dirty Fork"
  src="https://raw.githubusercontent.com/samkennerly/posters/master/pydiner.jpeg"
  title="Lucky I didn't tell them about the dirty knife.">

[development environments]: https://en.wikipedia.org/wiki/Sandbox_(software_development)

## abstract

`pydiner` is a [template] for a generic Python project which:

- runs code in [Docker containers] which [self-destruct].
- never reads or modifies files outside of its repository.
- never installs software outside of its own [Docker images].
- never uses or modifies other Pythons, [Anaconda], or [virtualenvs].
- updates `requirements.txt` with [pinned versions] of all [pip] installs.

These rules are intended to avoid [dependency hell].

[template]: https://help.github.com/en/articles/creating-a-repository-from-a-template
[Docker containers]: https://docs.docker.com/develop/
[self-destruct]: https://docs.docker.com/engine/reference/run/#clean-up---rm
[Docker images]: https://docs.docker.com/engine/docker-overview/
[Anaconda]: https://www.anaconda.com/
[virtualenvs]: https://virtualenv.pypa.io/en/latest/
[pinned versions]: https://pip.pypa.io/en/stable/user_guide/#pinned-version-numbers
[pip]: https://pip.pypa.io/en/stable/
[dependency hell]: https://en.wikipedia.org/wiki/Dependency_hell


## basics

To start a new project:

1. Create a [Git repo from this template].
1. Delete any files and folders you don't want.
1. Edit the `Dockerfile` to choose a Python version.
1. Edit `requirements.txt` to choose Python packages.
1. Open a [terminal], `cd` to this folder, and run this command:
```sh
./kitchen
```
This should print a help message for the `kitchen` script.

### `kitchen` functions

The `kitchen` script defines [shell functions] which run common Docker commands.

```sh
# Bake a Docker image named pydiner:monty
./kitchen bake monty

# Run Python in an interactive pydiner:monty container
./kitchen runit monty python

# Same as above, but with the current working directory mounted as /context
./kitchen serve monty python

# Run tests in an interactive pydiner:monty container
./kitchen runit monty python -m test

# Same as above, but use pytest to run tests
./kitchen runit monty pytest

# Freeze requirements.txt and rebuild pydiner:monty
./kitchen freeze monty

# Delete the image, its containers, and any leftovers
./kitchen eightysix monty
```
Typing `./kitchen` before each command is optional if the `kitchen` script is [sourced].

[Git repo from this template]: https://help.github.com/en/articles/creating-a-repository-from-a-template
[terminal]: https://en.wikipedia.org/wiki/Command-line_interface
[shell functions]: https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html
[sourced]: https://en.wikipedia.org/wiki/Source_(command)

### `bake` an image

`./kitchen bake` builds (or updates) a Docker image with copies of files from the [build context].

- Edit `requirements.txt` to specify which Python packages should be installed.
- Edit `.dockerignore` to declare file patterns which should never be copied.
- Edit `Dockerfile` to choose which non-ignored files are copied into images.

The default image name is `pydiner:latest`.

[build context]: https://docs.docker.com/engine/reference/commandline/build/

### `runit` interactively

`./kitchen runit` [runs a new interactive container] from a previously-baked image.

- Inside a container, <q>baked-in</q> copies of files are in the `/context` folder.
- Modifying files inside the container does not affect the original files.
- Type `exit` to exit the container. It should then [self-destruct].

[runs a new interactive container]: https://docs.docker.com/engine/reference/commandline/run/

### `serve` with mounted files

`./kitchen serve` runs a container with the current folder [mounted] as `/context`.

- Processes inside the container **can modify or delete** mounted files.
- Changes to mounted files will be visible inside and outside the container.
- Any files baked into `/context` will be obscured by the <q>fresh</q> mounted files.

[mounted]: https://docs.docker.com/storage/bind-mounts/

### `freeze`

`./kitchen freeze` [pins] Python packages to ensure [reproducible builds].

- The first time an image is baked, `pip` installs packages automatically.
- If an image is frozen, then baking it again uses the same package versions.
- Freezing an image will **overwrite** `requirements.txt`.

[pins]: https://pip.pypa.io/en/stable/user_guide/#pinned-version-numbers
[reproducible builds]: https://en.wikipedia.org/wiki/Reproducible_builds


## contents

This repo contains examples of common project files:

- [bin/](bin) contains example scripts.
- [etc/](etc) contains example configuration files.
- [src/](src) contains an example Python [package].
- [test/](test) is an [executable package] which runs tests.
- [var/](var) contains files output by the executables.

[package]: https://docs.python.org/3/tutorial/modules.html#packages
[executable package]: https://docs.python.org/3/library/__main__.html


## dependencies

`pydiner` has exactly one dependency:

- Docker for [Linux] or [Mac] or [Windows]

Windows users may need to edit the `kitchen` script for [path compatibility].

[Linux]: https://docs.docker.com/install/
[Mac]: https://docs.docker.com/docker-for-mac/install/
[Windows]: https://docs.docker.com/docker-for-windows/
[path compatibility]: https://en.wikipedia.org/wiki/Path_(computing)#MS-DOS/Microsoft_Windows_style


## examples

*Caution:* Remember to `cd` to this folder before using `kitchen` functions.

Bake a `pydiner:latest` image, freeze it, and serve `bash`.
```sh
[+] Building 0.9s (11/11) FINISHED                                docker:desktop-linux
 => [internal] load .dockerignore                                                 0.0s
 => => transferring context: 138B                                                 0.0s
 => [internal] load build definition from Dockerfile                              0.0s
 => => transferring dockerfile: 539B                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.12.0                  0.7s
 => [1/6] FROM docker.io/library/python:3.12.0@sha256:7b8d65a924f596eb65306214f5  0.0s
 => [internal] load build context                                                 0.0s
 => => transferring context: 10.84kB                                              0.0s
 => CACHED [2/6] RUN apt-get -y update && apt-get -y install less tree vim        0.0s
 => CACHED [3/6] COPY requirements.txt /tmp                                       0.0s
 => CACHED [4/6] RUN pip install --upgrade pip && pip install --requirement /tmp  0.0s
 => [5/6] COPY [., /context]                                                      0.0s
 => [6/6] WORKDIR /context                                                        0.0s

...

root@pydiner:/context#

```

From the inside, a container looks like a Linux machine.
```sh
root@pydiner:/context# which python
/usr/local/bin/python
root@pydiner:/context# grep PRETTY_NAME /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
root@pydiner:/context#
```

Python can import packages from the `src/` folder without hacking [sys.path]:
```sh
root@pydiner:/context# python
Python 3.12.0 (main, Nov  1 2023, 12:56:53) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pydiner
>>> pydiner.echo("Hello, World!")
2023-11-02 23:00:27 Hello, World!
>>> exit()
root@pydiner:/context#
```

Scripts in `/context/bin` are already on the system [PATH].
```sh
root@pydiner:/context# scrambled -o example.txt eggs
2023-11-02 23:05:33 Read parameters from  /context/etc/default
2023-11-02 23:05:33 Calculate 24 permutations of 'eggs'
2023-11-02 23:05:33 Write output to /context/var/example.txt
root@pydiner:/context#
```

[sys.path]: https://docs.python.org/3/library/sys.html#sys.path
[PATH]: https://en.wikipedia.org/wiki/PATH_(variable)


## faq

### How do I install `pydiner`?

Don't. Use it as a [template] for a new repository.

[template]: https://help.github.com/en/articles/creating-a-repository-from-a-template

### I'm stuck inside a container!

Press *CTRL-D* or type `exit` to exit a container.

### Do I have to run containers as root?

Not if you create a `USER`. See the [Dockerfile reference] for details.

[Dockerfile reference]: https://docs.docker.com/engine/reference/builder/

### Can I run containers in the background?

Yes, but not with the `kitchen` script. See the [Docker run reference].

[Docker run reference]: https://docs.docker.com/engine/reference/run/

### What exception handler does `pydiner` use?

None. Programs [stop immediately] when something goes wrong.

[stop immediately]: https://global.toyota/en/company/vision-and-philosophy/production-system/

### What testing framework does `pydiner` use?

None, but it has been tested with [pytest] to ensure compatibility.

[pytest]: https://docs.pytest.org/en/latest/

### What logging framework does `pydiner` use?

[None]. `utensils.achtung()` prints to `STDERR`. `utensils.echo()` prints to `STDOUT`.

[None]: https://12factor.net/logs

### What are some other Python project templates?

- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [PyPA tutorial](https://packaging.python.org/tutorials/packaging-projects/)
- [PyPA sample project](https://github.com/pypa/sampleproject)
- [python-boilerplate.com](https://www.python-boilerplate.com)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
