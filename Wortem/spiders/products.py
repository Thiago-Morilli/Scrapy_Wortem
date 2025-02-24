import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    domains = "https://www.worten.pt"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}     

    def start_requests(self):

        yield scrapy.Request(
            url=self.domains,
            method="GET",
            headers=self.headers,
            callback=self.parse
        )

    def parse(self, response):
        for category in response.xpath('''//div[@id="__nuxt"]/div/div/div/div[@data-module-id="01J0632XE32YQB2V423H8PT8XN"]/div/div/header/div[@class="main-nav__container"]
/div/div/div/nav/div/ul/li/a/@href''').getall():
            if "/gaming" in category or "/informatica-e-acessorios" in category:
                link = (self.domains + category)
                yield scrapy.Request(
                    url=link,
                    method="GET",
                    headers=self.headers,
                    callback= self.products
                )

    def products(self, response):

        link = response.xpath('//*[@id="__nuxt"]/div/div/div[2]/div[10]/div/section/div/div/div[1]/article[1]/a')
        print(link)