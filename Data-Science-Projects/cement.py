import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#dataset
data = pd.DataFrame()

data['Country'] = ''
data['Store'] = ''
data['Brand'] = ''
data['Product'] = ''
data['Cement Type'] = ''
data['Kg Price'] = ''
data['Bag Price'] = ''
data['Bag Price USD'] = ''
data['Bulk Price'] = ''
data['VAT'] = ''
data['Price w/o VAT'] = ''
data['Distributor Share'] = ''
data['Transportation'] = ''
data['Ex-Factory Price'] = ''
data['Notes'] = ''
data['Web Link'] = ''

#source & vars
brand = ['Blue Circle ', 'Hanson ']

test_links = []

product_links = ['https://www.diy.com/departments/blue-circle-multipurpose-cement-25kg-bag/35715_BQ.prd',
                 'https://www.diy.com/departments/blue-circle-mastercrete-cement-25kg-bag/35720_BQ.prd',
                 'https://www.diy.com/departments/blue-circle-extra-rapid-cement-25kg-bag/35718_BQ.prd',
                 'https://www.trade-point.co.uk/departments/blue-circle-mastercrete-cement-25kg-bag/35720_TP.prd',
                 'https://www.trade-point.co.uk/departments/blue-circle-multipurpose-cement-25kg-bag/35715_TP.prd',
                 'https://www.trade-point.co.uk/departments/blue-circle-extra-rapid-cement-25kg-bag/35718_TP.prd',

                 ]

travis_perkins_links = ['https://www.travisperkins.co.uk/cement/obrien-all-purpose-cement-25kg/p/779612']

jewson_links = ['https://www.jewson.co.uk/p/hanson-general-purpose-cement-25kg-paper-bag-CCASCEM2',
                'https://www.jewson.co.uk/p/hanson-multicem-cement-25kg-plastic-bag-CCASTMCP',
                'https://www.jewson.co.uk/p/hanson-quickcem-quick-setting-cement-25kg-plastic-bag-CCASQCEM',
                'https://www.jewson.co.uk/p/hanson-multicem-cement-25kg-tough-paper-bag-CCASTMC2',
                'https://www.jewson.co.uk/p/hanson-white-cement-25kg-paper-bag-CCASWHIT'
                ]

wickes_links = ['https://www.wickes.co.uk/Blue-Circle-General-Purpose-Cement---25kg/p/224661',
                'https://www.wickes.co.uk/Blue-Circle-Mastercrete-Cement---25kg/p/154100'
                ]

def url_parser(product_links):

    for link in product_links:

        price_info = []
        product_country = ''
        product_store = ''
        product_bran = ''
        product_cat = ''
        product_code = ''
        product_ppkg = ''
        product_price = ''

        #get product data from url
        product_url = requests.get(link).text
        parsed_product = bs(product_url, 'html.parser')

        #parse specific data
        product_price = parsed_product.find_all("div", {'class': "_5d34bd7a" })
        product_title = str(parsed_product.title.get_text())
        product_code = parsed_product.find_all(lambda tag: tag.name == 'td' and 'CEM' in tag.text)
        product_country = parsed_product.find_all(lambda tag: tag.name == 'script' and '"country":' in tag.text)

        #data cleaning
        if (len(str(product_code)) > 2):

            product_code = str(product_code).split('>')
            temp_val = product_code[1].split('<')
            product_code = temp_val[0]

        if (len(str(product_country)) > 2):
            temp_val2 = str(product_country).split('"store":')
            temp_val2 = temp_val2[1].split('"country":')
            temp_val2 = temp_val2[1].split(',')
            if temp_val2[0][0] and temp_val2[0][-1]:
                temp_val2[0] = temp_val2[0][1:-1]
            product_country = temp_val2[0]

        if (len(str(product_title)) > 2):
            for i in brand:
                if i in product_title:
                    product_title = product_title.split(i)
                    product_brand = i
                    temp_val3 = product_title[1].split(' |')
                    product_cat = temp_val3[0]
                    break

        if (len(str(product_price)) > 2):
            for j in product_price:
                product_price = str(j).split('>')
                temp_val4 = product_price[1].split('<')
                price_info.append(temp_val4[0])

            product_price = str(price_info[0]) + " " + str(price_info[1])
            product_ppkg = str(price_info[2]) + " " + str(price_info[1])


        #store for B&Q
        if (len(str(product_title)) > 2):
            temp_store = str(product_title).split('| ')
            product_store = temp_store[1][ 0 : (len(str(temp_store[1])) - 2)]

        #dataset manipulation
        bag_price_usd = ''
        bulk_price = ''
        vat = ''
        price_wO_vat= ''
        dist_share = ''
        transport = ''
        exFac_price = ''
        notes = ''

        data_vals = [product_country, product_store, product_brand, product_cat,
                                    product_code, product_ppkg, product_price]

        for val in range(len(data_vals)):
            if str(data_vals[val]) == '[]':
                data_vals[val] = ''

        data.loc[len(data.index)] =[data_vals[0], data_vals[1], data_vals[2], data_vals[3], data_vals[4], data_vals[5], data_vals[6],
                                    bag_price_usd, bulk_price, vat, price_wO_vat, dist_share, transport, exFac_price, notes, link ]

    return data

def jewson_url_parser(jewson_links):

    for link in jewson_links:

        price_info = []
        product_code_check = True

        #get product data from url
        product_url = requests.get(link).text
        parsed_product = bs(product_url, 'html.parser')

        #parse specific data
        product_price = parsed_product.find("span", {'class': "price__value" })
        product_title = str(parsed_product.title.get_text()).strip()
        product_code_2 = parsed_product.find(lambda tag: tag.name == 'li' and 'Conforms to ' in tag.text)

        if product_code_2 == None:
            product_code_check = False
            product_code = ''

        product_country = parsed_product.find_all("td", {'class': "table__cell" })
        product_store = parsed_product.find_all("span", {'id': "submenutitle" })


        #data cleaning
        if product_code_check:
            if (len(str(product_code_2)) > 2):

                product_code_2 = str(product_code_2).split('Conforms to ')
                product_code_2 = product_code_2[1].split('<')
                product_code_2 = product_code_2[0]

                product_code = product_code_2

        if (len(str(product_country)) > 2):
            product_country_temp = str(product_country).split('Country Of Origin</td>, <td class="table__cell">')
            product_country_temp = product_country_temp[1].strip()
            product_country_temp = product_country_temp.split('<')[0].strip()
            product_country = product_country_temp

        if (len(str(product_title)) > 2):
            for i in brand:
                if i in product_title:
                    product_title = product_title.split(i)
                    product_brand = i
                    product_cat = product_title[1]
                    break


        if (len(str(product_price)) > 2):
            product_currency = product_price
            product_price = str(product_price).split('"price">')
            product_price = product_price[1].split('<')
            product_price = product_price[0]

            product_currency = str(product_currency).split('"priceCurrency">')
            product_currency = product_currency[1].split('<')
            product_currency = product_currency[0]

            product_weight = product_cat[len(product_cat) - 4: len(product_cat) - 2]
            product_ppkg_temp = float(product_price) / float(product_weight)
            product_ppkg_temp = round(product_ppkg_temp,2)

            product_price = str(product_price) + " " + str(product_currency)
            product_ppkg = str(product_ppkg_temp) + " " + str(product_currency)

        #store

        if (len(str(product_store)) > 2):
            product_store = str(product_store).split('More from ')[1].split('<')[0]


        #dataset manipulation
        bag_price_usd = ''
        bulk_price = ''
        vat = ''
        price_wO_vat= ''
        dist_share = ''
        transport = ''
        exFac_price = ''
        notes = ''

        data_vals = [product_country, product_store, product_brand, product_cat,
                                    product_code, product_ppkg, product_price]

        for val in range(len(data_vals)):
            if str(data_vals[val]) == '[]':
                data_vals[val] = ''

        data.loc[len(data.index)] =[data_vals[0], data_vals[1], data_vals[2], data_vals[3], data_vals[4], data_vals[5], data_vals[6],
                                    bag_price_usd, bulk_price, vat, price_wO_vat, dist_share, transport, exFac_price, notes, link ]

    return data

def wickes_url_parser(wickes_links):

    for link in wickes_links:

        price_info = []
        product_country = ''
        product_store = ''
        product_bran = ''
        product_cat = ''
        product_code = ''
        product_ppkg = ''
        product_price = ''

        #get product data from url
        product_url = requests.get(link).text
        parsed_product = bs(product_url, 'html.parser')

        #parse specific data
        product_price = parsed_product.find_all("div", {'class': "main-price__value pdp-price__new-price" })
        product_title = str(parsed_product.title.get_text())
        product_code = parsed_product.find_all(lambda tag: tag.name == 'li' and 'Certifications Met:' in tag.text)
        product_country = parsed_product.find_all(lambda tag: tag.name == 'script' and '"country":' in tag.text)

        #data cleaning
        if (len(str(product_code)) > 2):
            product_code = str(product_code).split('</strong>')[1].strip()
            temp_val = product_code.split('<')
            product_code = temp_val[0]

        if (len(str(product_country)) > 2):
            temp_val2 = str(product_country).split('"store":')
            temp_val2 = temp_val2[1].split('"country":')
            temp_val2 = temp_val2[1].split(',')
            product_country = temp_val2[0]

        if (len(str(product_title)) > 2):
            for i in brand:
                if i in product_title:
                    product_title = product_title.split(i)
                    product_brand = i
                    temp_val3 = product_title[1].split(' |')
                    product_cat = temp_val3[0]
                    break

        if (len(str(product_price)) > 2):
            for j in product_price:
                product_price = str(j).split('>')
                temp_val4 = product_price[1].split('\n\t\t')[1].split('<')
                product_price = temp_val4[0]
                price_info.append(product_price)

            product_price = str(price_info[0][1:])

            product_weight = product_cat[len(product_cat) - 4: len(product_cat) - 2]
            product_ppkg_temp = float(product_price) / float(product_weight)
            product_ppkg_temp = round(product_ppkg_temp, 2)

            product_price = str(price_info[0][1:]) + " " + str(price_info[0][0])
            product_ppkg = str(product_ppkg_temp) + " " + str(price_info[0][0])


        #store for B&Q
        if (len(str(product_title)) > 2):
            temp_store = str(product_title).split('| ')
            product_store = temp_store[1][ 0 : (len(str(temp_store[1])) - 2)]

        #dataset manipulation
        bag_price_usd = ''
        bulk_price = ''
        vat = ''
        price_wO_vat= ''
        dist_share = ''
        transport = ''
        exFac_price = ''
        notes = ''

        data_vals = [product_country, product_store, product_brand, product_cat,
                                    product_code, product_ppkg, product_price]

        for val in range(len(data_vals)):
            if str(data_vals[val]) == '[]':
                data_vals[val] = ''

        data.loc[len(data.index)] =[data_vals[0], data_vals[1], data_vals[2], data_vals[3], data_vals[4], data_vals[5], data_vals[6],
                                    bag_price_usd, bulk_price, vat, price_wO_vat, dist_share, transport, exFac_price, notes, link ]

    return data

url_parser(product_links)
jewson_url_parser(jewson_links)
wickes_url_parser(wickes_links)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
     print(data)


