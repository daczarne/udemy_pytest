from pytest import mark

@mark.body
@mark.door
def test_body_functions_as_expected():
  assert True


@mark.body
def test_bumper():
  assert True
