from pytest import mark


@mark.web_pages
def test_amazon_launches(chrome_browser):
  chrome_browser.get("http://www.amazon.com")
  assert True
