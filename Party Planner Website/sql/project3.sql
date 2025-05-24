
CREATE TABLE events (event_id VARCHAR(80) PRIMARY KEY, date DATE(20), venue VARCHAR(50), starttime TIME, endtime TIME, invitation VARCHAR(100), image VARCHAR(40), attendees VARCHAR(10), planner VARCHAR(20), items VARCHAR(20), notes VARCHAR(100)) ENGINE=INNODB;
CREATE TABLE venues (venue_id VARCHAR(80) PRIMARY KEY, address VARCHAR(80), phone VARCHAR(20), fee INT, attendees VARCHAR(10)) ENGINE=INNODB;
CREATE TABLE people (person_id VARCHAR(80) PRIMARY KEY, address VARCHAR(80), email VARCHAR(40), birthday VARCHAR(30), phone VARCHAR(20), role VARCHAR(10)) ENGINE=INNODB;

INSERT INTO events (event_id, date, venue, starttime, endtime, invitation, image, attendees, planner, items, notes) VALUES 
("Berry Sweet Berry Bash", "10/25/23", "Strawberryville", "7:00 PM", "9:00 PM", "You've been invited to Strawberry's Berry Sweet Berry Bash!", "images/strawberry.jpg", "7", "Bubblegum", "3 tents", "Make it super sweet for all my fruity friends!"),
("Wicked Cool Whip Dinner", "10/30/23", "Quahog", "10:00:00PM", "11:00:00PM", "You've been invited to Stewie Griffin's wicked Cool Whip dinner!", "images/stewie.jpg", "20", "Finn", "20 chairs", "Make it ABSOLUTELY wicked and vile. Also don't let Lois in. Or Quagmire."),
("Halloween Pastry Party", "10/31/23", "Kitty's Cafe", "08:00:00PM", "09:00:00PM", "You've been invited to Hello Kitty's Supercute Halloween Pastry Party!", "images/hellokitty.jpg", "10", "Marceline", "2 tables", "Make it super cute for all my sanrio friends!"),
("All Night Rager", "11/04/23", "My Crib", "11:00:00PM", "07:00:00AM", "You've been invited to Muscle Man's all-night rager!", "images/muscleman.jpg", "400", "Jake", "1 PA system", "I don't care what you do just make sure my mom's there."),
("Y2K Juicy Couture Launch", "11/07/23", "The Hilton Hotel", "11:30:00PM", "01:00:00AM", "You've been invited to Paris Hilton's y2k-themed juicy couture launch!", "images/parishilton.jpg", "1000", "LSP", "1 stage", "Make it high fashion make it hot."),
("Gnarly Marathon Surf-Off", "11/11/23", "Surfer's Paradise", "06:00:00PM", "12:00:00AM", "You've been invited to Broseph's gnarly marathon surf-off! High tide's at midnight", "images/broseph.jpg", "444", "BMO", "10 lights", "Make it gnarly dude no kooks groms only!");
INSERT INTO venues (venue_id, address, phone, fee, attendees) VALUES
("Strawberry Shortcake's House", "286 Front Ave", "500-500-5331", "$5", "20"),
("Stewie's House", "31 Spooner Street", "123-456-7890", "$10", "30"),
("Hello Kitty Cafe", "1234 Supercute Avenue", "404-404-4004", "$15", "20"),
("Muscle Man's Crib", "403 My Mom Lane", "370-777-7777", "$20", "400"),
("The Hilton Hotel", "90210 McBling Drive", "902-102-1000", "$25", "1000"),
("Surfer's Paradise", "101 Hang Ten Boulevard", "101-404-8008", "$30", "303");
INSERT INTO people (person_id, address, email, birthday, phone, role) VALUES
("Strawberry Shortcake", "Beryville Road", "strawberrycakeshort@gmail.com", "01/01/2001", "123-321-2342", "customer"),
("Stewie Griffin", "31 Spooner Street", "stewieworlddomination@gmail.com", "05/31/2002", "202-002-0202", "customer"),
("Hello Kitty", "412 CutiePoo Drive", "hellokittysanrio@gmail.com", "10/31/2003", "400-020-4000", "customer"),
("Muscle Man", "555 ShirtRipper Peak", "mymom@gmail.com", "02/14/2004", "555-555-5555", "customer"),
("Paris Hilton", "404 Richie Road", "parishiltonbaby@gmail.com", "04/19/2005", "901-909-9191", "customer"),
("Broseph", "107 Kowabunga Creek", "brosephgnarly@gmail.com", "07/16/2006", "101-111-1444", "customer");

CREATE TABLE attendees (name VARCHAR(30), address VARCHAR(40), email VARCHAR(30), phone VARCHAR(14), dob VARCHAR(13)) ENGINE=INNODB;

INSERT INTO attendees (name, address, email, phone, DOB) VALUES
("Sailor Moon", "222 Crystal Avenue", "sailormoon@gmail.com", "222-222-2222", "1999-01-01"), 
("Starfire", "111 Titan Towers", "starfire@gmail.com", "111-111-1111", "2003-08-01"),
("The Crimson Chin", "444 Red Road", "doublecee@yahoo.com", "444-444-4444", "1982-05-21");