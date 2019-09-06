# list numbers from 0 to 10, divide each by 3,
# print results as 2 decimal places
# round()
# format ()


divisor = 3
decimal_places = 2

for number in range(0,11):
   #print(round(number/divisor, decimal_places))
   print( "this is my rounded result {0:.2f} also this{1}".format(number/divisor,5))