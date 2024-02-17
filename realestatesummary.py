current_price = int(input())
last_month_price = int(input())
difference = current_price - last_month_price
mortgage = (current_price * 0.051) / 12


print(f'This house is ${current_price:.2f}. The change is ${difference:.2f} since last month. The estimated monthly mortage is ${mortgage:.2f}.')