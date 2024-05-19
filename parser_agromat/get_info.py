from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.error import URLError


class GetInfo:
    @staticmethod
    def get_bs4_obj_all_page(url: str, headers_: dict) -> object | None:
        try:
            resp = Request(url, headers=headers_)
            down_html = urlopen(resp)
            return BeautifulSoup(down_html, 'html.parser')
        except HTTPError:
            print("HTTP Error")
            return None
        except URLError:
            print("URL Error")
            return None

    @staticmethod
    def get_main_tags_a_on_general_page(bs4_obj) -> object | str:
        return bs4_obj.find(name='div', attrs={'class': 'list-content js-cat _js-ga_view-list_catalog'}).find_all('a')

    @staticmethod
    def get_main_tag_on_individual_page(bs4_obj): # div : class - product-main
        return bs4_obj.find('div', {'class': 'product-main'})

    @staticmethod
    def get_name_product_on_general_page(bs4_obj):
        return bs4_obj.find('span', {'class': '_js-analytics'}).get("data-name")

    @staticmethod
    def get_href_product_individual_page(main_address, bs4_obj):
        return f'{main_address}{bs4_obj.get("href")}'

    @staticmethod
    def get_discount_individual_page(bs4_obj):
        try:
            return (bs4_obj.find('div', {'class': 'product-images'}).
                    find('div', {'class': 'product-images__wrapper'}).find('div', {'class': 'swiper main-slider'}).
                    find('div', {'class': 'goods-label'}).find('span').text)
        except:
            return 'No discount'

    @staticmethod
    def get_in_stock_individual_page(bs4_obj):
        return bs4_obj.find('div', {'class': 'bottom'}).find('div', {'class': 'cart-goods-alert'}).text

    @staticmethod
    def get_now_price(bs4_obj) -> dict:
        price = {}
        try:
            price['price_now'] = (bs4_obj.find('div', {'class': 'bottom'}).find('div', {'class': 'price'}).
                                  find('span').text)
            price['old_price'] = (bs4_obj.find('div', {'class': 'bottom'}).find('div', {'class': 'old-price_wrap'}).
                                  find('span', {'class': 'old-price'}).text)
            price['discount'] = (bs4_obj.find('div', {'class': 'bottom'}).find('div', {'class': 'old-price_wrap'}).
                                 find('span', {'class': 'discount'}).text)
            return price
        except:
            price['old_price'] = bs4_obj.find('div', {'class': 'bottom'}).find('div', {'class': 'price'}).find('span').text
            price['discount'] = 0
            return price

    @staticmethod
    def get_size(bs4_obj) -> str:
        tag_div = (bs4_obj.find('div', {'class': 'bottom'}).find('div', {'class': 'params-list'}).
                find_all('div', {'class': 'params-list__item'}))
        tag_p = tag_div[0].find_all('p')
        return tag_p[1].text

    @staticmethod
    def get_country(bs4_obj):
        tag_div = (bs4_obj.find('div', {'class': 'bottom'}).find('div', {'class': 'params-list'}).
                   find_all('div', {'class': 'params-list__item'}))
        tag_p = tag_div[2].find_all('p')
        return tag_p[1].text

    @staticmethod
    def get_unit_of_value(bs4_obj):
        return bs4_obj.find('div', {'class': 'price'}).text[-3:]

    @staticmethod
    def get_href_small_picture(bs4_obj):
        return (bs4_obj.find('div', {'class': 'top'}).find('div', {'class': 'swiper'}).find('div', {'class': 'swiper-wrapper'}).
                find('div', {'class':'swiper-slide'}).find('picture').find('img').get('src'))

    @staticmethod
    def get_href_picture_on_individual_page(bs4_obj):
        return bs4_obj.find('div', {'class': 'swiper-slide'}).find('picture').find('img').get('src')

    @staticmethod
    def get_articul_on_individual_page(bs4_obj):
        return (bs4_obj.find('div', {'class': 'product-info'}).find('div', {'class': 'brief-characteristics'})
                .find('div', {'class': 'brief-characteristics__item'}).find('span').text)

    @staticmethod
    def get_pagin_on_general_pae(bs4_obj) -> int:
        tags_a = bs4_obj.find('div', {'class': 'pagin-content'}).find_all('a')
        tag_a = tags_a[3].text
        return int(tag_a)
