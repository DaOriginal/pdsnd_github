import time
import pandas as pd
import numpy as np

MY_CITIES = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while 1:
        city = input('Enter city to start with. Chicago or Washington or New York \n').lower()
        if city not in MY_CITIES.keys():
            print('Invalid Input. Try Again')
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while 1:
        month = input('Enter month to filter data from. Type: Jan or Feb or Mar or Apr or May or Jun or Jul.... OR all for no filter \n').lower()
        my_months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','all']
        if month not in my_months:
            print('Invalid input. Try Again \n')
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
        day = input('Enter day to filter data from. Monday or Tuesday or Wednesday....  OR all for no filter \n').lower()
        my_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
        if day not in my_days:
            print('Invalid input. Try Again')
            continue
        else:
            break 
  
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
    df = pd.read_csv(MY_CITIES[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        miyezi = ['jan','feb','mar','apr','may','jun','jul','aug','sep','nov','dec','all']
        month = miyezi.index(month)+1

        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()[0]
    print(f'The most popular month is: {most_month}')

    # TO DO: display the most common day of week
    most_day = df['day_of_week'].mode()[0]
    print(f'The most popular day of the week is: {most_day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most popular hour is: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most frequent start station is: {popular_start_station}')

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'The most frequent end station is: {popular_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    freq_combination = df['Start To End'].mode()[0]
    print(f'The most frequent combination of trips is: {freq_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    minute,second = divmod(total_duration,60)
    hour,minute = divmod(minute,60)
    print(f'The total trip duration is {hour} hours, {minute} minutes and {second} seconds.')

    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    mins,sec = divmod(average_duration,60)
    if mins > 60:
        hrs,mins = divmod(mins, 60)
        print(f'The average trip duration is {hrs} hours, {mins} minutes and {sec} seconds')
    else:
        print(f'The average trip duration is {mins} minutes and {sec} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f'The total count of user types is: {user_type}')

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(f'The total count based on Gender is: {gender}')
    else:
        print('We do not have Gender defined in the dataset')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest_year = df['Birth_Year'].min()
        print(f'The earliest year is: {earliest_year}')
        recent_year = df['Birth_Year'].max()
        print(f'The most recent year is: {recent_year}')
        common_year = df['Birth_Year'].mode()[0]
        print(f'The most common year is: {common_year}')
    else:
        print('We do not those birth year details in this dataset.')   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Asking a user if they want 5 lines of data or more"""
    raw_data = 0
    while 1:
        response = input('Do you want to see the raw data. Type "yes" or "no"').lower()
        if response not in ['yes','no']:
            response = input('Invalid entry. Please "yes" or "no"').lower()
        elif response == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data +5])
            again = input('Do you want more? Type "yes" or "no"').lower()
            if again == 'no':
                break
        elif response =='no':
            return



def main():
    city  = ""
    month = ""
    day   = ""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
