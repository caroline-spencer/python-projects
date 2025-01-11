# Queries for the NPS Parks database
import sqlite3
import os

db = None


def main():
    global db
    try:
        dbname = 'nps_parks.db'
        if os.path.exists(dbname):         # Does this database file exist?
            db = sqlite3.connect(dbname)   # Connect to the database

            query_parks_by_designation()
            query_parks_by_activity()
            query_parks_by_topic()

            db.close()     # Close the database
        else:
            print('Error:', dbname, 'does not exist')

    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)


def query_parks_by_designation():
    # TODO Prompt for the designation to list all National Parks with this designation.
    # TODO Continue prompting if the user enters no value.
    # TODO Construct the query that incorporates the user's selection, and display formatted results.
    # TODO See the assignment description for sample input and output for Query 1

    search_value = input('Find national parks with this designation: ')
    while not search_value.isalpha():
        search_value = input('Find national parks with this designation: ')
    try:
        cursor = db.cursor()
        sql = "SELECT Name, Designation, States FROM PARK WHERE Designation LIKE '%" + search_value + "%' ORDER BY Name"
        # print(sql)
        cursor.execute(sql)  # execute the query
        records = cursor.fetchall()
        if len(records) > 0:  # if at least one record found, loop through and print
            print(len(records), 'National Parks designated as \'', search_value, '\'')
            print('----------------------------------------------')
            for rec in records:
                # print(rec)
                print(format(rec[0], '<60'), format(rec[1], '<50'), format(rec[2], '<5'))
        else:
            print("There are no parks with the designation '" + search_value + "'")
        print()
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)


def query_parks_by_activity():
    # TODO Prompt for an activity to list all National Parks that support this activity.
    # TODO Continue prompting if the user enters no value.
    # TODO Construct the query that incorporates the user's selection, and display formatted results.
    
    search_value = input('Find national parks with this activity: ')
    while not search_value.isalpha():
        search_value = input('Find national parks with this activity: ')
    try:
        cursor = db.cursor()
        sql = "SELECT Name, Activity, States FROM PARK " \
              "JOIN Activities ON Park.ParkCode = Activities.ParkCode " \
              "AND activity LIKE '%" + search_value + "%' ORDER BY Name"
        # print(sql)
        cursor.execute(sql)  # execute the query
        records = cursor.fetchall()
        if len(records) > 0:  # if at least one record found, loop through and print
            print(len(records), 'National Parks with activity \'', search_value, '\'')
            print('----------------------------------------------')
            for rec in records:
                # print(rec)
                print(format(rec[0], '<60'), format(rec[1], '<50'), format(rec[2], '<5'))
        else:
            print("There are no parks with the activity '" + search_value + "'")
        print()
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)


def query_parks_by_topic():
    # TODO Prompt for a topic to list all National Parks characterized by this topic.
    # TODO Continue prompting if the user enters no value.
    # TODO Construct the query that incorporates the user's selection, and display formatted results.
    
    search_value = input('Find national parks with this topic: ')
    while not search_value.isalpha():
        search_value = input('Find national parks with this topic: ')
    try:
        cursor = db.cursor()
        sql = "SELECT Name, Topic, States FROM PARK " \
              "JOIN Topics ON Park.ParkCode = Topics.ParkCode " \
              "AND topic LIKE '%" + search_value + "%' ORDER BY Name"
        print(sql)
        cursor.execute(sql)  # execute the query
        records = cursor.fetchall()
        if len(records) > 0:  # if at least one record found, loop through and print
            print(len(records), 'National Parks with activity \'', search_value, '\'')
            print('----------------------------------------------')
            for rec in records:
                # print(rec)
                print(format(rec[0], '<60'), format(rec[1], '<50'), format(rec[2], '<5'))
        else:
            print("There are no parks with the topic '" + search_value + "'")
        print()
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)


main()
