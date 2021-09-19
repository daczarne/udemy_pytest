from pytest import mark


@mark.skip(reason = "Not a dev environment")
def test_environment_is_qa(app_config):
  base_url = app_config.base_url
  app_port = app_config.app_port
  assert base_url == "https://myqa-env.com"
  assert app_port == 80


def test_environment_is_dev(app_config):
  base_url = app_config.base_url
  app_port = app_config.app_port
  assert base_url == "https://mydev-env.com"
  assert app_port == 8080


@mark.xfail(reason = "Env was not Stg")
def test_environment_is_stg(app_config):
  base_url = app_config.base_url
  app_port = app_config.app_port
  assert base_url == "https://mystg-env.com"
  assert app_port == 80
