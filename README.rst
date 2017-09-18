pyworkplace
###########

|Python| |Build Status| |Wercker| |Pyup| |GitHub issues| |license|

:Version: 0.0.0
:Web: https://github.com/labpositiva/pyworkplace
:Download: http://github.com/labpositiva/pyworkplace
:Source: http://github.com/labpositiva/pyworkplace
:Keywords: pyworkplace

.. contents:: Table of Contents:
    :local:

Pyworkplace Wrapper for workplace

Features
========

- Task

Requirements:
=============

List of applications:

- `Python 3.6.1`_
- `Docker`_
- `Docker Compose`_

Quick Start
===========

- Fork this repository

Usage
-----

- Install dependences

.. code-block:: bash

  λ make setup

- Build images

.. code-block:: bash

  λ make build

Actions:
========

.. code-block:: bash

  λ make
    ༼ つ ◕_◕ ༽つ Commands
      build                Build docker container by env
      clean                clean Files compiled
      documentation        Make Documentation
      down                 remove containers docker by env
      environment          Make environment for developer
      env                  Show envs available
      install              Install with var env Dependences
      generate             Generate pdf
      list                 List of current active services by env
      lint                 Make Lint Files
      test                 make test
      up                   Up application by env
      restart              Reload services
      ssh                  Connect to container
      stop                 stop containers docker by env
      setup                Install dependences initial
      verify_network       Verify network
      help                 Show help text

License
=======

MIT

Changelog
=========

Please see `CHANGELOG`_ for more information what
has changed recently.

Contributing
============

Please see `CONTRIBUTING`_ for details.

Credits
=======

-  `author`_
-  `contributors`_

Made with ♥️and ☕️by `author`_ and `company`_.

.. |Pyup| image:: https://pyup.io/repos/github/labpositiva/pyworkplace/shield.svg
     :target: https://pyup.io/repos/github/labpositiva/pyworkplace/
     :alt: Updates
.. |Python| image:: https://pyup.io/repos/github/labpositiva/pyworkplace/python-3-shield.svg
     :target: https://pyup.io/repos/github/labpositiva/pyworkplace/
     :alt: Python 3
.. |Build Status| image:: https://travis-ci.org/labpositiva/pyworkplace.svg
   :target: https://travis-ci.org/labpositiva/pyworkplace
.. |GitHub issues| image:: https://img.shields.io/github/issues/labpositiva/pyworkplace.svg
   :target: https://github.com/labpositiva/pyworkplace/issues
.. |Wercker| image::
             https://app.wercker.com/status/642f4288274e91f723ec2ecf7c03966c/s/ 'wercker status'
  :target: https://app.wercker.com/project/byKey/642f4288274e91f723ec2ecf7c03966c
  :alt: wercker status
.. |license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square
  :target: LICENSE
  :alt: License

.. Links
.. _`changelog`: CHANGELOG.rst
.. _`contributors`: AUTHORS
.. _`contributing`: CONTRIBUTING.rst


.. _`company`: https://github.com/labpositivatd
.. _`author`: https://github.com/luismayta

.. dependences
.. _Python 3.6.1: https://www.python.org/downloads/release/python-361
.. _Docker: https://www.docker.com/
.. _Docker Compose: https://docs.docker.com/compose/
