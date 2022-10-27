import streamlit as st
from PIL import Image
# from streamlit_player import st_player

# icon = Image.open('pro1.png')
st.set_page_config(layout = 'wide', page_title="My Profile",page_icon='pro1.png')

col1, col2, col3, = st.columns([0.5, 1, 0.05])
col2.header('Akinsida Anthony Stephen')
col2.write('---')
# col2.header('Akinsida Anthony Stephen')

col1, col2 = st.columns(2)
          
with col1:
        st.header('My Preambles')

        hold, tab1, tab2, tab3, tab4 = st.tabs(['Hold','Profile Summary','Contact', "Skills", "Accomplishments"])
        with tab1:
            st.write('''Analytical thinker leverages problem-solving skills to drive continuous improvement. 
            Works cross-functionally to adapt systems to changing business needs and formulate winning 
            solutions. Adept at using Python and R programming Languages.''')
        with tab2:
            st.write('''**CITY:**''')  
            st.caption('Salford Manchester') 
            st.write('**POSTCODE:**')  
            st.caption('M5 5AD')
            st.write('**PHONE:**')
            st.caption('+447867379457')
            st.write('**EMAIL ADDRESS**')
            st.caption('akinsidaanthony@gmail.com')
        with tab3:
            st.write('''  
            - Data wrangling  
            - Data mining  
            - Statistical Analysis  
            - Machine Learning  
            - Data Visualization   
            - Business Intelligence 
            - Dashboard Creation  
            - Teaching and Mentoring''')
        with tab4:
            st.write('''
            - Develop data pipeline and standard data handling processes 
            - Implementing standards operating procedures across departments for increased productivity.  
            - Created Systems to increase revenue and reduce costs  
            - I have mentees all over the world
            - Able to teach Python and R programming languages together''')


with col2:
        st.header('Education Experience and Lifestyle')

        hold, tabA, tab1, tab3 = st.tabs(['Hold','Education/Training', "Work Experience", "Hobbies/Lifestyle"])

        with tabA:
            st.write('2006, University of Lagos Nigeria')
            st.caption('Msc Economics')
            st.write('2004, University of Lagos Nigeria')
            st.caption('Post Graduate Diploma Manpower, Economics and Planning')
            st.write('2002, University of Ado Ekiti Nigeria')
            st.caption('Bachelor of Arts Degree in Philosophy')
        
        with tab1:
            struc = st.radio(label = 'Select a Topic', options = ['Data/Research Analyst Related Jobs',
                                                            'Teaching and Mentorship',
                                                            "Support Worker's Role",
                                                            ])
            st.write('---')
            if struc == 'Data/Research Analyst Related Jobs':
                st.write('''  
March 2018 - Current  
Data Analyst   
Alliance and Frontier Limited Lagos Nigeria 

April 2014 - August 2018  
Research Analyst  
Dominion Research Solutions Lagos Nigeria

January 2009 - February 2014  
Research Manager  
Primewaterview Limited Lagos
''')
                st.write('''- Analysed operational improvements against KPIs to measure progress.  
- Analysed and tracked data to prepare forecasts and identify trends.    
- Conducted data modelling and statistical analysis to note trends and draw conclusions.    
- Collaborated cross-functionally with diverse teams in cleaning, assessing and interpreting data.
- Evaluated performance data and established benchmarks for future tracking.  
- Contributed to data capture, storage and forecast for analysis projects.  
- Evaluated complex data sets to identify business opportunities and threats.
---
- Aided company strategy through large-scale data consolidation, analysis and evidence presentation.
- Developed charts and graphs on research findings to assess trends, presenting findings to management.
- Assessed research to evaluate and determine trends and anomalies for further investigation.
- Used data collected from research projects to make smart decisions when moving forward with business activities.
- Conducted targeted research based on policy and process improvement goals, supporting company growth.
- Informed and influenced policymakers through strategic research, reporting and analysis.
- Designed and coordinated diverse qualitative and quantitative research, aiding business improvement strategies.
- Improved project processes and operations through detailed advice from quantitative data findings.
- Analysed data to determine opportunities for growth and greater efficiency.
- Used various approaches to gathering and assessing data, including trend analysis, consumer research and best practice reviews.
- Used data collected to form strategies to successfully grow business by 20%.
- Developed competitive insight through strategic data capture, enhancing overall market intelligence.
- Applied mathematical and programmatic methods to perform data extraction, cleansing and manipulation.
''')

            if struc == 'Teaching and Mentorship':
                st.write('''
September 2005 - Current  
Teacher/Mentor  
Self-Employed 

April 2005 - March 2006 
Teaching Assitant
University of Lagos 
- Sourced and developed a wide range of creative materials required for lessons, including workbooks, quizzes, games and presentations.
- Monitored and documented student grades, behaviour and participation.
- Monitored student development by marking coursework, monitoring classroom activities and assessing student behaviour.
- Taught a wide range of subjects to students aged 9 - 30 in subjects, including Maths, Economics Data Science.
- Planned educational events, trips, outings, clubs and activities to support Data Science curriculum.
- Enhanced student outcomes by providing extra tutoring, mentoring and training support to underachieving students.
- Created software application as lesson notes to help students to aid developments
- Maintained excellent student relationships by providing a safe, positive learning environment for students.
- Motivated students to achieve maximum potential through ongoing encouragement and providing extra support where needed.
- Maintained strong student relationships by providing safe, positive learning environments for students.
''')

            if struc == "Support Worker's Role":
                st.write('''
2021 - Current
Support Worker: Part-time(Night Shifts)
- Lending helping hands to medical staff in mental heatlh homes and hospitals
- I am a certified Prevention Management of Violence and Aggression support staff
'''
)
                logo = Image.open('PMVA.png')
                st.image(logo,width= 100,caption = 'PMVA Certificate')
                if st.button('Enlarge Certificate'):
                    st.image(logo,width=500,caption= 'PMVA Certificate')
                    st.button('Close')




        with tab3:
            pas = Image.open('p2.png')
            st.image(pas,width= 250,caption = 'Profile Picture')
            # logo = Image.open('mo1.jpg')
            # st.image(logo,width= 250,caption = 'My Daughter')
            st.write('''My personal lifestyle revolves around: My Family, My Students, My Laptops and 
            Arsenal Footbal Club. Meaning you can guess my location at any particular time of the day when I am not at work.
            ''')
            
            logo = Image.open('mo2.jpg')
            st.image(logo,width= 250,caption = 'My daughter')

            st.write('''Dont blame me if i troll Tottenham fans about their empty trophy cabinet, I
            get trolled by Manchester United and Liverpool fans too. Annoyingly, Chelsea fans troll
            me about my lack of trophies in Europe. I am always very happy to get one over Tottenham because
            they are my next-door neigbours.''')
            # st_player('https://www.youtube.com/watch?v=l3z_gICq-CQ',height=290)

            st.video('https://www.youtube.com/watch?v=l3z_gICq-CQ', 'rb')
            
            
