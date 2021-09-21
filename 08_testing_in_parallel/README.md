# Testing in parallel

Running tests in parallel makes our suite much faster. To do so, we just need to install the `pytest-xdist` add-on package with

``` bash
pipenv install pytest-xdist
```

With this new add on we can now add the `-n#` flag to our CLI command and specify the number of threads to be used for running the tests.

``` bash
pytest -v -n4
```

When we run this command, `pytest-xdist` will first have to do some setup. This means that using parallel processing might not reduce time if the test is very small (and might even increase it). But in general, complete testing suites are large enough that it is worth it.

![no parallel](img/01_no_parallel.png)

![parallel](img/02_parallel.png)
