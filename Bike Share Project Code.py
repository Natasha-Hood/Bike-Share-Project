import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city = ('chicago', 'new york city', 'washington')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('Which city would you like to look at today: Chicago, New York City, or Washington?: ').lower()
       if city == 'chicago' or city == 'new york city' or city == 'washington':
           print('Okay! Now choose a month. ')
           break
       else:
           print('Data not available for that city. Please choose one of the following: Chicago, New York City, or Washington.') 
           continue
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
       month = input('Next, please choose a month. ').lower()
       if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
           print('Nice! Now choose a day of the week. ')
           break
       else:
           print("I am sorry, please pick a month between January and June, or you may choose 'all'. ")
           continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
       day = input('Last but not least, what day would you like to look at the data for? ').lower()
       if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
           print("Let's check out that data!")
           break
       else:
           print("What other day of the week is there that I don't already know about?")
           continue

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['Month'] = df['Start Time'].dt.month
    
    df['Day of the Week'] = df['Start Time'].dt.day_name()
    
    df['Hour'] = df['Start Time'].dt.hour
        
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        month = months.index(month) + 1 
        
        df = df[df['Month'] == month]
        
    if day != 'all':
        df = df[df['Day of the Week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()
    print(f"The most common month is: {common_month}\n")
    
    # TO DO: display the most common day of week
    common_day = df['Day of the Week'].mode()
    print(f"The most common day of the week is: {common_day}\n")
    
    # TO DO: display the most common start hour
    common_start_hour = df['Hour'].mode()
    print(f"The most common start hour is: {common_start_hour}\n" )
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)
    
    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    count_start = df['Start Station'].value_counts()
    print(f"The most common start station is {common_start}\n")

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    count_end = df['End Station'].value_counts()
    print(f"The most common end station is {common_end}\n")

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent combination of start station and end station trips is {start_end_combo}\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print(f"The total travel time is {total_travel}\n")

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(f"The mean travel time is {mean_travel}\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"The counts of user types are as follows: {user_type}\n")

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_type = df['Gender'].value_counts()
        print(f"The gender counts are as follows: {gender_type}\n")
    else:
        print("There is no gender data available for Washington")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print(f"The earlier birth year is: {earliest_year}\n")
    else: 
        print("There is no birth year data available for Washington")
        
    if 'Birth Year' in df:
        most_recent = df['Birth Year'].max()
        print(f"The most recent birth year is: {most_recent}\n")
    else:
        print("There is no birth year data available for Washington")
        
    if 'Birth Year' in df: 
        common_year = df['Birth Year'].mode()[0]
        print(f"The most common birth year is: {common_year}\n")
    else:
        print("There is no birth year data available for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def main():
    """Offers to display rows of raw data 5 rows at a time based on the inputs of the user at the beginning of the program."""
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input("Would you like to view 5 rows of individual trip data? Please enter yes or no. ")
        if raw_data == 'yes':
            start_loc = 0
            print(df.iloc[start_loc: start_loc + 5])
            start_loc += 5
            view_display = input('Would like to see the next 5 rows of data?: ').lower()
            while view_display == 'yes':
                print(df.iloc[start_loc: start_loc + 5])
                start_loc += 5
                view_display = input('Would like to see the next 5 rows of data?: ').lower()
                continue
        else:
            print("Ok!")
                                         
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
