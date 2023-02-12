# ###### fier import library to use in the project ######
import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
days= ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('##### Hello! Let\'s explore some US bikeshare data! ######')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("\n#### Would You like to see data for '(Chicago, New York City, Washington)' Typer Your Want ####\n").lower().strip()
    
    while city not in CITY_DATA :
        print ("#### YOur Chooes Is NOt Correct Try Again !!!!! ####")
        city = input("\n#### Would You like to see data for:'(Chicago, New York City, Washington)' Typer Your Want ####\n" ).lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
   
    while True :
        month = input ("\n#### Choose Month :( jan, feb, mar, apr, may, jun, all) ####\n").lower()
        if month in months : 
            break
        else:
            print ("#### YOur Chooes Is NOt Correct Try Again !!!!! ####")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday) 
    while True :
        day = input("\n#### Choose Day:Enter = ( 'all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday') ####\n").lower().strip()
        if day in days :
            break
        else:
            print ("#### Your Chooes Is NOt Correct Try Again !!!!! ####")
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(f'The most common month = {popular_month} ')
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f'The most common day of week = {popular_day}')
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most common start hour = {popular_hour}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode() [0]
    print(f'The Most Commonly Used Start Station = {popular_start_station}')
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode() [0]
    print(f'The Most Commonly Used End Station = {popular_end_station}')   
    # TO DO: display most frequent combination of start station and end station trip
    df['frequent']=df['Start Station']+","+df['End Station']
    print('The Most Frequent Combination Of Start Station And End Station Trip = {}'.format(df['frequent'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum().round()
    print(f'The Total Travel Time = {total_travel}')
    # TO DO: display mean travel time
    mean_travel = df ['Trip Duration'].mean().round()
    print(f'The Mean Travel Time = {mean_travel}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print(f'The Counts Of User Types = {user_types}')
    # TO DO: Display counts of gender
    if city != 'washington':
        count = df['Gender'].value_counts().to_frame()
        print(f'The Counts Of User Types = {count}')
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_brith = df['Birth Year'].max()
        common_brith = df['Birth Year'].mode()[0]
    else :
        print('Your city chooes no have data !!! ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def five_raw (df):
    #______ prompt the user when he like to show the raw data of thet city if they want to see 5 lines of raw data_____________
    print ('\n Data is available if you want to check ... \n  ')
    #_________ask user about 5 raw if want _____________
    choice = input('would you like to show 5 raws from data !!!!! ... if you want type (yes) if you don\'t type (no)').lower().strip()
    #_______loop for print 5 raw ________
    #_____________ If  Enter wrong type  print this__________ 
    if choice not in ['yes', 'no']:
         print(' Please Choice Again ...')
         choice = input('would you like to show 5 raws from data !!!!! ... if you want type (yes) if you don\'t type (no)').lower().strip()
    #_________whan choice no prin Thank you____________
    elif choice == 'no':
        print(' Thank You ...........')  
    #__________whan choice yes than loop work_____________
    else:
        i = 0
        while i+5 < df.shape[0]:
            print(df.iloc[i:i+5])
            i += 5
            choice = input('\n would you like to show 5 raws from data !!!!! ... if you want type (yes) if you don\'t type (no) \n').lower().strip()
            if choice == 'no':
                print(' Thank You ...........')
                break         
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        five_raw (df)
        restart = input('\n Would you like to restart? Enter yes or no....\n')
        if restart.lower() != 'yes':
            print(' Thank You ...........')
        
            break


if __name__ == "__main__":
	main()
