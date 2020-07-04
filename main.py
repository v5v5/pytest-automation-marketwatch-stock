import requests
from lxml import html

def format_number(number: str) -> str:
    number = number.replace('B', '000000')
    number = number.replace('M', '000')
    number = number.replace('.', '')
    number = number.replace('(', '-')
    number = number.replace(')', '')
    return number

def get_page_content(url: str) -> str:
    page = requests.get(url)
    return html.fromstring(page.content)

def get_financial_indicator_value(page_content: str, xpath: str)->float:
    return float(format_number(page_content.xpath(xpath)[0].text))

ticker = 'epam'
url = f'https://www.marketwatch.com/investing/stock/{ticker}/financials'

sales_revenue_xpath = '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[1]/td[6]'
cost_of_goods_xpath = '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[3]/td[6]'
gross_income_xpath = '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[9]/td[6]'

page_content = get_page_content(url)

sales_revenue = get_financial_indicator_value(page_content, sales_revenue_xpath)
cost_of_goods = get_financial_indicator_value(page_content, cost_of_goods_xpath)
gross_income = get_financial_indicator_value(page_content, gross_income_xpath)

print(sales_revenue)
print(cost_of_goods)
print(gross_income)
