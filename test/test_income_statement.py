import pytest
import main

ticker = 'epam'
url = f'https://www.marketwatch.com/investing/stock/{ticker}/financials'

ERROR = 0.05
LOW = 1 - ERROR
HIGH = 1 + ERROR

def test_gross_income():
    page_content = main.get_page_content(url)

    sales_revenue = main.get_financial_indicator_value(page_content, main.sales_revenue_xpath)
    cost_of_goods = main.get_financial_indicator_value(page_content, main.cost_of_goods_xpath)
    gross_income = main.get_financial_indicator_value(page_content, main.gross_income_xpath)

    expected_gross_income = sales_revenue - cost_of_goods
    actual_gross_income = gross_income

    assert actual_gross_income * LOW < expected_gross_income < actual_gross_income * HIGH