
from get_info import GetInfo as g_i

MAIN_URL = 'https://www.agromat.ua'
NEXT_STAGE_URL = '/keramichna-plitka-ta-keramogranit/'
PAGE = '?page=1'
URL = f"{MAIN_URL}{NEXT_STAGE_URL}{PAGE}"

def main():
    bs4_obj = g_i.get_bs4_obj(URL)
    for i in g_i.get_main_tags_a_in_first_page(bs4_obj):
        second_URL = g_i.get_href_product(MAIN_URL, i)

        second_bs4_obj = g_i.get_bs4_obj(second_URL)
        main_tag = g_i.get_main_tag_in_second_page(second_bs4_obj)
        print(g_i.get_articul(main_tag))
        """picture = urlopen(f"{first.get_href_picture_in_next_pages(main_tag)}")
        with open(str(first.get_href_picture_in_next_pages(main_tag).replace('/', '_')[-30:]), 'wb') as file:
            file.write(picture.read())
        time.sleep(1)"""


if __name__ == '__main__':
    main()
