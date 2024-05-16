

from get_info import GetInfo
from config import config_file


def main():
    url = f"{config_file['DOMAIN']}{config_file['CATALOG']}"
    headers = {
        'Accept': '* / *',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept-Language': 'u-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
    }

    first_bs4_obj = GetInfo.get_bs4_obj(url, headers_=headers)

    for page in range(1, GetInfo.get_pagin(first_bs4_obj) + 1):
        url = f"{config_file['DOMAIN']}{config_file['CATALOG']}?page={page}"
        bs4_obj = GetInfo.get_bs4_obj(url, headers_=headers)

        for i in GetInfo.get_main_tags_a_in_first_page(bs4_obj):
            print(f'name - {GetInfo.get_name_product(i)}')
            href_prod = GetInfo.get_href_product(config_file['DOMAIN'], i)

            second_bs4_obj = GetInfo.get_bs4_obj(href_prod, headers_=headers)
            main_tag = GetInfo.get_main_tag_in_second_page(second_bs4_obj)
            print(GetInfo.get_articul(main_tag))


if __name__ == '__main__':
    main()
