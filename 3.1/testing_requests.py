from parsel import Selector
import requests

response = requests.get("http://books.toscrape.com/")
selector = Selector(text=response.text)
print(selector)

titles = selector.css(".product_pod h3 a::attr(title)").getall()

prices = selector.css(".product_price .price_color::text").getall()

for product in selector.css(".product_pad"):
    title = product.css("h3 a::attr(title)").get()
    price = product.css(".price_color::text").get()
    print(title, price)