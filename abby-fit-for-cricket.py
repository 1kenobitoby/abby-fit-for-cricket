import streamlit as st
import time
import random
import pandas as pd

# pick 6 rows at random from number of rows in 'table' (i.e. range(0, len(table)) ) and put in list 'choices'
# cache data so it only runs 1st time and doesn't re-run every time user clicks something
@st.cache_data
def choose():
    choices = random.sample(range(0,len(table)), 6)
    return choices

st.set_page_config(
    page_title="Abby fit for cricket",
    page_icon="images/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
    #menu_items={
        #'Get Help': '<<URL>>',
        #'Report a bug': "<<URL>>",
        #'About': "Made with Streamlit v1.27"
    #}
)

# Get struct_time and strip full weekday name from it (%A)
day=time.strftime("%A", time.localtime())

st.image('images/logo.svg', width=100)
st.header(day + "'s exercises")
st.write("1 minute per exercise, slow and controlled, focussing on quality of movement.")

# a dictionary of 3 lists: 1. Exercise names; 2. Video URLs showing how to perform the exercises; 3. The start time in seconds of the relevant bit in the video
database={
    'Exercise name': ["Curl up", "Bird dog", "Side plank", "Knee off bed", "Scorpion roll", "SI joint corkscrew", "Windscreen wiper/piriformis rolls", "Donkey kicks", "90\u2070:90\u2070 sacrum lifts", "Single leg squats", "Clam shells", "Fire hydrants", "Bridges/thrusts/donkey kicks", "Side lying hip abduction", "90\u2070 wall ball roll", "Ball-wall deadlift", "Copenhagens", "Ball squeeze glute bridges", "Banded butterfly bridges", "Reverse lunge step ups"],
    'Video':["https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=7KYfGH8daJk", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=Qhk6nrorgT8", "https://www.youtube.com/watch?v=Qhk6nrorgT8", "https://www.youtube.com/watch?v=CjinhqRzcaY", "https://www.youtube.com/watch?v=s2bqEP1O6_s", "https://www.youtube.com/watch?v=s2bqEP1O6_s", "https://www.youtube.com/watch?v=Siw3bgdJE80"],
    'Start time':[68, 295, 205, 58, 322, 447, 604, 524, 169, 686, 474, 490, 505, 524, 279, 397, 0, 430, 334, 111]
}

# Pass database to pandas dataframe constructor to make 'table'
# Table has a row for each exercise showing name, video URL and start time in video
table = pd.DataFrame(database)

# call chose function which picks 6 exercises at random from the table
exercises = choose()
#exercises

#initialise counter 'number'
number=0

# Loop through pulling the exercise name from column 1 to put in the Streamlit tab called tab_text
# then pull the associated video URL from column 2 and set the start time from column 3
for i in exercises:
    number +=1
    tab_text, tab_video = st.tabs(["Exercise " + "%.0f" % number, "Video"])
    with tab_text:
        st.write(f"**{table.iloc[i, 0]}**")
        st.write("\n")

    with tab_video:
        st.video(table.iloc[i, 1], start_time=table.iloc[i,2]) 

st.divider()


# Some gym workout schedules and YouTube stretching routines, 1 for each day of the week, to follow.
st.header('Today\'s workout')

if day=="Saturday":
    selected = st.radio("Your choice today. What do you feel like doing?", ["I need a rest", "HIIT me", "Abby ab work", "Hip, glute & booty workout", "Relaxing yoga", "Step on"], index=None)
    if selected=="I need a rest":
        st.write("OK, see you tomorrow")
    elif selected=="HIIT me" :
        st.video("https://www.youtube.com/watch?v=M0uO8X3_tEA")
        st.write('Lots more like this at  [Juice & Toya\'s YouTube channel](https://www.youtube.com/@JuiceandToya/videos)')
        st.write("It\'s a good channel because she tends to do lower impact modifications while he goes a bit more intense alongside her so you can find a manageable level.")
    elif selected=="Abby ab work":
        st.video("https://www.youtube.com/watch?v=D6etUH5j2MA")
        st.write("[Move with Nicole](https://www.youtube.com/@MoveWithNicole/videos) is a good channel if you find you like pilates with videos for all body areas")
    elif selected == "Hip, glute & booty workout":
        st.video("https://www.youtube.com/watch?v=Pf98VQ0n7jg")
        st.write('Lots more like this on the  [Janekate Fitness YouTube channel](https://www.youtube.com/@JanekateFitness/videos)')
        st.write("Although the focus of this channel is 'bubble butt' looks, the exercises in these videos are great for your 'rear chain' (the hamstrings, glutes and lumbar spine muscles) which fast bowlers need strength in to prevent injuries.")
    elif selected == "Relaxing yoga":
        st.video("https://www.youtube.com/watch?v=ZSSC9X_6wo4", start_time=43)
        st.write("If you get into yoga, there are live classes several times a week in the village hall.")
    elif selected == "Step on":
        st.video("https://www.youtube.com/watch?v=u7c3CtrPKbc")
        st.write('Lots more step workouts like this at  [Get Fit With Rick\'s YouTube channel](https://www.youtube.com/@RickBhullarFitness/videos)')           
elif day=="Sunday":
    st.write('20 minutes of calisthenic strength work.')
    st.video("https://www.youtube.com/watch?v=nB0D1a0oC-A")    
elif day=="Monday":
    st.write('20 minutes of full body mobility and stretching.')
    st.video('https://www.youtube.com/watch?v=8fipKUJzcuk')
elif day=="Tuesday":
    st.write("See you at 8pm for training on the tennis courts.")
elif day=="Wednesday":
    st.write('15 minutes of hardcore calisthenic strength work.')
    st.video("https://www.youtube.com/watch?v=gnTzk1yUHB4", start_time=58)
    st.write('Chris Heria\'s stuff is great but it\'s properly hardcore. Start maybe doing just 20 seconds on, 40 seconds rest using the regression exercises and build it up from there.')
    st.write('If even that is too much at first though, try [this one](https://www.youtube.com/watch?v=XX1-nL9oM2E) which does similar exercises in two identical rounds. Start by doing just the first round, moving on to the full thing when you are ready.')
elif day=="Thursday":
    st.write('Relax. Breathe deep, get into your own head and feel your chakras. 20 minutes of yoga.')
    st.video('https://www.youtube.com/watch?v=b1H3xO3x_Js')
    st.write('Lots more like this at  [Adriene\'s YouTube channel](https://www.youtube.com/@yogawithadriene/videos)')
else:
    st.write('Running Foxes or indoor cricket tonight so no workout today.') 


