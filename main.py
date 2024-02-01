age = float('Enter age:')
weight = float('Enter weight in pounds:')
heart_rate = float('Enter heart rate:')
time = float('Enter time:')

calories_women = ( (age x 0.074) — (weight x 0.05741) + (heart_rate x 0.4472) — 20.4022 ) x time / 4.184
calories_men =  ( (Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) — 55.0969 ) x Time / 4.184

print(f'Women: {calories_women:.2f}')
print(f'Men: {calories_men:.2f}')