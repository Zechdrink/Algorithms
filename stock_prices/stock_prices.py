#!/usr/bin/python

# import argparse

def find_max_profit(prices):
  high = 0
  low = prices[0]
  for x in range(0, len(prices)):
    if prices[x] > high:
      high = prices[x]
      highIndex = x
  for x in range(0, highIndex):
    if prices[x] < low:
      low = prices[x]
  return high - low


print(find_max_profit([20, 10, 40, 5]))
# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))