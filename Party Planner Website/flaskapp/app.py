# Copyright © 2023, Indiana University

from flask import Flask, render_template, request, url_for, redirect 
from flaskapp import database
from flaskapp.config import *

app = Flask(__name__)

@app.route("/")
def index():
    '''routes us to the index page using index function'''

    return render_template("index.html")
    
@app.route("/people/")
def get_people():
    
    '''function accesses the people in the dictionary '''
    # with open("people.csv", encoding='UTF-8-sig') as csvfile:
    #     contents = csv.DictReader(csvfile)

    #     all_people= {
    #         row['name']: {
    #         'name': row['name'],
    #         'address': row['address'],
    #         'email': row['email'],
    #         'birthday': row['birthday'],
    #         'phone': row['phone'],
    #     } 
    #         for row in contents
    #     }
    all_people = database.get_people()
    return render_template("people.html", people=all_people)

@app.route("/events/")
@app.route("/events/<event_id>")
@app.route("/events/<event_id>/attendees/<person_id>/delete")
@app.route("/events/<event_id>/attendees/add", methods=['GET', 'POST'])
def get_events(event_id=None):
    '''gets each item in the events dictionary, and specifies one particular event for <event_id> and each individual page specified'''
    # with open("events.csv", encoding='UTF-8-sig') as csvfile:
    #     contents = csv.DictReader(csvfile)

    #     all_events= {
    #         row['name']: {
    #         'name': row['name'],
    #         'date': row['date'],
    #         'venue': row['venue'],
    #         'starttime': row['starttime'],
    #         'endtime': row['endtime'],
    #         'invitation': row['invitation'],
    #         'image': row['image'],
    #         'attendees': row['attendees'],
    #         'planner': row['planner'],
    #         'items': row['items'],
    #         'notes': row['notes'],
    #     } 
    #         for row in contents
    #     }
    all_events = database.get_events()
    
    if event_id in all_events:
       

    #         one_event = all_events[event_id]

    #         name = event_id
    #         date = one_event['date']
    #         venue = one_event['venue']
    #         starttime = one_event['starttime']
    #         endtime = one_event['endtime']
    #         invitation = one_event['invitation']
    #         one_image = one_event['image']
    #         attendees = one_event['attendees']
    #         planner = one_event['planner']
    #         items = one_event['items']
    #         notes = one_event['notes']

         return render_template('event.html', event_id=database.get_name(), event=database.get_event(), date=database.get_event(), venue=database.get_venue(), starttime=database.get_event(), endtime=database.get_event(), invitation=database.get_event(), image_path=database.get_event(), attendees=database.get_attendees(), planner=database.get_planner(), items=database.get_event(), notes=database.get_event())
    #     else:
    else:
        return render_template("events.html", events=all_events) 
    
def delete(person_id):
    database.remove_attendee_event(person_id)
    database.redirect()

def add(person_id):

    if request.method == "POST":
        database.add_person(person_id)
        database.redirect()
    else:
        database.add_person(person_id)
        database.redirect()

@app.route("/venues/")
def get_venues():

    '''accesses each item in the venues dictionary for use in the venues page'''
    # with open("venues.csv", encoding='UTF-8-sig') as csvfile:
    #     contents = csv.DictReader(csvfile)

    #     all_venues= {
    #         row['name']: {
    #         'name': row['name'],
    #         'address': row['address'],
    #         'phone': row['phone'],
    #         'fee': row['fee'],
    #         'attendees': row['attendees'],
    #     } 
    #         for row in contents
    #     }
    all_venues = database.get_venues()
    return render_template("venues.html", venues=all_venues)

@app.route("/events/add/", methods=['GET', 'POST'])
def add_event():

    '''adds an event to the events page when button pressed'''
    # if request.method == "POST":
      
    #     newEvent = ()

    #     print(newEvent)

        
    #     EVENT_PATH = 'events.csv'
    #     EVENT_KEYS = ['name', 'date', 'starttime', 'endtime', 'venue', 'invitation', 'attendees', 'planner', 'items', 'notes']

    #     return render_template('event_form.html', EVENT_PATH, EVENT_KEYS)
    # else:
    if request.method == "POST":
        newEvent = database.add_event()
        return render_template('event_form.html', newEvent)
    else:
        return render_template('event_form.html')

@app.route("/events/edit/")
@app.route("/events/<event_id>/edit/")
def edit_event(event_id=None):
    '''edits an event in the events page when button pressed'''
    # with open("events.csv", encoding='UTF-8-sig') as csvfile:
    #     contents = csv.DictReader(csvfile)

    #     all_events= {
    #         row['name']: {
    #         'name': row['name'],
    #         'date': row['date'],
    #         'venue': row['venue'],
    #         'starttime': row['starttime'],
    #         'endtime': row['endtime'],
    #         'invitation': row['invitation'],
    #         'image': row['image'],
    #         'attendees': row['attendees'],
    #         'planner': row['planner'],
    #         'items': row['items'],
    #         'notes': row['notes'],
    #     } 
    #         for row in contents
    #     }
    
    #     if event_id in all_events.keys():

    #         one_event = all_events[event_id]

    #         name = event_id
    #         date = one_event['date']
    #         venue = one_event['venue']
    #         starttime = one_event['starttime']
    #         endtime = one_event['endtime']
    #         invitation = one_event['invitation']
    #         one_image = one_event['image']
    #         attendees = one_event['attendees']
    #         planner = one_event['planner']
    #         items = one_event['items']
    #         notes = one_event['notes']

    #         return render_template('event.html', event_id=name, event=one_event, date=date, venue=venue, starttime=starttime, endtime=endtime, invitation=invitation, image_path=one_image, attendees=attendees, planner=planner, items=items, notes=notes)
    #     else:
    all_events = database.get_events()
    if event_id in all_events:
        one_event = all_events[event_id]
        name = event_id
        date = one_event['date']
        venue = one_event['venue']
        starttime = one_event['starttime']
        endtime = one_event['endtime']
        invitation = one_event['invitation']
        one_image = one_event['image']
        attendees = one_event['attendees']
        planner = one_event['planner']
        items = one_event['items']
        notes = one_event['notes']
        return render_template('event.html', event_id=name, event=one_event, date=date, venue=venue, starttime=starttime, endtime=endtime, invitation=invitation, image_path=one_image, attendees=attendees, planner=planner, items=items, notes=notes)
    else:
        return render_template("event_form_edit.html") 

@app.route("/events/delete/", methods=['GET', 'POST'])
@app.route("/events/<event_id>/delete/")
def delete_event(event_id=None):
    '''my ATTEMPT at what deleting the event would look like'''
    # if request.method == "POST":
        
    #     deleteEvent = ()

    #     print(deleteEvent)

    #     EVENT_PATH = 'events.csv'
    #     EVENT_KEYS = ['name', 'date', 'starttime', 'endtime', 'venue', 'invitation', 'attendees', 'planner', 'items', 'notes']

    
    #     with open("events.csv", encoding='UTF-8-sig') as csvfile:
    #         contents = csv.DictReader(csvfile)

    #         all_events= {
    #             row['name']: {
    #             'name': row['name'],
    #             'date': row['date'],
    #             'venue': row['venue'],
    #             'starttime': row['starttime'],
    #             'endtime': row['endtime'],
    #             'invitation': row['invitation'],
    #             'image': row['image'],
    #             'attendees': row['attendees'],
    #             'planner': row['planner'],
    #             'items': row['items'],
    #             'notes': row['notes'],
    #         } 
    #             for row in contents
    #         }
        
    #         if event_id in all_events.keys():

    #             one_event = all_events[event_id]

    #             name = event_id
    #             date = one_event['date']
    #             venue = one_event['venue']
    #             starttime = one_event['starttime']
    #             endtime = one_event['endtime']
    #             invitation = one_event['invitation']
    #             one_image = one_event['image']
    #             attendees = one_event['attendees']
    #             planner = one_event['planner']
    #             items = one_event['items']
    #             notes = one_event['notes']

    #             return render_template('events.html', event_id=name, event=one_event, date=date, venue=venue, starttime=starttime, endtime=endtime, invitation=invitation, image_path=one_image, attendees=attendees, planner=planner, items=items, notes=notes)
    #         else:
    #             return render_template('events.html', EVENT_KEYS, EVENT_PATH)
    # else:
    #     with open("events.csv", encoding='UTF-8-sig') as csvfile:
    #         contents = csv.DictReader(csvfile)

    #         all_events= {
    #             row['name']: {
    #             'name': row['name'],
    #             'date': row['date'],
    #             'venue': row['venue'],
    #             'starttime': row['starttime'],
    #             'endtime': row['endtime'],
    #             'invitation': row['invitation'],
    #             'image': row['image'],
    #             'attendees': row['attendees'],
    #             'planner': row['planner'],
    #             'items': row['items'],
    #             'notes': row['notes'],
    #         } 
    #             for row in contents
    #         }
        
    #         if event_id in all_events.keys():

    #             one_event = all_events[event_id]

    #             name = event_id
    #             date = one_event['date']
    #             venue = one_event['venue']
    #             starttime = one_event['starttime']
    #             endtime = one_event['endtime']
    #             invitation = one_event['invitation']
    #             one_image = one_event['image']
    #             attendees = one_event['attendees']
    #             planner = one_event['planner']
    #             items = one_event['items']
    #             notes = one_event['notes']

    #             return render_template('events.html', EVENT_KEYS, EVENT_PATH)
    #         else:
    all_events=database.get_events()
    if event_id in all_events:
        delete = database.delete_event()
        return render_template('events.html', delete)
    else:
        return render_template('events.html') 

@app.route("/people/add/", methods=['GET', 'POST'])
def add_people():
    '''adds a person to the people page when button pressed'''
    # if request.method == "POST":
      
    #     newPeople = ()

    #     print(newPeople)
        
    #     PEOPLE_PATH = 'people.csv'
    #     PEOPLE_KEYS = ['name', 'address', 'email', 'birthday', 'phone']

    #     return render_template('people_form.html', PEOPLE_PATH, PEOPLE_KEYS)
    # else:



    add = database.add_people()
    return render_template('events.html', add) 

@app.route("/venues/add/", methods=['GET', 'POST'])
def add_venue():
    '''adds a venue to the venues page when button pressed'''
    # if request.method == "POST":
      
    #     newVenue = ()

    #     print(newVenue)
        
    #     VENUE_PATH = 'venues.csv'
    #     VENUE_KEYS = ['name', 'address', 'phone', 'fee', 'attendees']

    #     return render_template('venue_form.html', VENUE_PATH, VENUE_KEYS)
    # else:
    add = database.add_venue()
    return render_template('venue_form.html', add)

