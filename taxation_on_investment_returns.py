def after_tax_return(initial_investment, annual_return_rate, annual_dividend_yield, duration_years, capital_gains_tax_rate, dividend_tax_rate, tax_annually=True):
    """
    Calculate the after-tax return on an investment considering capital gains and dividends.

    :param initial_investment: Initial amount invested
    :param annual_return_rate: Annual return rate (as a decimal)
    :param annual_dividend_yield: Annual dividend yield (as a decimal)
    :param duration_years: Number of years investment is held
    :param capital_gains_tax_rate: Tax rate on capital gains (as a decimal)
    :param dividend_tax_rate: Tax rate on dividends (as a decimal)
    :param tax_annually: Whether tax is applied annually or at the end
    :return: Total after-tax value of the investment
    """
    current_value = initial_investment
    total_dividends = 0

    for year in range(1, duration_years + 1):
        annual_gain = current_value * annual_return_rate
        annual_dividend = current_value * annual_dividend_yield
        dividend_tax = annual_dividend * dividend_tax_rate

        if tax_annually:
            tax_on_gain = annual_gain * capital_gains_tax_rate
            current_value = current_value + annual_gain - tax_on_gain + annual_dividend - dividend_tax
        else:
            current_value += annual_gain + annual_dividend

        total_dividends += annual_dividend - dividend_tax

    if not tax_annually:
        total_gain = current_value - initial_investment
        tax_on_gain = total_gain * capital_gains_tax_rate
        current_value -= tax_on_gain

    return current_value, total_dividends

def format_output(initial_investment, final_value, total_dividends, duration_years):
    """
    Format the investment output professionally.

    :param initial_investment: Initial amount invested
    :param final_value: The final value of the investment after tax
    :param total_dividends: Total dividends received after tax
    :param duration_years: Number of years investment is held
    :return: Formatted string of results
    """
    return (
        f"After {duration_years} years, an initial investment of ${initial_investment:,.2f}\n"
        f"would grow to a final value of ${final_value:,.2f} after tax,\n"
        f"including ${total_dividends:,.2f} from dividends after tax."
    )

# Example usage
initial_investment = 10000  # $10,000 initial investment
annual_return_rate = 0.07   # 7% annual return
annual_dividend_yield = 0.02  # 2% annual dividend yield
duration_years = 5         # 5 years duration
capital_gains_tax_rate = 0.15  # 15% capital gains tax
dividend_tax_rate = 0.15  # 15% dividend tax

final_value, total_dividends = after_tax_return(
    initial_investment, annual_return_rate, annual_dividend_yield, duration_years,
    capital_gains_tax_rate, dividend_tax_rate, tax_annually=False
)

print(format_output(initial_investment, final_value, total_dividends, duration_years))
