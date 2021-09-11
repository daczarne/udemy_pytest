# Reporting results

If we want to generate a test report we can use the `pytest-html` package. This package will render an HTML report of the test results. To use it (once installed in the environment), we run

``` bash
pytest --html="root/to/my/results/results.html"
```

This will generate a results HTML file in the specified directory with all the important information about the test run and the results generated. If the path specifies a directory that doesn't exist `pytest` will create it when outputting results.

The problem with the HTML fill is that it's only accessible in the machine in which it was run. To generate an output that we can share (via loading it to plugins), we need to use XML output. To do so we run:

``` bash
pytest --junitxml="root/to/my/results/results.xml"
```

The output is XML and therefore, not human readable. If you are using a CI-CD tool like Jenkins you can add the build

``` bash
cd tests
pytest --junitxml="BUILD_${BUILD_NUMBER}_results.xml"
```

and select the Post-build action: *Publish JUnit test result report*. You can then check the rest results in the Jenkins *Test Result* plugin.
