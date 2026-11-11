import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print("Hello! The following is a graph choice for Sitka, Alaska from 2018.")
    print("Please choose 'highs' to see a graph of the daily high tempuratures, 'low'")
    print("to see a graph of the daily low temperatures, or 'exit' to exit the program.")
    print("")

    choice = ''
    while choice != 'exit':

        choice = input("Did you want to see the highs or the lows for 2018? ")

        if choice == 'highs':
            # Reset file pointer to the beginning
            f.seek(0)
            next(reader)
            # Get dates and high temperatures from this file.
            dates, highs = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                high = int(row[5])
                highs.append(high)

            # Plot the high temperatures.
            #plt.style.use('seaborn')
            fig, ax = plt.subplots()
            ax.plot(dates, highs, c='red')

            # Format plot.
            plt.title("Daily high temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)

            plt.show()



        elif choice == 'lows':
            # Reset file pointer to the beginning
            f.seek(0)
            next(reader)
            # Get dates and low temperatures from this file.
            dates, lows = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                low = int(row[6])
                lows.append(low)

            # Plot the low temperatures.
            fig, ax = plt.subplots()
            ax.plot(dates, lows, c='blue')

            # Format plot.
            plt.title("Daily low temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)

            plt.show()

        elif choice == 'exit':
            print("Exiting the program now...")
            exit()
          
        elif choice != 'highs' and 'lows' and 'exit':
            print("Please choose 'highs' or 'lows' to continue, or 'exit' to exit the program.")
            continue
    
