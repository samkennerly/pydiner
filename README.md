# pydiner

Snakes on a plate.

## abstract

Pydiner is a [template]() for a generic Python project which:

- runs all code in [containers]() which [self-destruct]()
- never installs software outside of its own Docker [images]()
- never uses or modifies other Pythons, [Anaconda](), or [virtualenvs]()
- updates `requirements.txt` with [pinned versions]() of installed Python packages

These rules are intended to minimize time spent in [dependency hell]().

## basics

To start a new project:

1. Generate a new repo [from this template]().
2. Edit the `Dockerfile` to choose a Python version and system packages.
3. Edit `requirements.txt` to choose Python packages to install with `pip`.
4. Open a terminal, `cd` to this folder, and run these commands:

```sh
# Show all commands and Docker inventory
./kitchen help

# Build a Docker image named pydiner:monty
./kitchen bake monty

# Update requirements.txt and rebuild pydiner:monty
./kitchen freeze monty

# Run Python in a container with $PWD mounted as /context
./kitchen serve monty python

# Run a script in a container with $PWD mounted as /context
./kitchen serve monty scrambled eggs

# Run all pydiner tests without mounting any folders
./kitchen runit monty python -m test

# Show which files were baked into the pydiner:monty image
./kitchen runit monty tree

# Delete the image, its containers, and any leftovers
./kitchen eightysix monty
```
Typing `./kitchen` before each command is not necessary if the kitchen is [sourced]().

## contents

Pydiner includes examples of common Python project ingredients:

- [bin/](bin) contains executable scripts.
- [etc/](etc) contains configuration files.
- [src/](src) contains an importable [package]().
- [test/](test) is an [executable package]() which runs tests.
- [var/](var) contains files output by the script(s).

The [folder structure]() is loosely based on a C++ template from [hiltmon.com](https://hiltmon.com/blog/2013/07/03/a-simple-c-plus-plus-project-structure/).

### the kitchen script

Pydiner's [kitchen](kitchen) defines [shell functions]() for running containers.
Run `kitchen help` for details.

`./kitchen bake` copies files from the the [build context]() into an image's `/context` folder.

- Edit the `Dockerfile` to choose which files are copied into images.
- Files matching patterns in `.dockerignore` are never copied into images.
- Each `pydiner` container gets an independent copy of the `/context` folder.
- Files baked into an image do **not** update themselves when the originals change.

`./kitchen freeze` runs `pip freeze` and saves the output to `requirements.txt`.

- When a new `pydiner` image is baked, it uses `pip` to install requirements.
- On subsequent bakes, `pip` might not run again if `requirements.txt` is unchanged
- Running `freeze` forces `pip` to install the same package versions every time.
- Freezing **overwrites** anything that was in `requirements.txt`.

`./kitchen serve` runs a container with the current folder [mounted]() as `/context`.

- Images are [immutable](). Rebuilding is the only way to update baked-in files.
- Running `serve` runs a new container with real-time access to the original files.
- Any files baked into `/context` will be [shadowed]() by these <q>fresh</q> files.
- Mounts are **not** copies. If a mounted file dies in a container, it dies in the real world.

## dependencies

Pydiner does not require Python. It has one dependency:

- Docker for [Linux]() or [Mac]() or [Windows]()

Windows users may need to edit the [kitchen]() script for [path compatibility]().

## examples (UNDER CONSTRUCTION)

If everything worked, your terminal should look like this:
```bash
Successfully tagged pydiner:latest
Total reclaimed space: 0B
root@pydiner:/context#
```

Each `pydiner` container acts like a real Linux machine:
```bash
root@pydiner:/context# which python
/usr/local/bin/python
root@pydiner:/context# grep PRETTY_NAME /etc/os-release
PRETTY_NAME="Debian GNU/Linux 10 (buster)"
```
Project files are in the `/context` folder:
```bash
root@pydiner:/context# ls
Dockerfile  LICENSE  README.md  TODO.txt  bin  etc  kitchen  requirements.txt  setup.py  src  test  var
```
Packages in [requirements.txt] and [setup.py] have been installed:
```bash
root@pydiner:/context# flake8
./test/test_utensils.py:15:26: E203 whitespace before ':'
```
The `pydiner` package can be imported without hacking [sys.path]:
```bash
root@pydiner:/context# python
Python 3.7.4 (default, Jul 13 2019, 14:04:11)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pydiner
>>> pydiner.echo("Hello, World!")
2019-08-24 22:35:05 Hello, World!
```
Scripts in the project's [bin/] folder are on the system [PATH]:
```bash
root@pydiner:/context# soda --fizz 2 --buzz 3 1 10
1 Fizz  Buzz  Fizz  5 FizzBuzz  7 Fizz  Buzz
```

## faq

### Let me out of this thing!

Hit *CTRL-D* to exit a container.

### How do I install PyDiner?

Don't. Use it as a [template]() for a new repository.

### Can I run containers in the background?

Yes, but not with the `kitchen` script.
See the [Docker run reference]().

### Do I have to run as root inside a container?

Not if you create a `USER`. See the [Dockerfile reference] for details.

### What testing framework does `pydiner` use?

None, but it has been tested with [pytest]() to ensure compatibility.

### What logging framework does `pydiner` use?

[None](https://12factor.net/logs).
Calling `achtung()` prints to `STDERR`.
Calling `echo()` prints to `STDOUT`.

### What are some other Python project templates?

- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [PyPA tutorial](https://packaging.python.org/tutorials/packaging-projects/)
- [PyPA sample project](https://github.com/pypa/sampleproject)
- [pythonizr.com](https://pythonizr.com/)
- [python-boilerplate.com](https://www.python-boilerplate.com)




[hidden state]: https://twitter.com/alicegoldfuss/status/1116150186827337729
[Docker storage docs]: https://docs.docker.com/storage/
[framework]: https://en.wikipedia.org/wiki/Dungeon
[logging framework]: https://en.wikipedia.org/wiki/Dungeon
[testing framework]: https://en.wikipedia.org/wiki/Dungeon
[logs to STDOUT]: https://12factor.net/logs
[does not catch exceptions]: https://hiltmon.com/blog/2017/03/12/notification-city/
[stops immediately]: https://global.toyota/en/company/vision-and-philosophy/production-system/
[bind mount]: https://docs.docker.com/storage/bind-mounts/
[source]: https://en.wikipedia.org/wiki/Source_(command)
[uninstalled packages]: https://pip.pypa.io/en/stable/reference/pip_uninstall/
[nuked from orbit]: https://www.imdb.com/title/tt0090605/quotes
[Dockerfile reference]: https://docs.docker.com/engine/reference/builder/
[à la carte]: https://en.wikipedia.org/wiki/%C3%80_la_carte
[new repository]: https://help.github.com/en/articles/creating-a-repository-from-a-template
[terminal]: https://en.wikipedia.org/wiki/Command-line_interface
[Dockerfile]: Dockerfile
[base image]: https://hub.docker.com/_/python
[setup.py]: setup.py
[pip]: https://pypi.org/project/pip/
[delete themselves]: https://docs.docker.com/engine/reference/run/#clean-up---rm
[pdb]: https://docs.python.org/3/library/pdb.html
[sourced]: https://en.wikipedia.org/wiki/Source_(command)
[bash]: https://en.wikipedia.org/wiki/Bash_(Unix_shell)
[Docker Community Edition]: https://docs.docker.com/v17.12/install/
[zshell]: https://en.wikipedia.org/wiki/Z_shell
[Docker for Mac]: https://docs.docker.com/docker-for-mac/install/
[Docker for Windows]: https://docs.docker.com/docker-for-windows/
[zshell for Windows]: https://superuser.com/questions/1363735/is-it-possible-to-use-zsh-in-windows-machines
[Windows file path]: https://en.wikipedia.org/wiki/Path_(computing)#MS-DOS/Microsoft_Windows_style
[template]: https://help.github.com/en/articles/creating-a-template-repository
[Python]: https://www.python.org/
[Docker]: https://docs.docker.com/get-started/
[sandboxes]: https://en.wikipedia.org/wiki/Sandbox_(software_development)
[base image]: https://hub.docker.com/_/python
[requirements]: https://pip.readthedocs.io/en/1.1/requirements.html
[pinned versions]: https://pip.pypa.io/en/stable/user_guide/#pinned-version-numbers
[editable package]: https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs
[unit tests]: https://en.wikipedia.org/wiki/Unit_testing
[dependency hell]: https://en.wikipedia.org/wiki/Dependency_hell
[containers]: https://en.wikipedia.org/wiki/OS-level_virtualisation
[virtualenvs]: https://virtualenv.pypa.io/en/latest/
[Anacondas]: https://www.anaconda.com/
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[flake8]: http://flake8.pycqa.org/en/latest/



