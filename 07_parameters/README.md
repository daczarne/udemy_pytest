# Testing parametrization

Test parametrization allows us to run the same test but with different inputs, without having to copy-paste the test code. To pass parameters to our tests we use the `@mark.parametrize` decorator. The parameters of the test code itself are declared in the function and then used in the function body (as usual). We also need to pass the parameter names as strings to the decorator, followed by the parameter values, using some Python iterable (for example, a list of tuples). `pytest` will run the test as many times as there are values to iterate over.

``` python
@mark.parametrize(
  "tv_brand",
  [
    ("Samsung"),
    ("Sony"),
    ("Vizio")
  ]
)
def test_television_turns_on(tv_brand):
  print(f"{tv_brand} turns on as expected")
```

![parameters]("img/01_parameters.png)

One useful case is when we need to use different parameters on the fly (that is, when calling the test suite on the CLI).
