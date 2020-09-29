hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

######## List Comprehension ##############

#Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

#First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.

total_price = 0

# Iterate through the prices list and add each price to the variable total_price.

for price in prices:
  total_price += price
  # create a variable called average_price to find the avg price
  average_price = total_price/len(prices)
#Print the value of average_price
print('Average Haircut Price: $' + str(average_price))

#Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.
new_prices = [price - 5 for price in prices]

#Print new_prices
print(new_prices)


total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print('Total Revenue $'+ str(total_revenue))

average_daily_revenue = total_revenue / 7
print('Average Total Revenue $' + str(average_daily_revenue))


cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]<30]

print(cuts_under_30)