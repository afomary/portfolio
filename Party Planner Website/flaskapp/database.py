from pymysql import connect
from pymysql.cursors import DictCursor

from flaskapp.config import DB_HOST, DB_USER, DB_PASS, DB_DATABASE

# Make sure you have data in your tables. You should have used auto increment for
# primary keys, so all primary keys should start with 1

# <3 INSTRUCTIONS EASIER TRANSLATION TO SELF : <3
#make code match table slides instead of csv file slides, check lecture stuff to do this. -
#remove csv mentions -
#add data checker (make sure number length and other things are appropriate answers, (under 4 good,  over bad etc. maybe that's varchar char checker? )) -
#add primary keys to sql, input to mariadb (check slides for primary key) -
#cgi upload (hope it works)

def get_connection():
   
    return connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DATABASE,
        cursorclass=DictCursor
    )
#here i make the connection from config file

def get_events():
    """Returns a list of dictionaries representing all of the event data"""

    sql = "select * from events"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
#here i get  events using select from in sql 

def get_event(event_id):
    """Takes a event_id, returns a single dictionary containing the data for the event with that id"""
    sql = "select * from events where event_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, event_id)
            return cursor.fetchall()
#here i get a single event using the same thing, just including event id specifically now 

def add_event(name,event_date,start_time,end_time,venue,invitation,maximum_attendees,planner,host,rental_items,note,image_path):
    """Takes as input all of the data for a event. Inserts a new event into the event table"""
    sql = "insert into events (name, event_date,start_time,end_time,venue,invitation,maximum_attendees,planner,host,rental_items,note,image_path) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name, event_date,start_time,end_time,venue,invitation,maximum_attendees,planner,host,rental_items,note,image_path))
        conn.commit()
#adding event to event table 

def update_event(event_id, name,event_date,start_time,end_time,venue,invitation,maximum_attendees,planner,host,rental_items,note,image_path):
    """Takes a event_id and data for a event. Updates the event table with new data for the event with event_id as it's primary key"""
    sql = "update event_id from events where event_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id, name, event_date, start_time,end_time,venue,invitation,maximum_attendees,planner,host,rental_items,note,image_path))
        conn.commit()
#updating existing event

def get_people():
    """Returns a list of dictionaries representing all of the person data"""
    
    sql = "select * from people"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
#get person data from people tablleeee 

def add_person(name,address,email,dob,phone,role):
    """Takes as input all of the data for a person and adds a new person to the person table"""
    
    sql = "insert into TABLE (name, address,email,dob,phone,role) values (%s, %s, %s, %s, %s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name, address,email,dob,phone,role))
        conn.commit()
#add person to people table using insert , %s means string , to be subsituted 

def delete_person(person_id):
    """Takes a person_id and deletes the person with that person_id from the person table"""

    sql = "delete from people where person_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (person_id))
        conn.commit()
#delete person from people table

def get_attendees(event_id):
    """Returns a list of dictionaries representing all of the data for people attending a particular event"""

    sql = "select * from events where event_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, event_id)
            return cursor.fetchall()
#get attendees for specific event identified in the parameters 

def add_attendee_event(event_id, attendee_id):
    """Takes as input a event_id and a attendee_id and inserts the appropriate data into the database that indicates the attendee with attendee_id as a primary key is attending the event with the event_id as a primary key"""
    sql = "insert into events (event_id, attendee_id) values (%s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id, attendee_id))
        conn.commit()
#add this given attendee to the given event, so im updating the event table with this

def remove_attendee_event(event_id, attendee_id):
    """Takes as input a event_id and a attendee_id and deletes the data in the database that indicates that the attendee with attendee_id as a primary key
    is attending the event with event_id as a primary key."""
    
    sql = "delete from events where (event_id = %s, attendee_id = %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id, attendee_id))
        conn.commit()
#remove  this given attendee from this given event 

def get_host(event_id):
    """Takes a event_id and returns a dictionary of the data for the host of the event with
    event_id as its primary key"""
    
    sql = "select * from events where event_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, event_id)
            return cursor.fetchall()
#who is the host of this specified event in the parameter? this function answers that 

def set_host(person_id, event_id):
    """Sets the person with primary key person_id as the host of the event with event_id as its primary key"""
    
    sql = "alter events add constraint foreign key (person_id) references people(person_id)"
    sql2 = "update events set host = person_id"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, sql2, person_id, event_id)
        conn.commit()
#this person given in first parameter is the host of the event specified in second parameter. this function updates that in the events table

def get_planner(event_id):
    """Takes a event_id and returns a dictionary of the data for the planner of the event with
    event_id as its primary key"""
    
    sql = "select * from events where event_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, event_id)
            return cursor.fetchall()
    
#finds the planner of an event at specific event id

def set_planner(person_id, event_id):
    """Sets the person with primary key person_id as the planner of the event with event_id as its primary key"""

    sql = "alter events add constraint foreign key (person_id) references people(person_id)"
    sql2 = "update events set planner = person_id"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, sql2, person_id, event_id)
        conn.commit()

#person_id is now set as the planner of event_id . 1st sql adds foreign key, 2nd sql updates it 

def get_venues():
    """Returns a list of dictionaries representing all of the venues data"""

    sql = "select * from venues"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

#spits back out the venues table

def add_venue(name,address,phone,fee,capacity):
    """Takes as input all of the data for a venue. Inserts a new venue into the event table"""
    sql = "insert into venues (name,address,phone,fee,capacity) values (%s, %s, %s, %s, %s)"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (name, address,phone,fee,capacity))
        conn.commit()

#all info given in the parameters has been added as a new venue in the venues table!

if __name__ == "__main__":
    # Add test code here to make sure all your functions are working correctly

    print(f"All events: {get_events()}")
    print(f"Event info for event_id 1: {get_event(1)}")
    print(f"All people: {get_people()}")
    print(f"All attendees attending the event with event_id 1: {get_attendees(1)}")

def get_venue_name(event_id):
    sql = "select * from venues where event_id = %s"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, event_id)
            return cursor.fetchall()
#new function: getting the name of the venue specified in the parameters from the venues table where the id = event_id

