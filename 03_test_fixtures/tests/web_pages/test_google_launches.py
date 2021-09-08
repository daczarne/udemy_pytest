from pytest import mark


@mark.web_pages
def test_google_launches(chrome_browser):
  chrome_browser.get("http://www.google.com")
  assert True
