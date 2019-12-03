# pydiner

Snakes on a plate.

## abstract

Pydiner is a [template]() for a generic Python project which:

- runs code in [containers]() which [self-destruct]()
- never installs software outside of its own Docker [images]()
- never uses or modifies other Pythons, [Anaconda](), or [virtualenvs]()
- updates `requirements.txt` with [pinned versions]() of installed packages

These rules are intended to minimize time spent in [dependency hell]().

## basics

To start a new project:

1. Generate a new repo [from this template]().
2. Edit the `Dockerfile` to choose a Python version and system packages.
3. Edit `requirements.txt` to choose Python packages to install with `pip`.
4. Open a terminal, `cd` to this folder, and run this command:
```sh
./kitchen help
```

### mise en python

Pydiner's [kitchen](kitchen) defines [shell functions]() for running [development containers]().
```sh
# Build a Docker image named pydiner:monty
./kitchen bake monty

# Update requirements.txt and rebuild pydiner:monty
./kitchen freeze monty

# Run Python in a container with $PWD mounted as /context
./kitchen serve monty python

# Run automated tests without mounting any folders
./kitchen runit monty python -m test

# Show which files were baked into the `pydiner:latest` image.
./kitchen runit latest tree

# Delete the image, its containers, and any leftovers
./kitchen eightysix monty
```
Typing `./kitchen` before each command is not necessary if the kitchen is [sourced]().

### baking images

Baking a `pydiner` image copies files from the the [build context]() into the image.

- Inside a container, these <q>baked-in</q> copies will appear in the `/context` folder.
- Each `pydiner` container gets its own independent copy of the `/context` folder.
- Edit `.dockerignore` to declare file patterns which should never be copied.
- Edit `Dockerfile` to choose which non-ignored files are copied into images.

Modifying a baked-in copy does **not** affect the original file.

### freezing packages

Freezing an image runs `pip freeze` and saves the output to `requirements.txt`.

- When a `pydiner` image is first baked, it uses `pip` to install requirements.
- Subsequent bakes often skip using `pip` if `requirements.txt` is unchanged.
- If versions are not [pinned](), then baking might not produce [reproducible builds]().
- Running `freeze` enables `pip` to install the same package versions every time.

Freezing **overwrites** anything that was in `requirements.txt`.

### serving with fresh files

Serving an image runs a new container with the current folder [mounted]() as `/context`.

- Images are [immutable](). Rebuilding is the only way to update baked-in files.
- For development work, rebuilding after every minor code edit can be impractical.
- Mounting folders gives a container read and write access to the original files.
- Any files baked into `/context` will be [shadowed]() by these <q>fresh</q> files.

Mounts are **not** copies. If a mounted file dies in a container, it dies in the real world.

## contents

Pydiner includes short examples of common project ingredients:

- [bin/](bin) contains executable scripts.
- [etc/](etc) contains configuration files.
- [src/](src) contains an importable [package]().
- [test/](test) is an [executable package]() which runs tests.
- [var/](var) contains files output by the script(s).

The [folder structure]() is loosely based on a C++ template from [hiltmon.com](https://hiltmon.com/blog/2013/07/03/a-simple-c-plus-plus-project-structure/).

## dependencies

Pydiner does not require Python. It has one dependency:

- Docker for [Linux]() or [Mac]() or [Windows]()

Windows users may need to edit the [kitchen]() script for [path compatibility]().

## examples

Remember to `cd` to this folder before running any `kitchen` commmands.

Bake, freeze, and serve `bash` with the default name `pydiner:latest`.
```sh
./kitchen bake && ./kitchen freeze && ./kitchen serve
```

Serving `bash` makes the container act like a real Linux machine.
```sh
root@pydiner:/context# which python
/usr/local/bin/python
root@pydiner:/context# grep PRETTY_NAME /etc/os-release
PRETTY_NAME="Debian GNU/Linux 10 (buster)"
root@pydiner:/context#
```

Run Python and `import pydiner` without hacking [sys.path]().
```sh
root@pydiner:/context# python
Python 3.7.4 (default, Jul 13 2019, 14:04:11)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pydiner
>>> pydiner.echo("Hello, World!")
2019-08-24 22:35:05 Hello, World!
>>> exit()
root@pydiner:/context#
```

Scripts in the project's `bin` folder are on the system [PATH]().
```sh
root@pydiner:/context# scrambled eggs
2019-12-03 21:36:55 Write derangements of 'eggs' to STDOUT
2019-12-03 21:36:55 10 expected
gesg
gseg
gesg
gseg
2019-12-03 21:36:55 4 found
2019-12-03 21:36:55 0:00:00.000116 time elapsed
root@pydiner:/context#
```

Save the output of a script.
```sh
root@pydiner:/context# scrambled -o var/dirtyfork.txt dirtyfork
2019-12-03 21:42:07 Write derangements of 'dirtyfork' to /context/var/dirtyfork.txt
2019-12-03 21:42:07 145152 expected
2019-12-03 21:42:07 101976 found
2019-12-03 21:42:07 0:00:00.632822 time elapsed
root@pydiner:/context#
```

Exit the container.
```sh
root@pydiner:/context# exit
```

Look inside the `var` folder. Is the output file real, or was it all just a dream?

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



