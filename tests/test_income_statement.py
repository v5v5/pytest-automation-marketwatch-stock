import pytest
import main

ticker = 'epam'
url = f'https://www.marketwatch.com/investing/stock/{ticker}/financials'

ERROR = 0.03
LOW = 1 - ERROR
HIGH = 1 + ERROR

def test_gross_income():
    page_content = main.get_page_content(url)

    sales_revenue = main.get_financial_indicator_value(page_content, main.sales_revenue_xpath)
    cost_of_goods = main.get_financial_indicator_value(page_content, main.cost_of_goods_xpath)
    gross_actual_actual = main.get_financial_indicator_value(page_content, main.gross_income_xpath)

    gross_income_expected = sales_revenue - cost_of_goods

    assert gross_actual_actual * LOW < gross_income_expected < gross_actual_actual * HIGH

def test_net_income():
    page_content = main.get_page_content(url)

    gross_income = main.get_financial_indicator_value(page_content, main.gross_income_xpath)
    sg_a_expense = main.get_financial_indicator_value(page_content, main.sg_a_expense_xpath)
    income_tax = main.get_financial_indicator_value(page_content, main.income_tax_xpath)
    net_income_actual = main.get_financial_indicator_value(page_content, main.net_income_xpath)

    net_income_expected = gross_income - sg_a_expense - income_tax

    assert net_income_actual * LOW < net_income_expected < net_income_actual * HIGH

