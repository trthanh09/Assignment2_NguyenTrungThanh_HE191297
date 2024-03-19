class Stock:
    def __init__(self, code):
        self.code = code
        self.prices = []

    def add_price(self, open_price, close_price):
        self.prices.append((open_price, close_price))

    def average_price_difference(self):
        total_diff = sum(close - open for open, close in self.prices)
        return total_diff / len(self.prices)


def read_file(filename):
    stocks = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_stocks = int(lines[0])
        for line in lines[1:]:
            stock_info = line.split()
            code = stock_info[0]
            open_price = float(stock_info[1])
            close_price = float(stock_info[2])
            if code not in stocks:
                stocks[code] = Stock(code)
            stocks[code].add_price(open_price, close_price)
    return stocks


def print_sorted_stocks(stocks):
    sorted_codes = sorted(stocks.keys())
    for code in sorted_codes:
        stock = stocks[code]
        avg_diff = stock.average_price_difference()
        print(f"{code}: {avg_diff:.3f}")


def search_stock_by_code(stocks, code):
    if code in stocks:
        max_close = max(price[1] for price in stocks[code].prices)
        min_close = min(price[1] for price in stocks[code].prices)
        print(f"Max Close Price: {max_close:.3f}")
        print(f"Min Close Price: {min_close:.3f}")
    else:
        print("Không tìm thấy mã chứng khoán.")


def find_trending_stocks(stocks):
    trending_stocks = []
    for code, stock in stocks.items():
        if len(stock.prices) >= 2:
            if stock.prices[0][1] > stock.prices[0][0] and stock.prices[1][1] > stock.prices[1][0]:
                trending_stocks.append(code)
    return trending_stocks


def find_longest_trending_stocks(stocks):
    longest_trending = []
    max_days = 0
    for code, stock in stocks.items():
        count = 0
        for price in stock.prices:
            if price[1] > price[0]:
                count += 1
        if count > max_days:
            longest_trending = [code]
            max_days = count
        elif count == max_days:
            longest_trending.append(code)
    return longest_trending, max_days


def main():
    stocks = read_file("data.txt")
    while True:
        print("\nMENU:")
        print("1. In thông tin tất cả mã chứng khoán và giá trị trung bình của hiệu (giá đóng cửa – giá mở cửa) trong 10 ngày")
        print("2. Tìm kiếm theo mã chứng khoán")
        print("3. Tìm kiếm những mã chứng khoán có xu hướng tăng")
        print("4. Tìm mã có số ngày tăng lớn nhất")
        print("5. Thoát chương trình")
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            print_sorted_stocks(stocks)
        elif choice == '2':
            code = input("Nhập mã chứng khoán cần tìm: ")
            search_stock_by_code(stocks, code)
        elif choice == '3':
            trending_stocks = find_trending_stocks(stocks)
            print("Các mã chứng khoán có xu hướng tăng đồng thời trong cả ngày 1 và ngày 2:")
            print(trending_stocks)
        elif choice == '4':
            longest_trending, max_days = find_longest_trending_stocks(stocks)
            print(f"Mã có số ngày tăng lớn nhất ({max_days} ngày):")
            print(longest_trending)
        elif choice == '5':
            print("Tác giả: [Nguyễn Trung Thành] - [HE191297]")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")


if __name__ == "__main__":
    main()
