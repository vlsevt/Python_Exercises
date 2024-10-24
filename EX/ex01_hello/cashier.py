"""EX01 Cashier."""


amount = int(input("Enter a sum: "))
fifty_cent_coins = amount // 50
twenty_cent_coins = (amount % 50) // 20
ten_cent_coins = (amount % 50 % 20) // 10
five_cent_coins = (amount % 50 % 20 % 10) // 5
one_cent_coins = (amount % 50 % 20 % 10 % 5)

coins = fifty_cent_coins + twenty_cent_coins + ten_cent_coins + five_cent_coins + one_cent_coins

print(f"Amount of coins needed: {coins}")
