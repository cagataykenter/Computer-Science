import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome web driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.page_load_strategy = 'none'
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)

# dataframe
data = pd.DataFrame(
    columns=['Country', 'Store', 'Brand', 'Product', 'Cement Type', 'Kg Price', 'Bag Price', 'Bag Price USD',
             'Bulk Price', 'VAT', 'Price w/o VAT', 'Distributor Share', 'Transportation', 'Ex-Factory Price',
             'Notes', 'Web Link'])

# website links
diy_tradePoint_links = ['https://www.diy.com/departments/blue-circle-multipurpose-cement-25kg-bag/35715_BQ.prd',
                        'https://www.diy.com/departments/blue-circle-mastercrete-cement-25kg-bag/35720_BQ.prd',
                        'https://www.diy.com/departments/blue-circle-extra-rapid-cement-25kg-bag/35718_BQ.prd',
                        'https://www.trade-point.co.uk/departments/blue-circle-mastercrete-cement-25kg-bag/35720_TP.prd',
                        'https://www.trade-point.co.uk/departments/blue-circle-multipurpose-cement-25kg-bag/35715_TP.prd',
                        'https://www.trade-point.co.uk/departments/blue-circle-extra-rapid-cement-25kg-bag/35718_TP.prd']

travis_perkins_links = ['https://www.travisperkins.co.uk/cement/obrien-all-purpose-cement-25kg/p/779612',
                        'https://www.travisperkins.co.uk/cement/castle-multicem-cement-in-plastic-bag-25kg/p/210768',
                        'https://www.travisperkins.co.uk/cement/blue-circle-general-purpose-grey-cement-in-paper-bag-25kg/p/846581',
                        'https://www.travisperkins.co.uk/cement/blue-circle-mastercrete-grey-cement-in-plastic-bag-25kg/p/250294',
                        'https://www.travisperkins.co.uk/cement/blue-circle-extra-rapid-fast-set-cement-25kg/p/847023',
                        'https://www.travisperkins.co.uk/cement/blue-circle-snowcrete-white-cement-25kg/p/550548',
                        'https://www.travisperkins.co.uk/cement/castle-cement-grey-25kg/p/767201',
                        'https://www.travisperkins.co.uk/cement/castle-white-portland-cement-25kg/p/550544',
                        'https://www.travisperkins.co.uk/cement/castle-quickcem-quick-setting-and-hardening-portland-cement-25kg/p/506615']

jewson_links = ['https://www.jewson.co.uk/p/hanson-general-purpose-cement-25kg-paper-bag-CCASCEM2',
                'https://www.jewson.co.uk/p/hanson-multicem-cement-25kg-plastic-bag-CCASTMCP',
                'https://www.jewson.co.uk/p/hanson-quickcem-quick-setting-cement-25kg-plastic-bag-CCASQCEM',
                'https://www.jewson.co.uk/p/hanson-multicem-cement-25kg-tough-paper-bag-CCASTMC2',
                'https://www.jewson.co.uk/p/hanson-white-cement-25kg-paper-bag-CCASWHIT']

wickes_links = ['https://www.wickes.co.uk/Blue-Circle-General-Purpose-Cement---25kg/p/224661#',
                'https://www.wickes.co.uk/Blue-Circle-Mastercrete-Cement---25kg/p/154100']

bradfords_links = ['https://www.bradfords.co.uk/blue-circle-mastercrete-25kg-cem210',
                   'https://www.bradfords.co.uk/blue-circle-general-purpose-cement-25kg-cem225',
                   'https://www.bradfords.co.uk/blue-circle-snowcrete-white-cement-25kg-snc225',
                   'https://www.bradfords.co.uk/blue-circle-extra-rapid-cement-25kg-bag-cem230']

selco_links = ['https://www.selcobw.com/cement-in-plastic-bag-25kg?geographic_area=61195',
               'https://www.selcobw.com/rugby-fastset-cement-25kg',
               'https://www.selcobw.com/rugby-high-strength-cement-25kg',
               'https://www.selcobw.com/rugby-white-cement-25kg']

tfm_sup_links = ['https://www.tfmsuperstore.co.uk/products/cement-425n-25kg-plastic-bag/',
                 'https://www.tfmsuperstore.co.uk/products/cement-25kg-paper-bag-2/']

carvers_links = ['https://www.carvers.co.uk/building-materials/cement-additives-salt/cement/cement-25kg-bag-hanson-554246']
############
buildShop_links = ['https://buildingshop.co.uk/product/cement-25kg-bag-paper-bag/',
                   'https://buildingshop.co.uk/product/cement-25kg/',
                   'https://buildingshop.co.uk/product/hanson-white-cement-25kg/']

megatek_links = ['https://www.megateksa.com/sq/cimento-e-bardhe-klasa-42-5-r-20-kg-thes',
                 'https://www.megateksa.com/sq/cimento-krujacem-klasa-32-5-r-25-kg-thes-cimento-portland-me-gur-gelqeror']

def data_manipulation(title, country, store, brand, code, price, bag_price_usd, bulk_price, vat,
                      price_wo_vat, dist_share, transport, ex_fac_price, notes, links):

    brands = ["O'Brien", "Castle", "Blue Circle", "Hanson", "Rugby", "Cement"]
    stores = ['Travis Perkins', 'B&Q', 'Trade Point', 'Jewson', 'Wickes', 'Bradfords', 'Selco BW', 'TFM Superstore', 'Carvers']
    weight_check = False
    price_check = False

    # rate of exchange

    # gbp to usd
    gbp_to_usd = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=USD'
    driver.get(gbp_to_usd)
    time.sleep(5)
    gbp_to_usd = str(driver.find_element(By.CSS_SELECTOR, "p[class*='result__BigRate-sc-1bsijpp-1 iGrAod'").text)
    gbp_to_usd = gbp_to_usd.split('US')[0].strip()

    # country
    while price_check == False:
        if price[0] == '£':
            country = 'United Kingdom'
        try:
            temp_price = price
            price = float(price[1:])
            price = temp_price
            price_check = True
            break
        except ValueError:
            price = price[:-2]
    # store
    for i in stores:
        if i.lower() in store.lower():
            store = i
            break
    if store == 'Item In Stock for Home Delivery':
        store = 'Trade Point'
    # brand
    for i in brands:
        if i.lower() in title.lower():
            brand = i
            break
    if brand == 'Cement':
        brand = ''
    # category
    try:
        category = title.split(brand)[1].strip()
    except ValueError:
        category = title.strip()
    except IndexError:
        category = title.split(brand)[0].strip()
    # code
    if (store == 'B&Q' or store == 'Trade Point'):
        if 'Standard' and 'Material' in code:
            code = code.split('Standard ')[1].split('Material')[0].strip()
        else:
            code = ''
    elif store == 'Travis Perkins':
        if 'View more' in code:
            code = code.split('View more')[0].strip()
        else:
            pass
    else:
        pass
    # price_per_kg
    kg = title.lower().split('kg')[0].split(' ')[-1].strip()

    while weight_check == False:
        try:
            price_per_kg = str(round(float(price[1:]) / float(kg), 2))
            weight_check = True
            break
        except ValueError:
            kg = kg[1:]

    if country == 'United Kingdom':
        price_per_kg = '£' + price_per_kg
    # price
    price = price
    #price in usd
    if price[0] == '£':
        bag_price_usd = round(float(price[1:]) * float(gbp_to_usd),2)
        bag_price_usd = '$' + str(bag_price_usd)
    else:
        pass

    # dataset manipulation
    data.loc[len(data.index)] = [country, store, brand, category, code, price_per_kg, price, bag_price_usd,
                                 bulk_price, vat, price_wo_vat, dist_share, transport, ex_fac_price, notes, links]
    return data

def diy_tradePoint(diy_tradePoint_links):

    for links in diy_tradePoint_links:
        url = links
        driver.get(url)
        time.sleep(5)

        country = store = brand = category = code = price_per_kg = price = bag_price_usd = bulk_price = vat = price_wo_vat = dist_share = transport = ex_fac_price = notes = ''

        title = str(driver.find_element(By.CSS_SELECTOR, "div[class*='_5c442f8c _6c656aee d14853b2 a57807c3 _068ba325 _0b888acb'").text)
        price = str(driver.find_element(By.CSS_SELECTOR, "div[class*='b25ad5d5 _4e80f7be _23ee746f _7b343263 _21dc035c'").text)
        store = str(driver.find_element(By.CSS_SELECTOR,
                                        "div[class*='_5c442f8c _6c656aee d14853b2 c7666214 f63bdc50 _8522d932'").text)
        code = str(
            driver.find_element(By.CSS_SELECTOR, "table[class*='f16ac490 eddf1b8e'").text)

        data = data_manipulation(title, country, store, brand, code, price, bag_price_usd, bulk_price,
                          vat,
                          price_wo_vat, dist_share, transport, ex_fac_price, notes, links)
    return data

def travis_perkins(travis_perkins_links):

    for links in travis_perkins_links:
        url = links
        driver.get(url)
        time.sleep(5)

        country = store = brand = category = code = price_per_kg = price = bag_price_usd = bulk_price = vat = price_wo_vat = dist_share = transport = ex_fac_price = notes = ''

        title = str(driver.find_element(By.CSS_SELECTOR, "div[class*='PDPDesktop__PDPTitle-sc-kr68up-3 iELfph'").text)
        price = str(driver.find_element(By.CSS_SELECTOR, "h1[class*='sc-bczRLJ sc-gsnTZi nFQPz ePZrKO'").text)
        store = 'Travis Perkins'
        code = str(
            driver.find_element(By.CSS_SELECTOR, "div[class*='PDPDesktop__SectionBody-sc-kr68up-11 fnlSWE'").text)

        data = data_manipulation(title, country, store, brand, code, price, bag_price_usd,
                                 bulk_price,
                                 vat,
                                 price_wo_vat, dist_share, transport, ex_fac_price, notes, links)
    return data

def jewson(jewson_links):

    for links in jewson_links:
        url = links
        driver.get(url)
        time.sleep(5)

        country = store = brand = category = code = price_per_kg = price = bag_price_usd = bulk_price = vat = price_wo_vat = dist_share = transport = ex_fac_price = notes = ''

        title = str(driver.find_element(By.CSS_SELECTOR, "h1[class*='product-title mb-1'").text)
        price = str(driver.find_element(By.CSS_SELECTOR, "span[class*='price__value'").text)
        store = 'Jewson'
        code = str(
            driver.find_element(By.CSS_SELECTOR, "div[class*='d-lg-none product__description'").text)

        data = data_manipulation(title, country, store, brand, code, price, bag_price_usd,
                                 bulk_price,
                                 vat,
                                 price_wo_vat, dist_share, transport, ex_fac_price, notes, links)
    return data

def wickes(wickes_links):

    for links in wickes_links:
        url = links
        driver.get(url)
        time.sleep(5)

        country = store = brand = category = code = price_per_kg = price = bag_price_usd = bulk_price = vat = price_wo_vat = dist_share = transport = ex_fac_price = notes = ''

        title = str(driver.find_element(By.CSS_SELECTOR, "h1[class*='pdp__heading'").text)
        price = str(driver.find_element(By.CSS_SELECTOR, "div[class*='main-price__value pdp-price__new-price'").text)
        store = 'Wickes'
        code = str(
            driver.find_element(By.CSS_SELECTOR, "div[class*='product-main-info__description'").text)

        data = data_manipulation(title, country, store, brand, code, price, bag_price_usd,
                                 bulk_price,
                                 vat,
                                 price_wo_vat, dist_share, transport, ex_fac_price, notes, links)
    return data

def bradfords(bradfords_links):

    for links in bradfords_links:
        url = links
        driver.get(url)
        time.sleep(5)

        country = store = brand = category = code = price_per_kg = price = bag_price_usd = bulk_price = vat = price_wo_vat = dist_share = transport = ex_fac_price = notes = ''

        title = str(driver.find_element(By.CSS_SELECTOR, "div[class*='page-title-wrapper product'").text)
        price = str(driver.find_element(By.CSS_SELECTOR, "span[class*='price'").text)
        store = 'Bradfords'
        code = ''

        data = data_manipulation(title, country, store, brand, code, price, bag_price_usd,
                                 bulk_price,
                                 vat,
                                 price_wo_vat, dist_share, transport, ex_fac_price, notes, links)
    return data

def selco(selco_links):

    for links in selco_links:
        url = links
        driver.get(url)
        time.sleep(5)

        country = store = brand = category = code = price_per_kg = price = bag_price_usd = bulk_price = vat = price_wo_vat = dist_share = transport = ex_fac_price = notes = ''

        title = str(driver.find_element(By.CSS_SELECTOR, "h1[class*='page-title page-title--product'").text)
        price = str(driver.find_element(By.CSS_SELECTOR, "span[class*='PriceBox-item-3SD PriceBox-itemExVat-skf'").text)
        store = 'Selco BW'
        code = str(
            driver.find_element(By.CSS_SELECTOR, "div[class*='rich-text'").text)

        data = data_manipulation(title, country, store, brand, code, price, bag_price_usd,
                                 bulk_price,
                                 vat,
                                 price_wo_vat, dist_share, transport, ex_fac_price, notes, links)
    return data

def tfm_sup(tfm_sup_links):

    for links in tfm_sup_links:
        url = links
        driver.get(url)
        time.sleep(5)

        country = store = brand = category = code = price_per_kg = price = bag_price_usd = bulk_price = vat = price_wo_vat = dist_share = transport = ex_fac_price = notes = ''

        title = str(driver.find_element(By.CSS_SELECTOR, "h1[class*='product_title entry-title'").text)
        price = str(driver.find_element(By.CSS_SELECTOR, "span[class*='woocommerce-Price-amount amount'").text)
        store = 'TFM Superstore'
        code = ''

        data = data_manipulation(title, country, store, brand, code, price, bag_price_usd,
                                 bulk_price,
                                 vat,
                                 price_wo_vat, dist_share, transport, ex_fac_price, notes, links)
    return data

def carvers(carvers_links):

    for links in carvers_links:
        url = links
        driver.get(url)
        time.sleep(5)

        country = store = brand = category = code = price_per_kg = price = bag_price_usd = bulk_price = vat = price_wo_vat = dist_share = transport = ex_fac_price = notes = ''

        title = str(driver.find_element(By.CSS_SELECTOR, "h1[class*='font-product-title'").text)
        price = str(driver.find_element(By.CSS_SELECTOR, "span[class*='lbl-price'").text)
        store = 'Carvers'
        code = str(driver.find_element(By.CSS_SELECTOR, "div[class*='description fr-view'").text)

        data = data_manipulation(title, country, store, brand, code, price, bag_price_usd,
                                 bulk_price,
                                 vat,
                                 price_wo_vat, dist_share, transport, ex_fac_price, notes, links)
    return data

diy_tradePoint(diy_tradePoint_links)
travis_perkins(travis_perkins_links)
jewson(jewson_links)
wickes(wickes_links)
bradfords(bradfords_links)
selco(selco_links)
tfm_sup(tfm_sup_links)
carvers(carvers_links)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(data)

data.to_excel('cement_data.xlsx')


