# pydiner

Snakes on a plate.

## abstract

Pydiner is a [template]() for a generic Python project which:

- runs code in [containers]() which [self-destruct]() after exiting
- never modifies other Pythons, [Anaconda](), or [virtualenvs]()
- never installs anything outside of its own Docker [images]()
- declares all required Python packages in `requirements.txt`
- declares all required system packages in a `Dockerfile`

These rules are intended to minimize time spent in [dependency hell]().

## basics

To start a new project:

1. Generate a new repo [from this template]().
2. Delete files you don't need. Add any files you want.
3. Edit the `Dockerfile` to choose a Python version and system packages.
4. Edit `requirements.txt` to choose Python packages to install with `pip`.
5. Run `./kitchen help` to see available commands and Docker objects.

Remember to `cd` to this folder before running `kitchen` commands.

### prepare the kitchen

The `kitchen` script contains [shell functions]() for running [dev containers]().

- `./kitchen bake` builds (or rebuilds) a `pydiner:latest` Docker image.
- `./kitchen freeze` updates `requirements.txt` with [pinned versions]().
- `./kitchen serve` runs a `pydiner` container and [mounts]() the current folder.

Typing `./kitchen` is not necessary if the `kitchen` script is [sourced]().

### bake an image

Processes in a `pydiner` container have two ways to access files on your computer:

- `./kitchen bake` copies the [build context]() into an image's `/context` folder.
- `./kitchen serve` [mounts]() the current working folder as `/context`.

Docker ignores files which match patterns in the [.dockerignore](.dockerignore) file.
Everything else in this repository is copied into each `pydiner` image.
Each `pydiner` container gets an independent copy of these <q>baked-in</q> files.
Containers can read, write and delete their own `/context` files without fear of damaging the originals.

Files baked into an image do **not** update themselves when the originals change.

### freeze packages

Each time you bake an image, Docker checks if `requirements.txt` has changed.
If so, then it uses [pip]() to install all packages and their dependencies.
(See the [Dockerfile](Dockerfile) for details.)

Run `./kitchen freeze` if you need to know *exactly* what was installed,
or you want [reproducible builds]() for your project.
Docker will rebuild the image, run `pip freeze`, and save the output.

Freezing **overwrites** anything that was in `requirements.txt`.

### serve with fresh files

Images are [immutable]().
Files copied into images do not update when the originals change.

Run `./kitchen serve` to run a container with access to the original files.
Docker will [bind mount]() the current working folder as `/context`.
Files <q>baked</q> into `/context` will be [shadowed]() by these <q>fresh</q> files.


Mounted files are **not** copies.
If a mounted file dies in a container, it dies in the real world.


### nuke the entire site from orbit

Run `exit` or hit *CTRL-D* to exit a container.

Pydiner containers [self-destruct]() when they exit. It's the only way to be sure.


## contents

### `bin` scripts
### `etc` config files
### `src/pydiner` package
### `test` package
automated [unit tests] for the `pydiner` package

[Hiltmon](https://hiltmon.com/blog/2013/07/03/a-simple-c-plus-plus-project-structure/)

## dependencies

- Docker for [Linux] or [Mac] or [Windows]

Windows users might need to edit the [kitchen] script for [path compatibility].

## examples


## UNDER CONSTRUCTION


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

### think inside the box

For the most part, what happens inside a container stays inside a container.
You can move fast and break things with no lasting consequences.
After you `exit`, Docker cleans up your mess by destroying the container.

There are **three dangerous exceptions**:

1. The `/context` folder is your real project folder. It is *not* a copy.
2. On Linux machines, containers have [root access] to your project folder.
3. Containers can [connect to the internet] by default.

If this is a problem, then see the [faq] for workarounds.

|                               |                                       |
|-------------------------------|---------------------------------------|
| show [kitchen] help           | `./kitchen help`                      |
| build a Docker image          | `./kitchen bake`                      |
| show all Docker objects       | `./kitchen carte`                     |
| update [requirements.txt]     | `./kitchen freeze`                    |
| start an interactive shell    | `./kitchen serve`                     |
| start an interactive Python   | `./kitchen serve python`              |
| run [bin/soda] with arguments | `./kitchen serve soda --fizz=3 0 10`  |
| debug [bin/cake] with [pdb]   | `./kitchen debug cake`               |
| delete image and leftovers    | `./kitchen eighty_six`                |


## faq

### How do I install PyDiner?

Don't. Use it as a [template].

### Do I have to run as root inside a container?

Not if you edit the [Dockerfile] to create another user.
See the [Dockerfile reference] for details.

### What is the `.dockerignore` file?

Files and folders listed in `.dockerignore` are *not* copied into the `pydiner` image.

- Secrets (passwords, SSH keys, etc.) can be read by anyone with access to the image.
- Large files and `.git` folders waste disk space and build time.
-

Note that files outside the [build context] cannot be baked into an image.
The `kitchen` script uses your current working directory as context.

### Can I run containers in the background?

The `kitchen` script only runs [interactive] containers.
See the [Docker run reference] for other options.

### What testing framework does `pydiner` use?

None. The [test] folder is an [executable package]. To run all tests:
```bash
# from the top-level repo folder
./kitchen serve latest python -m test

# from inside a container
python -m test
```
When possible, `pydiner` tries to follow [pytest] conventions.

### What logging framework does `pydiner` use?

None. Log messages are [streamed](https://12factor.net/logs) and never saved.
The `pydiner.achtung()` method prints errors to [STDERR]().
The `pydiner.echo()` method prints other logs to [STDOUT]().

### What are some other Python project templates?

- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [PyPA tutorial](https://packaging.python.org/tutorials/packaging-projects/)
- [PyPA sample project](https://github.com/pypa/sampleproject)
- [pythonizr.com](https://pythonizr.com/)
- [python-boilerplate.com](https://www.python-boilerplate.com)



## UNDER CONSTRUCTION



### Can I use `setup.py` instead of `PYTHONPATH`?
### What files can I access from inside a container?


opt-in permissions
self-documenting
explicit

### Why can't the container see my files?

- `serve` [mounts] the current working directory.
  - Containers can read, write, and execute all files in that folder.
  - Symlinks are not guaranteed to work inside the container.

- `runit` mounts no folders.
  - Containers cannot access files outside the `pydiner` image.

See the [Docker storage docs] for more information.


### Why not use `virtualenv`, `pyenv`, ... ?

The author prefers containers because:

- There is no [hidden state] except Docker itself.
- The `python` command never calls the wrong Python.
- System requirements are stated explicitly in the [Dockerfile].
- Files cannot be modified unless they are explicitly [mounted].
- Leftovers from [uninstalled packages] do not survive container deletion.
- Packages not listed in [requirements.txt] or [setup.py] are not installed.
- Malfunctioning containers are easily [nuked from orbit] and replaced.

PyDiner can be used with a [virtualenv] if you prefer. For example:
```bash
cd path/to/wherever/you/put/pydiner

# Delete all the Docker stuff if you want to
rm .dockerignore Dockerfile kitchen

# Create a virtualenv in the pydiner/.venv folder
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install --editable .
.venv/bin/pip install --requirement requirements.txt
.venv/bin/pip freeze > requirements.txt

# Use the new virtualenv to run the cake script
.venv/bin/python bin/cake
```



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



