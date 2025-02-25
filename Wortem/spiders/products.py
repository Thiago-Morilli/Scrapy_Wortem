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
            callback=self.category
        )

    def category(self, response):
        for category in response.xpath('''//div[@id="__nuxt"]/div/div/div/div[@data-module-id="01J0632XE32YQB2V423H8PT8XN"]/div/div/header/div[@class="main-nav__container"]
/div/div/div/nav/div/ul/li/a/@href''').getall():
            if "/gaming" in category or "/informatica-e-acessorios" in category:
                link = (self.domains + category)
                yield scrapy.Request(
                    url=link,
                    method="GET",
                    headers=self.headers,
                    callback= self.parse
                )

    def parse(self, response):

        title = response.xpath('//section[@class="neu-02-bg category-links"]/div/div/div/article/a/h2[@class="category-links__text semibold"]/text()').getall()
        
        for links in response.xpath('//section[@class="neu-02-bg category-links"]/div/div/div/article/a/@href').getall():
            link = self.domains + links
            yield scrapy.Request(
                url=link,
                method="GET",
                headers=self.headers,
                callback=self.products
            )
            
    def products(self, response):
        link = response.xpath('//section[@class="listing-content gama__listing-content"]/div/div[@class="listing-content__list-container"]/li[@class="listing-content__card"]')
        print(link)
        
        