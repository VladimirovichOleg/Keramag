from get_info import GetInfoGeneralPage, GetResp, GetInfoIndividualPage
from config import config_file
from headers import different_headers


def main():
    url_start = f"{config_file['DOMAIN']}{config_file['CATALOG']}"
    first_bs4_obj = GetResp.get_bs4_obj_all_page(url_start, headers_=different_headers['headers_1'])

    for page in range(1, GetInfoGeneralPage.pagin(first_bs4_obj) + 1):
        url_in = f"{config_file['DOMAIN']}{config_file['CATALOG']}?page={page}"
        bs4_obj_all_general_page = GetResp.get_bs4_obj_all_page(url_in, headers_=different_headers['headers_1'])

        for a in GetInfoGeneralPage.main_tags_a(bs4_obj_all_general_page):
            href_individual_page = GetInfoGeneralPage.href_individual_page(config_file['DOMAIN'], a)
            bs4_obj_all_individual_page = GetResp.get_bs4_obj_all_page(href_individual_page, headers_=different_headers['headers_1'])

            print(GetInfoIndividualPage.name(bs4_obj_all_individual_page))



if __name__ == '__main__':
    main()
