Welcome to the loggerFactory Documentation
==========================================

``loggerFactory`` include some commonly used logger. You can create a super easy to use logger in minimal code.

Example::

	import loggerFactory

	logger = loggerFactory.StreamOnlyLogger()
	logger.info("Some thing wrong!")


If you are using default log format ``%(asctime)s; %(levelname)-8s; %(message)s``, I provide a ``logfilter`` can help you search log info.


Example::

	from loggerFactory.logfilter import find

	result = find("log.txt", level="debug", message="ValueError",
		time_lower=None, time_upper=None, case_sensitive=False)
	result.dump("result.txt")
	print(result)


**Quick links**:

- `GitHub Homepage <https://github.com/MacHu-GWU/loggerFactory-project>`_
- `Online Documentation <https://github.com/MacHu-GWU/loggerFactory-project>`_
- `PyPI download <https://pypi.python.org/pypi/loggerFactory>`_
- `Install <install_>`_
- `Issue submit and feature request <https://github.com/MacHu-GWU/angora-project/issues>`_


.. _install:

Install
-------
``loggerFactory`` is released on PyPI, so all you need is:

.. code-block:: console

	$ pip install loggerFactory

To upgrade to latest version:

.. code-block:: console
	
	$ pip install --upgrade loggerFactory