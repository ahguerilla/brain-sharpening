'''
have an array stock_prices_yesterday where:

The indices are the time, as a number of minutes past trade opening time, which was 9:30am local time.
The values are the price of Apple stock at that time, in dollars.
For example, the stock cost $500 at 10:30am, so stock_prices_yesterday[60] = 500.

Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of 
1 Apple stock yesterday. For this problem, we won't allow "shorting" - you must buy before you sell.
'''


def calc_best_price(trades):
    best_price = None
    max_profit = 0
    for t in trades:
        if best_price is None:
            best_price = t
            continue
        current_profit = t - best_price
        max_profit = max(current_profit, max_profit)
        best_price = min(best_price, t)
    return max_profit


# TEST DATA
def test():
    # PROFIT = 5
    stock_prices_one = [1, 2, 3, 4, 6]
    # PROFIT = 0
    stock_prices_two = [5, 4, 3, 2, 1]
    # PROFIT = 6
    stock_prices_three = [5, 2, 3, 4, 8]
    # PROFIT = 9
    stock_prices_four = [5, 10, 2, 11, 8]

    try:
        if not calc_best_price(stock_prices_one) == 5:
            raise "Test Error"
        if not calc_best_price(stock_prices_two) == 0:
            raise "Test Error"
        if not calc_best_price(stock_prices_three) == 6:
            raise "Test Error"
        if not calc_best_price(stock_prices_four) == 9:
            raise "Test Error"
        print "Tests Passed"
    except:
        print "Test Failed"

test()