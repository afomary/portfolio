#⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡

import random #import random to use later

#⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ PART1 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆

titles = input('Enter titles for the videos in your channel  ♡ : ') #getting video names from user
titles = titles.split() #breaking the input up into seperate elements in a list (aka different accessible videos)
print(titles) #display video titles !

#⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ PART2 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆

videos = {} #empty dictionary where i'll put the video title with it's duration (ex: 'myvideo': 4 )

length_list = [] #list where it stores the lengths of all the videos so i can have it one uncomplicated place to find the minimum, maximum, and average !
for title in titles: #for each video
    length = float(input('Enter a length for this video (in minutes)  ♡ : ')) #float just incase of user input being non-int
    length_list.append(length) #put this entered length in length list
    videos[title] = length #throw this pair in the dictionary "videos" from earlier !

shortestvid = min(length_list) #self-explanatory 
longestvid = max(length_list) 
avgofvids = sum(length_list) / len(length_list)

print(shortestvid)
print(longestvid)
print("%.3f" % avgofvids) # print the average with 3 decimal points

#⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ PART3 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆

total_time_watched = 0 #initializing variables
video_views = {}
addaview = 0

subscribers = int(input('How many subscribers does your channel have ?  ♡ : '))   #enter subscribers plz
for subscriber in range(subscribers): #for each subscriber
    watch = random.choice(titles) #this specific subscriber will be watching this ONE specific video that was randomly picked
    duration = videos[watch] #accessing the key of the video that was just picked randomly so that we can get the duration
    total_time_watched += duration #adding that duration on to the total time watched
    addaview += 1 # plus one view
    video_views[watch] = addaview #putting this in the video views dictionary
print('Time spent between all videos (in minutes) ♡ : ', total_time_watched) #outputting our time spent after all iterations have finished !
print('Views per video ♡ : ', video_views) #display the dictionary so we can see how many views each specific video racked up !

#⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ PART4 ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆

rival_videos = {} #2 empty dictionaries to store both the rival's videos and the rival's views. (It is said in the instructions they only have one video, however.)
rival_views = {}
rival_subcount = random.randint(1, 100) #they could have anywhere between 1 and 100 subscribers in this day and age !!
rival_duration = random.randint(1, 5) #the length of their one video could be 1 2 3 4 or 5 minutes long 
rival_videos['enemyvideo'] = rival_duration #adding their one video in pair with its duration to the rival videos dictionary
total_time_rival = 0 #initializing their subscribers total time watching their videos

for sub in range(rival_subcount): #for each subscriber in my rivals subscriber count,
    total_time_rival += rival_duration #add the duration of the video watched by each subscriber on to the total !
    
#state my rivals total and state my total
print('Your competitors subscribers have watched ', total_time_rival, 'minutes of their content, while your subscribers have watched', total_time_watched, 'minutes of your content ! ♡ ')

#if else statements to show who has more views, aka who's numbers are bigger. If equal, then its a tie !
if total_time_rival > total_time_watched:
    print('Your rival has more views than you :( ♡ !')
elif total_time_watched > total_time_rival:
    print('You have more views than your rival :) ♡ !')
else:
    print('You are tied with your competitor ! ♡')
    
#words of positive affirmation to encourage myself to keep growing this youtube channel either way !
print('Keep it up! ♡')

#⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆

# #⠀⠀⢐⠑⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠈⠐⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡅⠀⠀⠀⠀⠈⠒⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⡀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠈⠢⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⠔⠂⠁⠀⢰⠁⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠔⠂⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⢄⠀⠀⠀⠀⢀⡠⠄⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡑⣒⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⣞⠟⡋⡉⠍⡉⠍⠛⠛⠶⣦⣤⡀⠀⣀⣀⣀⣀⠀⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢀⣴⡞⢯⣑⠞⠡⠌⡐⠁⠎⢄⡉⠌⡑⡐⠠⡈⢛⢻⣭⡐⡈⢉⠻⢳⣄⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⢀⣴⡟⢣⡚⣥⠋⠄⢃⠌⠰⣩⠶⣤⠐⣈⠐⣠⡿⢳⡆⠠⠙⢿⣷⡀⠢⢁⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣰⡟⣇⠺⣡⢳⠃⠌⠨⠄⢊⢼⡏⠀⢹⡆⡐⢂⣾⡁⠀⢿⡁⠌⡐⠘⣿⣂⠂⠤⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⢀⣴⡿⡑⣎⡱⢥⠇⠌⠂⠥⠘⢠⢸⣧⠀⢸⣧⠐⡡⢿⣇⠀⣼⡇⠒⣈⠡⠘⣿⣀⢳⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠔⠁⣠⣴⠟⣥⢃⠷⣐⢣⢛⢀⠊⣁⠢⠉⠄⠚⣿⣿⣿⣿⢂⢁⢺⣿⣿⣿⣏⠡⠐⢂⠅⢚⣧⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⣴⠿⣡⠏⢦⡙⢦⡙⢦⠃⠌⡐⡀⠆⣉⡘⠄⢻⣿⣿⡟⡇⠠⠊⣿⣿⣿⠇⣢⢽⠲⣞⣤⢿⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⡠⠒⠁⠀⠀⠀⢴⢏⠧⣱⢊⠧⣜⡡⢞⣡⠋⢄⠑⢴⡻⢍⡝⣳⠌⠻⠿⢡⢄⠃⣰⣨⠟⠋⢠⠻⣬⣳⠬⢃⢻⠄⠑⠄⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⣀⠔⠁⠀⠀⠀⠀⠀⣾⢜⡰⣍⠺⢤⢍⠳⢬⡙⣲⠈⠔⡘⠧⠾⠵⠛⡀⠆⢠⠘⠾⠶⠟⢋⠀⠆⠌⡠⢉⠉⠤⢈⣾⠀⠀⠐⢄⠀⠀⠀⠀⠀⠀⠀
# ⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⣿⢎⠲⣌⡓⢎⣎⢹⣂⠳⣙⡌⠰⠐⠰⠀⠆⢡⠐⠌⢂⠌⠒⡈⠒⡈⠰⢈⡐⢁⠂⣉⠐⣂⡿⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀
# ⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣕⡢⢝⠲⣌⠶⣈⠗⣡⡻⡄⠡⡁⠎⡈⢄⠊⠄⠃⢌⢂⠡⢂⡑⠌⠄⡂⠌⡰⢀⠒⣼⠃⠀⠀⠀⠀⠀⠀⠢⡀⠀⠀⠀
# ⠀⠀⠉⠒⠒⠤⢀⣀⠀⠀⠀⠀⠙⠛⠮⠷⠬⣶⡝⡞⡍⢶⡙⣆⠔⡐⠠⢂⠘⡈⢡⠂⢂⠡⠂⠔⡈⢂⠔⠡⢐⢠⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠒⠢⠤⣀⣀⠀⣀⣽⣷⣬⠙⢦⡙⣬⠳⣄⡑⠠⢂⠁⠆⣈⠂⢡⠉⡐⠤⠁⡌⠐⣦⣿⡿⣿⢿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠘⠄
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣦⣹⢄⡛⡴⣙⠶⡥⣌⣂⡄⡘⣀⣂⣡⢦⣓⣶⣿⡿⣿⡽⣯⢿⣽⣻⢿⣦⣄⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣴⣳⣌⠶⡑⣎⢲⢩⡜⣥⣳⣼⣶⣿⣿⢯⣟⡷⣿⣽⣻⡾⣽⣯⣟⡿⣷⡖⠒⠒⠂⠀
# ⠀⠀⠀⠀⠀⠀⠀⣀⣠⢤⡴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣻⣿⣿⣿⣿⣿⣿⡿⣽⣻⢷⣯⢷⣟⡿⣾⣽⣻⡽⣿⡄⠀⠀⠀
# ⠀⠀⠀⠀⠀⢰⡿⣵⣫⢯⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣹⢞⡵⡿⣿⣿⣿⣿⣿⣿⣿⣽⣻⢾⣻⣾⣻⢷⣯⢷⣿⡿⠁⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠉⠓⠯⠯⣳⣏⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢻⡝⣾⡱⣯⣟⠷⣭⡻⣝⡿⢿⡿⣿⣿⣿⣿⣷⣯⣿⠿⠾⠛⠉⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠑⠛⠛⠙⠿⠿⠿⠿⠟⢿⢻⣟⣽⣣⣟⣮⣗⣯⣳⣯⣟⡶⠯⠷⠽⠷⠾⠷⠝⠛⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⢀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
