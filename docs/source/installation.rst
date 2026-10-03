.. RadSSH documentation master file, created by
   sphinx-quickstart on Tue Jul 22 09:00:40 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Installation Guide
==================

The preferred way to install RadSSH is to use Python's `pip <http://pip.readthedocs.org/en/latest/>` utility. If you do not have administration (root) privileges to install Python packages into the system level directories, pip can install RadSSH to a `virtual environment <https://pypi.python.org/pypi/virtualenv>`.

Pip will handle the appropriate installation of RadSSH for your Python environment, either system-wide or virtual environment, and also utilitze the Python Package Index to install any missing dependencies. RadSSH currently requires `Paramiko <https://pypi.python.org/pypi/paramiko>` and `netaddr <https://pypi.python.org/pypi/netaddr>` packages, and pip will download these (and their dependencies) and install them if they are not already installed.


Installing from PyPI
--------------------

If you are installing to a virtual environment, be sure to activate the environment prior to running pip.

The python modules required for RadSSH will be installed by `pip` if they are not already present. Due to the upgrade of Paramiko's back end cryptography library, this may add some extra complexity to get all the necessary dependencies installed. The simplest way to avoid potential issues is to use your distributions own package manager (yum/apt/dnf) to pre-install paramiko (or python-paramiko) before installing RadSSH via `pip`.

Alternatively, attempt to install the Paramiko dependency Cryptography using ``pip install cryptography``. If it is able to install via the python prebuilt binary wheel package, that reduces a major source of complexity. See this `StackOverflow https://stackoverflow.com/questions/22073516/failed-to-install-python-cryptography-package-with-pip-and-setup-py` topic for additional details, and suggested solutions.

If you must resort to installation and compiling/linking from source, use your distribution package manager to install the core compilation packages:
 - Ubuntu needs some additional dependencies:
 ``sudo apt-get install libssl-dev python-dev libffi-dev -y``

 - CentOS requires additional depencies:
 ``sudo yum install -y python-devel libffi-devel openssl-devel``

Run the command (with sudo, if needed): ``pip install radssh``

This should download and install RadSSH from the internet, along with the dependency packages (as well as their own dependencies, etc.)


Installing from GitHub, with pip
--------------------------------

Run the command (with sudo, if needed): ``pip install git+https://github.com/radssh/radssh``

As with installation from PyPI, this will download and install (from source on GitHub) the latest version of RadSSH, along with its dependencies.


Installing from Developer Source
--------------------------------

If you have a local source tree, either from a developer checkout or from un-tarred source package, you can install RadSSH in a similar fashion, replacing the URL of the repository with the local directory. Alternatively, you can ``cd`` into the source directory and run ``pip install .``

Verifying the Install
=====================

Once installed, you should run ``python -m radssh`` as a diagnostic test. If successful, it will report the results of loading the RadSSH package and its dependencies, along with some details about the Python runtime environment and current host. It will also run some capacity checks for the system limitations on concurrent open files and execution threads. These upper limits, if listed, are a significant factor in how many concurrent connections RadSSH will be able to handle on your system.

Sample Output::

    (sample_env)[paul@pkapp2 ~]$ python -m radssh
    RadSSH Runtime Information Report
    Package RadSSH 1.3.0 from (/usr/lib/python3/site-packages/radssh/__init__.py)
      Using Paramiko  3.5.1 from /usr/lib/python3/site-packages/paramiko/__init__.py
      Using cryptography 48.0.0 from /usr/lib/python3/site-packages/cryptography/__init__.py
      Using netaddr 1.3.0 from /usr/lib/python3/site-packages/netaddr/__init__.py

    Python 3.10.12 (CPython)
    Running on Linux [pkapp2.risk.regn.net]
      Scientific Linux (6.8/Carbon)

    Checking runtime limits...
      System is able to open a maximum of 1021 concurrent files
        Attempting to open file #1022 reported (IOError(24, 'Too many open files'))
      File check completed in 0.005508 seconds

      System is able to run 866 concurrent threads
        Attempting to start thread #867 reported (error("can't start new thread",))
      Thread check completed in 0.450732 seconds

    End of runtime check
