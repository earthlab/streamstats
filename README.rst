StreamStats
===========


.. image:: https://img.shields.io/pypi/v/streamstats.svg
        :target: https://pypi.org/project/streamstats/

.. image:: https://readthedocs.org/projects/streamstats-python/badge/?version=latest
        :target: https://streamstats-python.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/earthlab/streamstats/branch/master/graph/badge.svg
        :target: https://app.codecov.io/gh/earthlab/streamstats

.. image:: https://static.mybinder.org/badge.svg
        :target: https://mybinder.org/v2/gh/earthlab/streamstats/master



Python package for interfacing with the USGS StreamStats API.

- Free software: MIT license
- Documentation: https://streamstats-python.readthedocs.io/en/latest/

Features
~~~~~~~~~

- Plot the GeoJSON of a watershed containing a spatial point in the United States
- Find available basin characteristics of an identified watershed
- Find the hydrologic unit code (HUC) of an identified watershed


View Example StreamStats Applications in Our Documentation Gallery
-------------------------------------------------------------------
Check out our `vignette gallery <https://streamstats-python.readthedocs.io/en/latest/gallery_vignettes/index.html>`_
for applied examples of using StreamStats.


Installation
~~~~~~~~~~~~~
Stable release
--------------
To install StreamStats via ``pip`` use:

.. code-block:: console

    $ pip install streamstats

This is the preferred method to install StreamStats, as it will always install
the most recent stable release. If you don't have `pip <https://pip.pypa.io/en/stable/>`_ installed, this
`Python installation guide <https://docs.python-guide.org/starting/installation/>`_
can guide you through the process.


Alternatively, StreamStats can be installed from the ``conda-forge`` repository
using `Conda <https://docs.conda.io/en/latest/>`__:

.. code-block:: console

    $ conda install -c conda-forge streamstats


From sources
------------
The sources for StreamStats can be downloaded from the `GitHub repository <https://github.com/earthlab/streamstats>`_ .

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/earthlab/streamstats

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


How to Contribute
~~~~~~~~~~~~~~~~~~
The steps to set up StreamStats for local development are as follows:

1. Fork the streastats repo on GitHub
2. Clone your fork locally:

.. code-block:: console

    $ git clone git://github.com:your_name_here/streamstats.git

3. Install your local copy into a new environment

If you have virutalenvwrapper installed:

.. code-block:: console

    $ mkvirtualenv streamstats


If you are using conda:

.. code-block:: console

    $ conda create -n streamstats python=3
    $ conda activate streamstats


Then intsall StreamStats:

.. code-block:: console

    $ cd streamstats/
    $ pip install -r requirements.txt
    $ pip install -r requirements_dev.txt
    $ install -e .


4. Create a branch for local development:

.. code-block:: console

    $ git checkout -b name-of-your-bugfix/feature

Now you can make your changes locally


5. When your changes are complete, check that your changes pass flake8 and the tests,
including other Python versions with tox:

.. code-block:: console

    $ pytest
    $ tox


6. Commit your changes and push your branch to GitHub:

.. code-block:: console

    $ git add
    $ git commit -m "Your detailed description of your changes"
    $ git push origin name-of-your-bugfix/feature


7. Submit a pull request through the GitHub website



We welcome and greatly appreciate contributions to StreamStats! The best way to
send feedback is to file an issue at https://github.com/earthlab/streamstats/issues.
To read more on ways to contribute and pull requests, click `here <https://streamstats-python.readthedocs.io/en/latest/contributing.html>`_.


Credits
~~~~~~~~
Development Lead
-----------------
- `Maxwell B. Joseph <https://github.com/mbjoseph>`_

Contributors
-------------
- `Scott Eilerman <https://github.com/seilerman>`_
- `Leah Wasser <https://github.com/lwasser>`_
- `Jeremy Diaz <https://github.com/jdiaz4302>`_
- `Nate Mietkiewicz <https://github.com/natemietk>`_
- `Ally Fitts <https://github.com/aefitts>`_


This package was created with `Cookiecutter <https://github.com/cookiecutter/cookiecutter>`_.
