.. image:: https://travis-ci.org/MacHu-GWU/loggerFactory-project.svg?branch=master
    :target: https://travis-ci.org/MacHu-GWU/loggerFactory-project?branch=master

.. image:: https://codecov.io/gh/MacHu-GWU/loggerFactory-project/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/MacHu-GWU/loggerFactory-project

.. image:: https://img.shields.io/pypi/v/loggerFactory.svg
    :target: https://pypi.python.org/pypi/loggerFactory

.. image:: https://img.shields.io/pypi/l/loggerFactory.svg
    :target: https://pypi.python.org/pypi/loggerFactory

.. image:: https://img.shields.io/pypi/pyversions/loggerFactory.svg
    :target: https://pypi.python.org/pypi/loggerFactory

.. image:: https://img.shields.io/badge/Star_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/loggerFactory-project


Welcome to ``loggerFactory`` Documentation
==============================================================================

``loggerFactory`` include some commonly used logger. You can create a super easy to use logger in minimal code.

Example::

    import loggerFactory

    # log to console
    logger = loggerFactory.StreamOnlyLogger(name="stream_only")
    logger.warning("Some thing wrong!")

    # log to file
    # if name is not specified, a random name will be assigned
    logger = loggerFactory.SingleFileLogger(path="log.txt")
    logger.error("Fatal Error!")

    # file rotating
    logger = loggerFactory.FileRotatingLogger(path="log.txt")

    # time rotating
    logger = loggerFactory.TimeRotatingLogger(path="log.txt")


If you are using default log format ``%(asctime)s; %(levelname)-8s; %(message)s``, a ``logfilter`` can help you search log info.

Example::

    from loggerFactory import find

    result = find("log.txt",
        level="debug", message="ValueError",
        time_lower=None, time_upper=None,
        case_sensitive=False,
    )
    result.dump("result.txt")
    print(result)


Quick Links
------------------------------------------------------------------------------

- .. image:: https://img.shields.io/badge/Link-Document-red.svg
      :target: http://www.wbh-doc.com.s3.amazonaws.com/loggerFactory/index.html

- .. image:: https://img.shields.io/badge/Link-API_Reference_and_Source_Code-red.svg
      :target: http://www.wbh-doc.com.s3.amazonaws.com/loggerFactory/py-modindex.html

- .. image:: https://img.shields.io/badge/Link-Install-red.svg
      :target: `install`_

- .. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: https://github.com/MacHu-GWU/loggerFactory-project

- .. image:: https://img.shields.io/badge/Link-Submit_Issue_and_Feature_Request-blue.svg
      :target: https://github.com/MacHu-GWU/loggerFactory-project/issues

- .. image:: https://img.shields.io/badge/Link-Download-blue.svg
      :target: https://pypi.python.org/pypi/loggerFactory#downloads


.. _install:

Install
------------------------------------------------------------------------------

``loggerFactory`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install loggerFactory

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade loggerFactory