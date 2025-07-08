# [] create The Weather
# Norman McCord


import urllib.request

url = "https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv"
urllib.request.urlretrieve(url, "mean_temp.txt")

# curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt


mean_temps = open("mean_temp.txt", "a+")
mean_temps.write("Rio de Janeiro,Brazil,30.0,18.0\n")

mean_temps.seek(0)
headings = mean_temps.readline()
headings_list = headings.split(',')

print("Norman McCord")

line = mean_temps.readline()
while line:
    city_temp = line.strip().split(',')
    city = city_temp[0]
    highest = city_temp[2]  # "month ave: highest high" is index 2 based on the headings
    print("City of", city, "month ave: highest high is", highest, "Celsius")
    line = mean_temps.readline()


mean_temps.close()


