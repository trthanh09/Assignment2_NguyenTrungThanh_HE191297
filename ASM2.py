class Stock:
    def __init__(self, code):
        self.code = code
        self.prices = []

    def add_price(self, open_price, close_price):
        self.prices.append((open_price, close_price))
        self.open_price= open_price
        self.close_price = close_price
    def avg_diff(self):
        return round(sum(close - open for open, close in self.prices) / len(self.prices), 3)

    def high_low(self):
        return max(close for open, close in self.prices), min(close for open, close in self.prices)

    def increasing_days(self):
        return sum(1 for open, close in self.prices if close > open)

stocks = {}

def read_file():
    fileName = input("Enter the file name: ")
    with open(fileName,'r') as file:
        line = file.readlines()
        for line in file:
            code, open_price, close_price = line.split(' ')
            if code not in stocks:
                stocks[code] = Stock(code)
            stocks[code].add_price(float(open_price), float(close_price))
    for code in sorted(stocks.keys()):
        print(f'{code}: {stocks[code].avg_diff()}')

def search_stock():
    code = input('Enter stock code: ')
    if code in stocks:
        high, low = stocks[code].high_low()
        print(f'Highest closing price: {high}\nLowest closing price: {low}')
    else:
        print('Stock code not found.')

def increasing_stocks():
    for code in stocks:
        if all(close > open for open, close in stocks[code].prices[:2]):
            print(code)

def max_increasing_days():
    max_days = max(stocks[code].increasing_days() for code in stocks)
    for code in stocks:
        if stocks[code].increasing_days() == max_days:
            print(code)

def main():
    while True:
        print('1. Read file')
        print('2. Search stock')
        print('3. Increasing stocks')
        print('4. Max increasing days')
        print('5. Exit')
        option = input('Choose an option: ')
        if option == '1':
            read_file()
        elif option == '2':
            search_stock()
        elif option == '3':
            increasing_stocks()
        elif option == '4':
            max_increasing_days()
        elif option == '5':
            print('Author: Nguyễn Trung Thành (HE191297)')
            break

if __name__ == '__main__':
    main()
