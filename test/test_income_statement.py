import main
from main import format_number as f

def test_gross_income():
    ticker = 'epam'
    url = f'https://www.marketwatch.com/investing/stock/{ticker}/financials'
    content = main.get_content(url)

    sales_revenue = float(f(content.xpath(main.sales_revenue_xpath)[0].text))
    cost_of_goods = float(f(content.xpath(main.cost_of_goods_xpath)[0].text))
    gross_income = float(f(content.xpath(main.gross_income_xpath)[0].text))

    expected_gross_income = sales_revenue - cost_of_goods
    actual_gross_income = gross_income

    assert actual_gross_income * 0.95 < expected_gross_income < actual_gross_income * 1.05