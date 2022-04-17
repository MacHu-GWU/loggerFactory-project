
.. image:: https://readthedocs.org/projects/loggerfactory/badge/?version=latest
    :target: https://loggerfactory.readthedocs.io
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/loggerFactory-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/loggerFactory-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/loggerFactory-project/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/loggerFactory-project

.. image:: https://img.shields.io/pypi/v/loggerFactory.svg
    :target: https://pypi.python.org/pypi/loggerFactory

.. image:: https://img.shields.io/pypi/l/loggerFactory.svg
    :target: https://pypi.python.org/pypi/loggerFactory

.. image:: https://img.shields.io/pypi/pyversions/loggerFactory.svg
    :target: https://pypi.python.org/pypi/loggerFactory

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/loggerFactory-project

------


.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://loggerFactory.readthedocs.io/index.html

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://loggerFactory.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
    :target: https://loggerFactory.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/loggerFactory-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/loggerFactory-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/loggerFactory-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/loggerFactory#files


Welcome to ``loggerFactory`` Documentation
==============================================================================

Construct **Stream Handler** and **File Handler** is so boring. ``loggerFactory`` include some commonly used logger out-of-the-box. You can create a super easy to use logger in **minimal code**.

Example:

.. code-block:: python

    import loggerFactory

    # log to console
    logger = loggerFactory.StreamOnlyLogger(rand_name=True)
    logger.warning("Some thing wrong!")

    # log to file
    # if name is not specified, a random name will be assigned
    logger = loggerFactory.SingleFileLogger(path="log.txt")
    logger.error("Fatal Error!")

    # file rotating
    logger = loggerFactory.FileRotatingLogger(path="log.txt")

    # time rotating
    logger = loggerFactory.TimeRotatingLogger(path="log.txt")


Use color and indent to format your print:

.. code-block:: python

    import loggerFactory

    logger = loggerFactory.BaseLogger()
    logger.show_in_red("Hello", indent=0)
    logger.show_in_blue("Hello", indent=1)
    logger.show_in_yellow("Hello", indent=2)
    logger.show_in_green("Hello", indent=3)
    logger.show_in_cyan("Hello", indent=4)
    logger.show_in_meganta("Hello", indent=5)

.. image:: https://user-images.githubusercontent.com/6800411/53650419-7ca86780-3c12-11e9-99c7-bf7baccb3fc4.png


If you are using default log format ``%(asctime)s; %(levelname)-8s; %(message)s``, a ``logfilter`` can help you search log info.

Example:

.. code-block:: python

    from loggerFactory import find

    result = find("log.txt",
        level="debug", message="ValueError",
        time_lower=None, time_upper=None,
        case_sensitive=False,
    )
    result.dump("result.txt")
    print(result)


.. _install:

Install
------------------------------------------------------------------------------

``loggerFactory`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install loggerFactory

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade loggerFactory