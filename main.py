import requests
from lxml import html

def format_number(number: str)->str:
    number = number.replace('B', '000000')
    number = number.replace('M', '000')
    number = number.replace('.', '')
    number = number.replace('(', '-')
    number = number.replace(')', '')
    return number

def get_content(url: str)->str:
    page = requests.get(url)
    content = html.fromstring(page.content)
    return content

ticker = 'epam'
url = f'https://www.marketwatch.com/investing/stock/{ticker}/financials'

sales_revenue_xpath = '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[1]/td[6]'
cost_of_goods_xpath = '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[3]/td[6]'
gross_income_xpath = '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[9]/td[6]'

content = get_content(url)

sales_revenue = content.xpath(sales_revenue_xpath)
cost_of_goods = content.xpath(cost_of_goods_xpath)
gross_income = content.xpath(gross_income_xpath)

print(sales_revenue[0].text)
print(cost_of_goods[0].text)
print(gross_income[0].text)
