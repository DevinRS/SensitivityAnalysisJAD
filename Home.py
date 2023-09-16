import streamlit as st
from PIL import Image

st.set_page_config(page_title='KU JAD 2023-24', page_icon='🏆')

st.sidebar.success('Select Mission Above 👆')
st.sidebar.title('Table of Contents')
st.sidebar.markdown("[Summary](#summary)", unsafe_allow_html=True)
st.sidebar.markdown("[General Information](#general-information)", unsafe_allow_html=True)
st.sidebar.markdown("[Schedule](#schedule)", unsafe_allow_html=True)
st.sidebar.markdown("[Fly-off Site](#fly-off-site)", unsafe_allow_html=True)
st.sidebar.markdown("[Mission and Vehicle Design](#mission-and-vehicle-design)", unsafe_allow_html=True)
st.sidebar.markdown("[Reports](#reports)", unsafe_allow_html=True)
st.sidebar.markdown("[Scoring](#scoring)", unsafe_allow_html=True)


st.title('Jayhawk Aero Design')
st.header('AIAA 2023-2024')
st.write('The objective for this year is to design, build, and test an airplane to demonstrate Urban Air Mobility (UAM) missions. Flight missions will include delivery of the airplane, medical transport, and urban taxi.')
st.subheader('👉[Rules](https://www.aiaa.org/docs/default-source/uploadedfiles/aiaadbf/resources/dbf-rules-2024-draft-4.pdf?sfvrsn=8d6c3a8a_0)')

st.subheader('Summary')
with st.expander('Summary'):
    st.write('''
    The AIAA through the Applied Aerodynamics, Aircraft Design, Design Engineering and Flight Test Technical
    Committees and the AIAA Foundation invites all university students to participate in the Textron Aviation/Raytheon
    Student Design, Build, Fly Competition. The contest will provide a real-world airplane design experience for
    engineering students by giving them the opportunity to validate their analytic studies.
                
    Student teams will design, fabricate, and demonstrate the flight capabilities of an electric powered, remote-
    controlled airplane that can best meet the specified mission profile. The goal is a balanced design possessing good
    flight handling qualities and practical and affordable manufacturing requirements while demonstrating high vehicle
    performance.
                
    To encourage innovation and maintain a fresh design challenge, the design requirements and performance objectives
    are updated for each new contest year. The changes provide new design requirements and opportunities, while
    allowing for application of technology developed by the teams from prior years.
                
    Check the rules package carefully as items and approaches that were legal in past years may not be legal for this
    contest year. Only the contents of this year's Rules package along with the current FAQ and Q&A documents hold
    bearing on the requirements and/or allowances for the current contest year.
                
    NOTE: Items in the rules that are critical to the safety and execution of the competition or are new are hi-lighted
    in RED text. Please take note of these requirements and rules.
                
    It is the responsibility of the teams to know and follow all provided rules, the FAQ and Q&A, and all contest day
    briefings.
                
    Cash prizes are 3000 for 1st, 2000 for 2nd and 1500 for 3rd place. The winning team(s) may be invited to present
    their design at AIAA's AVIATION Forum. The team with the best Report Score will receive a 100 prize from the
    Design Engineering Technical Committee.
             
    ''')

st.subheader('General Information')
with st.expander('Team Requirements'):
    st.write('''
All team members (except for a non-student pilot) must be full time students at an accredited University or College
and student members of the AIAA. Team members may include graduate students. At least 1/3 of the team
members must consist of freshman, sophomores or juniors (below senior year, for non-four year programs). The
pilot must be an AMA (Academy of Model Aeronautics) member. Teams may use a non-university member for the
pilot if desired. Qualified, volunteer pilots will be available at the contest on an as-available basis to assist teams who
are unable to have their pilot attend.
             
There is no set requirement for the number of students that must attend the fly-off. It is preferred, but not required,
for the team advisor or responsible faculty member to attend.
             
Team members may be updated/changed at any time during the contest but must always comply with the 1/3 rule.
Following the initial team roster submitted with the contest entry, a “One Time” update to the official team roster
may be submitted with the Design Report in February.
             
Each educational institution may submit one (1) team entry.
             
The team members may be changed during the contest period, so schools may use an internal selection process to
determine their final design and team members prior to the written report submission and fly-off. For schools with
multiple campuses in different cities each campus will be considered as a separate entity.
             
Two or more schools may combine to submit a single entry.
             
Schools which already have an entry may not have additional students from their school participate as members of a
team from a different (shadow) school.
''')
with st.expander('Sponsorship'):
    st.write('''
Teams may solicit and accept sponsorship in the form of funds or materials and components from commercial
organizations. All design, analysis, major component fabrication and assembly of the contest entry airplane is the
sole responsibility of the student team members.
''')
with st.expander('Communications'):
    st.write('''
The contest administration will maintain a website containing the latest information regarding the contest schedules,
rules, and participating teams. The contest web site is https://www.aiaa.org/dbf
             
Questions regarding the contest, schedules, or rules interpretation may be sent to the contest administrator by email
at: director@aiaadbf.org
             
Please note that rules interpretation questions will not be answered by e-mail until after the entry date (when all
participant e-mail addresses are known), so that all teams will have equal access to all rules information.
Questions received prior to the entry deadline will not be answered and must be resubmitted after the entry
deadline. Official questions with answers received following the entry submission date will be posted on the website
Q&A and delivered by email to all teams.
             
The DBF Organizing Committee will utilize social media as an additional means of communicating with the teams
during the contest weekend only. This will NOT be a means of communicating rules, FAQ's, Q&A, protests, etc., but
only used in case of emergencies, weather delays or contest weekend schedule updates. Additional information will
be included in the contest information sheet to be sent out to the registered teams prior to the fly-off.
''')
with st.expander('Flight Line and Order'):
    st.write('''
A flight order list will be generated and emailed to the teams on the Wednesday prior to the fly-off weekend.
Teams will always rotate in this order. The flight order will be repeated continuously.
             
The flight order list will carry over from Thursday to Friday, Friday to Saturday, and Saturday to Sunday at whatever
spot in the rotation it leaves off. The flight order list is used for all queues during the contest. These queues include,
but are not limited to Tech inspection, Flight Line Missions, and Ground Missions. Note that the Organizing
Committee reserves the right to open up any of the queues to first-come-first-served if no teams come when called,
or return to the flight order if lines begin to form. This will be done at the sole discretion of the Organizing
Committee.
             
Each team's position in the flight order will be determined from their written report score, the highest report score
goes first.
             
Report scores will be available following the pilot briefing at the start of the contest (they will not be included with
the rotation sequence e-mail).
             
There will be staging box positions near the flight line.
             
If you are not ready to enter a staging box when your rotation number comes up, you will miss (forfeit) your
opportunity for that rotation.
             
Note: It is each team's responsibility to monitor the notifications from the scoring table in order to respond if
ready. Teams MUST Check-In with the scoring table before proceeding to the flight line. A contest official will be
available to help teams enter the staging box.
             
If you choose to leave the staging box for any reason, that is still considered a flight attempt, and you may not
attempt another flight until your turn comes up again in the rotation order.
''')
with st.expander('Flight Course'):
    st.write('''
The orientation (direction) of the flight course will be adjusted based on the prevailing winds as determined by the
Flight Line Judge. The flight course will be positioned to maintain the greatest possible safety to personnel and
facilities. The nominal flight course is shown in Figure 1 below.
''')
    image_flightcourse = Image.open('assets/flight_course.png')
    st.image(image_flightcourse, caption='Flight Course', use_column_width=True)
with st.expander('Protest Procedure'):
    st.write('''
Submitting a protest is a serious matter and will be treated as such. Teams may submit a protest to the Contest
Administration at any time during the competition. Protests MAY NOT be submitted after the conclusion of the
competition. Protests must be submitted in writing and signed by the registered team advisor; designees are not
allowed for protest submissions. If the team advisor is not present, he or she may send by electronic method a
signed protest to the team for them to present. Electronically submitted protests must be on hard copy (printed by
the team) and have the advisor's signature. A phone number where the advisor may be contacted must be provided.
Protests may be posted for review at the decision of the administration.
             
Protests and penalties (up to disqualification from the contest for deliberate attempts to misinform officials, violate
the contest rules, or safety infractions) will be decided by the Contest Administration. Protests submitted but not
upheld by the judges may be given a penalty of the loss of one flight score to the team submitting the protest. The
decision of the Contest Administration is final.
             
Teams may only protest events involving their own team. Protests against other teams or actions not specifically
involving their own team will not be accepted.
''')
with st.expander('Sportsmanship'):
    st.write('''
All teams and students participating in DBF are expected to uphold the highest standards of sportsmanship during
the competition and abide by the AIAA Code of Ethics (https://www.aiaa.org/about/Governance/Code-of-Ethics).
Attempts to intentionally violate the rules or negatively impact the performance of other teams will not be
tolerated. Penalties for violations will be decided by the Contest Administration and may range from a warning to
a loss of flight score up to disqualification from the current and future competitions
''')

st.subheader('Schedule')
with st.expander('Entries'):
    st.write('''
The entry period OPENS 15 October at 8AM (0800) US Eastern Time. No entries will be accepted before that time. A
completed entry must be RECEIVED by 5 PM (1700) US Eastern Time on 31 October. Entries will be collected through
the AIAA Online Submission System.
             
Proposals and Team Rosters must be submitted as part of the entry process. Proposals and Team Rosters will not be
accepted outside of the online submission system.
             
Be sure to include ALL required information requested by the online submission. Once submitted, corrections to the
entry, including any corrections or updates to the Proposal, will not be accepted.
             
All team members must have a valid AIAA Student Membership. Membership numbers of all team members must be
submitted with the team rosters. You may join at any time by going to the AIAA Student Membership website.
Membership numbers are provided instantly upon payment of membership fees.
             
Incomplete entries will not be accepted.
             
It is the team's responsibility to make sure the e-mail contact addresses they supply remain active during the entire
period from entry to the close of the competition as e-mail will be the primary means to provide information and
updates. Do not use an internal team correspondence e-mail list server as your point of contact e-mail address.
             
An entry is not complete until the “Save and Finalize” function is selected in the online submission system and
confirmed.
''')
with st.expander('Proposal'):
    st.write('''
Proposals will be submitted using the online system.
             
The proposals will be scored as defined in the proposal requirements section. The top 110 proposals plus ties will be
invited to submit design reports and potentially become eligible for the fly-off. Teams will be notified no later than 17
November if their proposal has been accepted.
             
Proposals submitted by email will not be accepted.
             
Proposals will be judged “as received”. No corrections/additions/changes will be allowed by the organizers so check
your proposals carefully before submitting them. Once a Proposal is submitted, no changes are allowed.
             
Submission of Proposals is electronic only (no hard copy required). The details for the electronic format and
submission are at the end of the proposal section in this rules document.
''')
with st.expander('Design Report'):
    st.write('''
Design Reports will be submitted using the online system.
             
The design report submission period OPENS 1 February at 8AM (0800) US Eastern Time. The design report must be
submitted by 5 pm (1700) US Eastern Time on 23 February 2024.

The reports will be scored as defined in the design report requirements section. Reports submitted by email will not
be accepted.
             
Reports will be judged “as received”. No corrections/additions/changes will be allowed by the organizers so check
your reports carefully before submitting them. Once a Report is submitted, no changes are allowed.
             
Submission of Reports is electronic only (no hard copy required). The details for the electronic format and
submission, including a requirement for an additional, separate configuration drawing, are in the report section in
this rules document
''')
with st.expander('Contest Fly-off'):
    st.write('''
The contest fly-off is scheduled for 18 - 21 April 2024 and is anticipated to run from 12PM (1200) to 6PM (1800) on
Thursday, 7AM (0700) to 6PM (1800) on Friday, 7AM (0700) to 6PM (1800) on Saturday and 7AM (0700) to 5PM
(1700) on Sunday (local time). Awards will be presented at 5:30PM (1730) on Sunday. All teams should plan their
travel so that they may stay for the awards presentations on Sunday. A final contest schedule will be e-mailed to the
teams prior to the contest date.
             
Tech inspections will begin on Thursday afternoon and will continue as required on Friday, Saturday and Sunday.
             
To help streamline the contest flow and maximize opportunities for each team to get their flights in, the Tech
inspections will be conducted in the same order as the flight rotation (which is based on report scores) so that the
first teams inspected will be the first teams in the flight queue. Teams may use the sequence to help estimate when
they need to arrive at the contest site to make sure they do not miss their slot in the first tech inspection rotation.
             
PLEASE NOTE: All schedule deadlines are strictly enforced
             
All deadlines are based on when an entry or submission is Received (Save and Finalize) by Contest officials via the
online submission system.
             
Late entries and proposals will NOT be accepted.
             
Late report submissions will NOT be accepted.
             
There is no allowance for computer, internet, or power outages by the submitter, or any other type of error beyond
the control of the DBF Organizing Committee.
             
Teams which do not submit the required electronic report and additional configuration drawing will NOT be allowed
to fly.
             
It is the team's responsibility to assure that all deadlines are known, understood, and met.
''')

st.subheader('Fly-off Site')
with st.expander('Fly-off Site'):
    st.write('''
Host for the competition will be Textron Aviation. The fly-off is planned to be held at the Textron Aviation Employees'
Flying Club in Wichita, KS. Details on the contest site and schedule will be sent to registered teams 2 - 3 weeks prior
to the flyoff. You can check on historical weather conditions at www.weatherbase.com or
www.weatherunderground.com.
             
Teams are advised to check with their airlines on what materials they will be allowed to bring both to and from the
contest site. Hazmat items like paints, thinners and glues may need to be purchased locally and PROPERLY disposed
of following the contest. **NOTE: It is the team's responsibility to ensure that their airplane arrives at the fly-off
location. Neither AIAA nor the corporate sponsors will assist in getting your airplane or materials to the fly-off
location. Teams may hand carry their airplane, use a shipping company to have it delivered to their hotel, or use any
other means of transportation that they feel is appropriate. But each team must coordinate all aspects of getting the
airplane to the fly-off.
''')

st.subheader('Mission and Vehicle Design')
with st.expander('General'):
    st.write('''
- The airplane wingspan cannot exceed 5 feet.
             
- The airplane in the parking configuration, while on its landing gear in the upright orientation, must fit inside a
parking spot 2 ½ feet wide.
             
- If wingspan exceeds parking spot width, then the airplane must be configured to fit without any components
removed from the airplane.
             
- Payloads:
    - Mission 1 -- Crew only.
    - Mission 2 -- Crew, EMTs, Patient, gurney, and Medical Supply Cabinet.
    - Mission 3 -- Crew and Passengers.
    - The Crew, EMTs, Patients, and Passengers will be provided at the competition. The Crew, EMTs and Passengers are shown in Figure 2 (3 ½ inch jumbo angel) and the Patient is shown in Figure 3 (5 ½ inch jumbo man). These are “wood peg dolls” and are available on Amazon and other sites for teams to obtain for trials and testing.
             
https://www.amazon.com/Unfinished-Angel-Dolls-Angle-Birch/dp/B01MQJZHVL/ref=sr_1_1_sspa?keywords=wooden%2Bpeg%2Bdolls&qid=1688655976&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1
''')
    col1, col2 = st.columns(2)
    with col1:
        image_crew = Image.open('assets/crew.png')
        st.image(image_crew, caption='Crew, EMTs, and Passengers', use_column_width=True)
    with col2:
        image_patient = Image.open('assets/patient.png')
        st.image(image_patient, caption='Patient', use_column_width=True)

    st.write('''
- The gurney must be at least the same width and length as the Patient as a minimum with a minimum
height of 1.50 inches.
             
- The Medical Supply Cabinet shall have a minimum width and length of 3.00 inches and a minimum
height of 3.50 inches. The maximum weight is up to each team to decide and the weight can be varied
for each mission attempt not to exceed the maximum weight declared in tech inspection.
             
- The airplane shall have a single plane, horizontal floor in the passenger compartment to carry the EMTs,
Patient on gurney, Medical Supply Cabinet and Passengers. A separate insert on top of the horizontal floor
may be used specific to each mission, if desired.
             
- The Crew, EMTs, Patient on gurney, and Passengers must have a restraint system to secure them from
moving during taxi, take-off, flight, and landing. The Patient must also be securely restrained to the gurney.
             
- The EMTs must be alongside of the Patient on the gurney as shown in Figure 4. The EMTs cannot touch each
other, the Patient, gurney or any part of the airplane other than the floor or insert. The Medical Supply
Cabinet can be forward or aft of the EMTs/Patient.
             
- The Passengers must be placed in the passenger compartment as shown in Figure 5. The Passengers cannot
touch each other or any part of the airplane other than the floor or insert.
             
- The Crew (Pilot and Co-Pilot) shall sit on a horizontal plane and be placed side-by-side without touching each
other or any part of the airplane other than the floor. The crew horizontal plane does not have to be co-
planar with the passenger compartment floor. There must be a solid bulkhead between the Crew and
Passenger compartment as shown in Figures 4 and 5.
''')
    image_missionlayout = Image.open('assets/mission_layout.png')
    st.image(image_missionlayout, use_column_width=True)
    st.write('''
- The Crew shall be in a cockpit such that their heads are above the fuselage forward of the cockpit as shown in
Figure 6. It is incumbent on each team to assure this requirement can be verified in Tech Inspection.
''')
    image_crewplacement = Image.open('assets/crew_placement.png')
    st.image(image_crewplacement, use_column_width=True)
    st.write('''
- The passenger compartment shall be accessed via a hinged hatch(es) on the side of the airplane. The hinge
for the hatch(es) cannot extend beyond the fuselage centerline. The opening opposite the hinge side cannot
extend beyond the fuselage centerline. The hatch(es) are limited to a width of 6.00 inches. There is no limit
to the number of hatches implemented.
             
- The Crew must be loaded via a separate hinged hatch(es) that is forward of the required bulkhead. This
could include a hinged side hatch(es) or a hinged canopy on top.
''')
with st.expander('Mission Sequence'):
    st.write('''
- The airplane must be capable of performing all required missions.
    - During Tech Inspection, the airplane must pass the wing tip load test in the flight condition with the
maximum designed takeoff weight, to include the heaviest weight payload declared and heaviest
battery to be flown.
    - The maximum load demonstrated will be recorded and cannot be increased after completing Tech
Inspection.
             
- The Flight Missions must be flown in order.
    - A new mission cannot be flown until the team has obtained a successful score for the preceding mission.
    - The ground mission can be attempted at any time.
             
- The airplane must be flown in the same configuration for all three missions excluding payloads and optional
passenger compartment insert(s), if used.
             
- After successfully completing all three flight missions, teams will be allowed one additional attempt for both
Mission 2 and Mission 3 to improve their score.
             
- After successfully completing the ground mission, teams will be allowed one additional attempt to improve
their score.
             
- The airplane will be brought to the staging box in the parking configuration with Crew, EMTs, Patient, gurney,
Medical Supply Cabinet, floor insert (if used) and propulsion battery pack(s) removed from the airplane.
             
- If you forget something you must leave the staging box and forfeit the flight attempt.
             
- Only the assembly crew member, pilot, and observer may go to and enter the staging box or Ground Mission
area.
             
- The assembly crew member is the only person who can touch the airplane while inside the staging box
while preparing the airplane for flight.
             
- Prior to starting assembly of the airplane, the propulsion battery pack will be inspected to verify it has been
approved in Tech Inspection and the capacity recorded and the Medical Supply Cabinet will be weighed,
verify it does not exceed the maximum allowable weight and recorded. The teams will be provided with the
Crew (all missions), EMTs and Patient (M2 only) and the number of Passengers requested not exceeding the
maximum number of Passengers declared in Tech Inspection (M3 only).
             
- All assembly work on the airplane in the staging box or during the ground mission must be done with the
airplane on its landing gear in the upright configuration. The airplane cannot be picked up, rotated or put in
any position other than upright and on its landing gear during assembly, payload installation or flight controls
checks. One exception is to check balance using the wing tips with the aid of the observer or pilot.
             
- The airplane assembly and payload installation must be completed in less than 5 minutes.
             
- There is no work allowed on the airplane after the 5-minute assembly and checkout time including
connection of batteries, receivers, etc. The airplane must be ready to fly prior to being called to the flight
line, less the installation of the arming fuse.
             
- The airplane will use ground rolling takeoff and landing.
             
- The airplane must take-off within 20 feet of the start/finish line. All ground contact points of the airplane
MUST be forward of the start/finish line.
             
- The initial upwind turn on the first lap of each mission will occur after passing the turn judge (signaled by
raising a flag).
             
- The airplane must always remain in unaided visual control distance of the pilot. The Flight Line Judge may
require turns to be made to remain in a safe visual control range at his discretion.
             
- The airplane must complete a successful landing at the end of each mission for the mission to receive a score.
    - A successful landing is outlined in the general mission specifications section below.
''')
with st.expander('Flight Missions'):
    st.subheader('Mission 1: Delivery Flight')
    st.write('''
- The payload for Mission 1 is Crew only.
             
- The airplane will enter the staging box in the parking configuration with the propulsion battery(ies) removed.
             
- The ground crew will put the airplane in the flight configuration and install the battery(ies) and Crew within
the 5 minute staging window.
             
- Teams must complete 3 laps within the flight window.
             
- There will be a 5-minute flight window for this mission.
             
- Time starts when the airplane throttle is advanced for the first take-off (or attempt).
             
- A lap is complete when the airplane passes over the start/finish line in the air (the landing is not part of the
5-minute time window).
             
- Must complete a successful landing to get a score.
''')
    st.subheader('Scoring:')
    st.write('M1 = 1.0 for successful mission')
    st.subheader('Mission 2: Medical Transport Flight')
    st.write('''
- The payload for Mission 2 is the Crew, EMTs, Patient on gurney, and Medical Supply Cabinet.
             
- The airplane will enter the staging box in the parking configuration with the propulsion battery(ies) removed.
The staging box judge will weigh the Medical Supplies Cabinet and record the weight on the score sheet.
             
- The ground crew will put the airplane in the flight configuration and install the battery(ies), Crew, floor insert
(if used), EMTs, Patient on gurney, and Medical Supply Cabinet within the 5-minute staging window.
             
- There will be a 5-minute window for this mission.
             
- Teams will be timed for 3 laps.
             
- The score will be a function of the Medical Supply Cabinet weight / time to fly 3 laps.
             
- Time starts when the airplane throttle is advanced for the first take-off (or attempt).
             
- A lap is complete when the airplane passes over the start/finish line in the air (the landing is not part of the
5-minute time window).
             
- Must complete a successful landing to get a score.
''')
    st.subheader('Scoring:')
    st.write('''
M2 = 1 + [N_(payload weight / time) / Max_(payload weight / time] , where Max_(payload weight / time) is the
highest payload weight / time score of all teams.
''')
    st.subheader('Mission 3: Urban Taxi Flight')
    st.write('''
- The payload for Mission 3 is Crew and Passengers.
             
- The airplane will enter the staging box in the parking configuration with the propulsion battery(ies) removed.
The staging box judge will record the battery capacity and number of passengers flown on the score sheet.
             
- The ground crew will put the airplane in the flight configuration and install the battery(ies), Crew, floor insert
(if used) and Passengers within the 5-minute staging window.
             
- There will be a 5-minute window for this mission.
             
- The number of laps flown within the 5-minute window will be recorded.
             
- The score will be a function of the number of laps flown * number of passengers / rated battery capacity
(Wh).
             
- Time starts when the airplane throttle is advanced for the first take-off (or attempt).
             
- A lap is complete when the airplane passes over the start/finish line in the air (the landing is not part of the
5-minute time window).
             
- Must complete a successful landing to get a score.
''')
    st.subheader('Scoring:')
    st.write('''
M3 = 2 + [N_(# laps * # passengers / battery capacity) / Max_(# laps * # passengers / battery capacity)] , where
Max_ (# laps * # passengers / battery capacity) is the highest (# laps * # passengers / battery capacity) of all teams.
''')
    st.subheader('Ground Mission: Configuration Demonstration')
    st.write('''
- The Ground Mission is a timed mission to demonstrate efficiently changing mission configurations.
             
- The teams will enter the ground mission with the airplane in the parking configuration and no payloads or
components installed. The propulsion battery is not part of the ground mission but flight controls will be
verified at the completion of the mission.
             
- The assembly crew member and a pilot may participate in the Ground Mission; only the assembly crew
member can touch the airplane and payloads.
             
- The mission will start with the airplane in the ground mission parking spot and Crew, EMTs, Patient, gurney,
floor insert (if used) and Medical Supply Cabinet in the triage area next to the parking spot.
             
- Time will start when the ground mission judge says “GO”.
             
- The assembly crew member will remove the airplane from the parking spot, put the airplane in the flight
configuration, load and secure for flight the Crew, EMTs, Patient on gurney, and Medical Supply Cabinet, and secure all hatches and doors then say “STOP” at which time the ground mission judge will stop the clock and verify doors and hatches are closed and secured.
             
- The pilot will verify all flight controls are working properly.
             
- The Passengers will then be staged in terminal area near the ground mission parking spot.
             
- Time will re-start when the ground mission judge says “GO”.
             
- The assembly crew member will then remove the EMTs, Patient on gurney and Medical Supply Cabinet from
the airplane (Crew may remain in place), change the floor insert (if used), load and secure for flight the
Passengers, secure all hatches and doors then say “STOP”, at which time the ground mission judge will stop
the clock and verify doors and hatches are closed and secured.
             
- The pilot will verify all flight controls are working properly.
             
- Time will re-start when the ground mission judge says “GO”.
             
- The assembly crew member will then remove the Crew and Passengers, put the airplane into the parking
configuration and place it in the parking spot and says “STOP”, at which time the ground mission judge will
stop the clock and record the total mission time.
''')
    st.subheader('Scoring:')
    st.write('''
GM = [Min_(mission time) / N_(mission time] , where Min_(mission time) is the lowest mission time for all teams.
''')
with st.expander('Airplane Requirements'):
    st.subheader('General')
    st.write('''
- The airplane may be of any configuration except rotary wing or lighter-than-air.
             
- No structure/components may be dropped from the airplane during flight.
             
- No form of externally assisted take-off is allowed. All energy for take-off must come from the on-board
propulsion battery pack(s).
             
- Must be propeller driven and electric powered with an unmodified over-the-counter model electric motor.
May use multiple motors and/or propellers. May be direct drive or with gear or belt reduction.
             
- Motors must be any commercial brushed or brushless electric motor.
             
- For safety, each airplane will use a commercially produced propeller/blades. The propeller can have folding
blades. Teams may modify the propeller diameter by clipping the tip and may paint the blades to balance
the propeller. No other modifications to the propeller are allowed. Commercial ducted fan units are
allowed.
             
- You can change the propeller (diameter/pitch) for each flight attempt.
             
- The airplane and pilot must be Academy of Model Aeronautics (AMA) legal. This means that the airplane
TOGW (take-off gross weight with payload) must be less than 55-lb, and the pilot must be a member of the
AMA. All pilots must sign in and verify AMA membership.
             
- Since this is an AMA sanctioned event, the team must submit proof that the exact airplane being presented
at Tech Inspection has been flown prior to the contest date to the technical inspection team. Proof of flight is a video showing controlled straight and level flight and will be presented to the inspector when called to
Tech Inspection. There are NO exceptions to this requirement.
             
- The airplane must remain substantially the same as documented in the report (for example you cannot
change a flying wing design to a conventional tail design). You may make small modifications to the design to
improve flight performance after the report submission (one example would be changing a control surface
size). The configuration drawing supplied in PDF form as described below in the Design Report section will be
used to verify the airplane configuration during tech inspection.
             
- The airplane must have an externally accessible SWITCH to turn on the radio control system. It cannot be
internal or under a panel or hatch. An arming plug is NOT considered an acceptable switch. The radio
control system switch must be separate from the propulsion system fuse & arming system.
''')
    st.subheader('Batteries')
    st.write('''
- There can be a maximum of one battery pack connected to a propulsion system. A propulsion system
consists of one battery, one externally accessible arming fuse, one or more electronic speed controllers (ESC),
and one or more motors.
             
- If the ESC has a Battery Eliminator Circuit (BEC), it must be disabled.
             
- If more than one battery pack is implemented for a single purpose such as propulsion, the following rules
apply:
    - All commercial battery packs must be identical (same manufacturer, part number, size, voltage, power,
rating, etc).
    - Each battery pack must be independently connected to its own propulsion system. Batteries cannot be
connected in series or parallel.
    - Each battery/propulsion system is required to have its own Arming Fuse.
             
- Teams may choose between NiCad/NiMH OR Lithium based batteries with the following provisions:
    - Teams may only use one battery type for propulsion.
    - Once a team completes tech inspection with a specific battery type, the team must use that battery
type for the remainder of the competition.
    - A separate battery is required for the Rx/Servo battery on the airplane. There is no restriction on the
Rx/Servo and Transmitter battery type regardless of the propulsion battery type.
    - Individual battery packs cannot exceed the FAA limits for hand carry on commercial air flights of 100
Watt-hours (rated capacity x rated voltage) per battery pack and as further defined in:
             
    - https://www.faa.gov/hazmat/packsafe/resources/media/Airline_passengers_and_batteries.pdf
             
    - Propulsion power total stored energy cannot exceed 100 Watt-hours.
    - Battery packs must be properly labeled indicating cell chemistry.
    - All battery disconnects must be "fully insulated" style connectors.
    - All battery packs must be un-altered and commercially procured as Commercial-Off-The-Shelf (COTS)
battery packs. Custom battery packs will not be allowed.
    - The Manufacturer's Label stating the Battery Capacity (mAh), Voltage (V), and C-Rating must be clearly
visible.
    - The maximum current rating for the Arming Fuse is 100 amps.
        - If using lithium-based batteries, the maximum current rating for the fuse is the maximum
continuous discharge current rating of the lithium battery pack (battery capacity X C-rating) up to
100 amps.
    - Lithium batteries must be stored and charged in a commercially available, unaltered Lithium battery
charging sack - the only time they can be out of the sack is for tech inspection or while in the airplane.
             
    - NOTE: It is the responsibility of each team to ensure compliance with all laws and regulations for shipping
or hand-carrying batteries.
             
- Batteries may not be changed or charged during any mission attempt.
             
- There is no limit to total battery weight (only capacity).
''')
with st.expander('Technical Inspection'):
    st.write('''
All vehicles will undergo a technical inspection by a designated contest tech inspector prior to being allowed to make
any competition flight or ground mission. All decisions of the Tech inspector are final.
             
To speed up the tech inspection process, each team MUST present a paper copy of a signed Pre-Tech and First-
Flight Certification when called to begin their on-site tech inspection. Teams may not begin the on-site tech
inspection without a completed certification. The Pre-Tech and First-Flight Certification sheet will be provided to
each team prior to the fly-off and made available on the contest website.
             
The Pre-Tech must be conducted by, and signed off by, a non-team member RC pilot or the team faculty advisor. The
Pre-Tech will cover the same safety of flight requirements as the on-site tech inspection and will assist teams in
making sure they are ready and able to pass the on-site tech inspection the first time. An expanded First-Flight
requirement, which also must be signed off by a non-team member RC pilot or the team faculty advisor, requires
demonstration of a complete flight including take-off, flying a minimum flight pattern, and landing in a pre-designated
location without damage to the airplane. The non-team member RC pilot who signs the inspection and flight
certifications may be the same as a team's non-student contest pilot.
             
Each team will also present their proof of flight video showing controlled straight and level flight to the inspector
when called to Tech Inspection.
''')
    st.subheader('Airplane Staging:')
    st.write('''
- The Airplane will enter Tech Inspection in the parking configuration with no payload items or propulsion
batteries installed.
             
- The Mission 2 Medical Supplies Cabinet will be at the maximum possible weight the team intends to fly
(Note: teams will not be allowed to fly with a weight greater than this after completing tech inspection but
can fly with less weight if they choose).
             
- Team members will declare the maximum number of Mission 3 Passengers
             
- All batteries and battery packs must be inspected during Tech Inspection. Teams should bring all possible
batteries for use over the full duration of the competition to Tech Inspection.
             
NOTE: Teams will be allowed to have additional batteries or battery packs inspected after passing Tech Inspection
due to damage, real time power change requirements, etc. However, teams must follow the Tech Inspection queue
or wait until Tech Inspection is open for all for additional battery inspections. Any team that uses batteries that have
not passed a Tech Inspection will lose that flight attempt and cannot attempt any further flights until the batteries
have passed inspection.
''')
    st.subheader('Safety inspections will include the following as a minimum:')
    st.write('''
Physical inspection of vehicle to ensure structural integrity:
1. Verify all components are adequately secured to the vehicle. Verify all permanent fasteners are tight and
have either safety wire, thread locker (LoctiteTM), or nuts/screws with a mechanical interference fit such as
nylon inserts or patches or self-locking threads. Clevises on flight controls must have an appropriate
mechanical locking device to prevent their disengaging in flight.
2. Verify all hatches and access panels have a positive, mechanical latching method to assure it does not come
loose in flight. Spring latches, fasteners, cotter pins, tape, etc are examples of acceptable methods. Magnets are not an acceptable latching method. Velcro may be an acceptable method depending on the implementation, but a secondary method may be required at the discretion of the technical inspector.
3. Verify propeller structural and attachment integrity.
4. Visual inspection of all electronic wiring to assure adequate wire gauges and connectors in use.
5. Radio range check with motor off and motor on.
6. Verify all controls move in the proper sense.
7. Check the general integrity of the payload system.
      
Structural verification:

The airplane will be lifted with one lift point at each wing tip to verify adequate wing strength (this is "roughly"
equivalent to a 2.5g load case) and to check for vehicle cg location. Teams must mark the expected empty and
loaded cg locations on the exterior of the airplane. Special provisions will be made at the time of the contest for
airplanes whose cg does not fall within the wing tip chord. This test will be made with the airplane filled to its
maximum payload and battery (combination) capacity.
Radio fail-safe check:
All airplane radios must have a fail-safe mode that is automatically selected during loss of transmit signal. The fail-
safe will be demonstrated on the ground by switching off the transmit radio. During fail-safe the airplane receiver
must command:
- Throttle closed
- Full up elevator
- Full right rudder
- Full right aileron
- Full Flaps down
             
For airplanes not equipped with a particular control, then the tech inspector must be satisfied that the intended
function of the fail-safe system will be carried out.
             
The radio Fail Safe provisions will be strictly enforced.
             
All airplane must have a mechanical motor arming fuse separate from the onboard radio Rx switch. This MUST be the
contest specified "blade" style fuse. This device must be located so it is accessible by a crewmember standing ahead
of the propeller(s) for pusher airplanes, and standing behind the propeller(s) for tractor airplanes (i.e. the crew
member must not reach across the propeller plane to access the fuse). The "Safety Arming Device" will be in "Safe"
mode for all payload changes. The airplane Rx should always be powered on and the throttle verified to be "closed"
before activating the motor arming switch. Fuses MUST be mounted on the outside of the airplane (they can not be
behind an access panel or door) and MUST act as the "safing" device. Note: The airplane must be “safed” (arming
fuse removed) any time the airplane is being manually moved, or while loading/unloading payloads during the
mission. The arming fuse must be removed anytime the airplane is in the hanger area.
             
The maximum current rating for the Arming Fuse is 100 amps.
- If using lithium-based batteries, the maximum current rating for the fuse is the maximum continuous
discharge current rating of the lithium battery pack (battery capacity X C-rating) up to 100 amps.
''')
with st.expander('General Mission Specifications and Notes'):
    st.write('''
- The airplane propulsion system(s) must be "safed" (fuse removed) during any time when crew members are
preparing/handling the airplane.
             
- Maximum mission support crew is: pilot, observer, and ground crew.
             
- Observer and ground crew must be students. Only the pilot may be a non-student.
             
- The upwind turn will be made after passing the upwind marker. The downwind turn will be made after
passing the downwind marker. Upwind and downwind markers will be 500 ft from the starting line. The
airplane must be "straight and level" when passing the turn marker before initiating a turn.
             
- "Successful" Landing - The airplane must land on the paved portion of the runway. The airplane may "run-
off" the runway during roll-out. The airplane may not “bounce” off the runway
             
- Airplanes obtaining “significant” damage during landing will not receive a score for that flight. Determination
of “significant” is solely at the discretion of the Flight Line Judge.
             
- Flight altitude must be sufficient for safe terrain clearance and low enough to maintain good visual contact
with the airplane. Decisions on safe flight altitude will be at the discretion of the Flight Line Judge and all
rulings will be final.
             
- All instructions from the Flight Line Judge must be followed IMMEDIATELY. Failure to do so may result in a
loss of mission attempt or in the case of multiple or serious infractions, loss of future flight attempts.
             
- Additional information is included in the FAQ (Frequently Asked Questions).
''')

st.subheader('Reports')
with st.expander('Reports'):
    st.write('''
All material contained within all proposals and design reports must be original work of the teams or appropriately
cited in the bibliography section of the report or in the footnotes of the proposal. All proposals and reports will be
reviewed using standard AIAA tools. Any material that is found to be uncited and non-original work will be subject to
a penalty as determined by the DBF Organizing Committee. Based on the severity, penalties can include points
deducted from the proposal or report score up to a 100-percent reduction or full disqualification for the competition year.
''')
with st.expander('Proposal'):
    st.write('''
Each team will submit a proposal as outlined below that will be judged.
             
Examples of top scoring proposals from prior contest years are posted on the contest website. Note that the
formatting and content may have changed from one year to the next. Prior year proposals may not reflect or meet
the rules listed for the current year.
             
Note: Proposals must strictly adhere to the following requirements. Failure to meet requirements will
result in penalties that range from score reduction to elimination from the contest.
''')
    st.subheader('Formatting Requirements:')
    st.write('''
- Proposals must be in PDF format. Proposals that are not in PDF format will not be accepted.
             
- Proposals must be one and one-half line spacing with a 10-pt Arial font recommended. Text, tables, and
figures should be clear and readable for the judges. The proposals will be assessed for format and readability
at the judges' discretion.
             
- Proposals must have the University name on the first page.
             
- Absolute maximum page count for the proposal is 5 pages, the PDF reader "pages" value will be used as the
official page count.
             
- Proposals exceeding the maximum page count will not be accepted.
             
- Proposal PDF must be formatted as 8.5” x 11" pages.
''')
    st.subheader('Submission Requirements:')
    st.write('''
Each team must provide an electronic copy of their proposal as outlined below to the online Submission site.
             
- Electronic proposal must be named: “2024DBF_[university name]_PROPOSAL.pdf" .
             
- University name should not be an acronym.
             
- Universities with multiple campuses should specify which campus in the university name.
             
- Electronic proposal must be a single file with all figures/drawings included in the proper sequence in PDF
format.
             
- Electronic proposals should have all figures compressed to print resolution to minimize file size.
             
- Electronic proposals must be less than 20 MB in size.
Proposals exceeding the file size will incur a 10-point penalty.
''')
    image_proposalpenalties = Image.open('assets/proposal_penalties.png')
    st.image(image_proposalpenalties, caption='Summary of Proposal Penalties', use_column_width=True)
    st.subheader('Scoring:')
    st.write('''
Proposals will be scored on a 100-point basis following the guidelines outlined below.
             
All information used for scoring must be in the outlined sections. Content that is out of sequence will be treated as
missing and scored accordingly.
             
ALL items requested below should be present, easy to locate and identify, well documented and in the correct
section for full scoring. Note that all proposals are assessed relative to each other so that simply addressing each of
the sections below may not be sufficient for full credit. Proposals will be assessed on how well they communicate
the required information given the size and length constraints.
''')
    st.subheader('Proposal Scoring Rubric:')
    st.write('''
All section scores include format, completeness and readability.
             
Executive Summary (5 points):
- Objective Statement.
- Planned approach to achieve all objectives.
- Includes main points from subsequent sections.
             
Management Summary (40 points):
- Describe the organization, the roles of each team and individual skill sets required.
- Organization chart (by team/function, individual names are not required for the proposal).
- Schedule / Major Milestone chart.
- Budget (not only for expected materials and manufacturing of the airplane, but for travel to the competition
site and any other expenses associated with the competition).
             
Conceptual Design Approach (35 points):
- Decomposition of mission requirements into sub-system requirements.
- Preliminary design / sizing results; concept sketch, if available (does not have to be representative of the final
design).
- Sensitivity Study of Design Parameters.
             
Manufacturing Plan (10 points):
- Preliminary manufacturing flow.
- Describe critical processes or technologies required.
             
Test Planning (10 points):
- Component and ground test plan.
- Flight test plan.
''')
with st.expander('Design Report'):
    st.write('''
Each team will submit a design report as outlined below that will be judged.
             
Examples of winning team design reports from prior contest years are posted on the contest website. Note that the
formatting and content has changed from one year to the next. Prior year reports may not reflect or meet the rules
listed for the current year.

Note: Reports must strictly adhere to the following requirements. Failure to meet requirements will
result in penalties that range from score reduction to elimination from the contest.
''')
    st.subheader('Formatting Requirements:')
    st.write('''
- Reports must be in PDF format.
             
Reports that are not in PDF format will not be accepted.
             
- Reports must be one and one-half line spacing with a 10-pt Arial font recommended. Text, tables and figures
should be clear and readable for the judges. The reports will be assessed for format and readability at the
judges' discretion.
             
- Reports must have the University name on the cover page.
             
- Absolute maximum page count for the report is 60 pages, the PDF reader "pages" value will be used as the
official page count.
             
Reports exceeding the maximum page count will incur a 10-point penalty for each additional page.
             
- Report PDF must be formatted as 8.5” x 11" pages.
             
- May use 11” x 17" pages for the drawing package.
             
- An additional stand-alone configuration drawing must be submitted along with the report file. See
description below in the Submission Requirements section.
''')
    st.subheader('Submission Requirements:')
    st.write('''
Each team must provide an electronic copy of their design report as outlined below to the online Submission site.
             
- Electronic report files must be named: “2024DBF_[university name]_DESIGN_REPORT.pdf”.
             
- Electronic report must be a single file with all figures/drawings included in the proper report sequence in PDF
format.
             
- Electronic reports should have all figures compressed to print resolution to minimize file size.
             
- Electronic reports must be less than 20 MB in size.
             
Reports exceeding the file size will incur a 10-point penalty.
''')
    st.subheader('Stand Alone Configuration Drawing Requirements:')
    st.write('''
- In addition to the drawings included within the design report, an additional, separate file with a one page
configuration drawing formatted to fit 8.5" x 11" paper must be submitted with the report for confirmation
of the basic configuration. Note that this page DOES NOT count toward the report total page count)
             
- The configuration drawing shall include the following configuration items as a minimum:
             
- Wing configuration
             
- Propulsion/propellor location(s)
             
- Tail configuration
             
- Landing gear configuration (tricycle vs tail-dragger for example)
             
- The configuration drawing must be in the format shown in Figure 7 and must include a top, side, front and
isometric view.
             
- The configuration drawing file must be named: “2024DBF_[university name]_CONFIG.pdf”.
             
- University name should not be an acronym.
             
- Universities with multiple campuses should specify the campus in the university name.
             
- The university name shall be clearly shown on the drawing.
             
- The configuration drawing file is limited to 5 MB in size.
             
Configuration drawings that do not contain the configuration items above or are in the format shown in Figure
7 or meet the file size requirement will incur a 10 point penalty against the design report score.
''')
    image_configdrawing = Image.open('assets/config_drawing.png')
    st.image(image_configdrawing, caption='Configuration Drawing Format and Content', use_column_width=True)
    image_designpenalties = Image.open('assets/design_penalties.png')
    st.image(image_designpenalties, caption='Summary of Design Penalties', use_column_width=True)
    st.subheader('Scoring:')
    st.write('''
Reports will be scored on a 100 point basis following the guidelines outlined below.
             
All information used for scoring must be in the outlined sections. Content that is out of sequence, including the
drawing package, will be treated as missing and scored accordingly.
             
ALL items requested below should be present, easy to locate and identify, well documented and in the correct
section for full scoring. Note that all reports are assessed relative to each other so that simply addressing each of the
sections below may not be sufficient for full credit. Reports will be assessed on how well they communicate the
required information given the size and length constraints.
''')
    st.subheader('Design Report Scoring Rubric:')
    st.write('''
All section scores include format, completeness and readability.
             
Executive Summary (5 Points):
- Maximum of 1 page. If exceeded, score as 0 points.
- Summary description of selected design and why it best meets the mission requirements.
- Main points from subsequent sections.
- Document the performance/capabilities of your system solution.
             
Management Summary (5 Points):
- Describe the organization of the design team.
- Chart of design personnel and assignments areas.
- Milestone chart showing planned and actual timing of major elements.
             
Conceptual Design (15 Points):
- Describes mission requirements (problem statement).
- Translate mission requirements into sub system design requirements.
- Present a scoring sensitivity analysis.
- Review solution concepts/configurations considered.
- Describe concept weighting and selection process and results.
             
Preliminary Design (20 Points):
- Describe design/analysis methodology.
- Document design/sizing trades.
- Describe/document methodology for prediction of airplane performance
(include capabilities and uncertainties).
- Provide estimates of the airplane lift, drag and stability characteristics and method of prediction.
- Provide estimates of the airplane mission performance.
             
Detail Design (15 Points + 15 Points for Drawing Package):
- Document dimensional parameters of final design.
- Document structural characteristics/capabilities of final design.
- Document systems and sub-systems selection/integration/architecture.
- Document Weight and Balance for final design.
- Must include Weight & Balance table empty and with each possible payload/configuration.
- Document flight performance parameters for final design.
- Document mission performance for final design.
- Drawing package:
    - Configuration drawing with dimensions of all configurations.
    - Structural arrangement drawing.
    - Systems layout/location drawing.
    - Payload(s) accommodation drawing(s).
             
Manufacturing Plan (5 Points):
- Document the process selected for major component manufacture.
- Manufacturing processes investigated and selection process and results.
- Manufacturing milestones chart: plan and actual.
             
Testing Plan (5 points):
- Describe all major ground and flight tests performed.
- Objectives and schedule for each.
- Data to be collected and how applied.
- Test and flight check lists.
             
Performance Results (10 Points):
- Describe the demonstrated performance of key subsystems following execution of testing plan.
- Compare test results to predictions and explain any differences and improvements made.
- Describe the demonstrated performance of your complete airplane solution.
- Compare test results to predictions and explain any differences and improvements made.
             
Bibliography (5 Points):
- Must include list of all published works referenced in the text must be present in this section.
- Any material taken from a published source in all previous sections must have a numerical subscript
corresponding to the appropriate citation in this section.
- References should appear in numerical order.
- Format should match AIAA provided guidelines:
             
https://www.aiaa.org/publications/journals/reference-style-and-format
''')

st.subheader('Scoring')
with st.expander('Scoring'):
    st.write('''
In the event that, due to time or facility limitations, it is not possible to allow all teams to have the maximum number
of flight attempts, the contest committee reserves the right to ration and/or schedule flights. The exact
determination of how to ration flights will be made on the contest day based on the number of entries, weather, and
field conditions. In the event of a tie, Report Score will take precedence over Flight Score as a tie-breaker.
''')
with st.expander('Judging'):
    st.write('''
Students must design, document, fabricate, and demonstrate the airplane they determine to be capable of achieving
the highest score on the specified mission profile(s). Mission scores will be based on the demonstrated mission
performance obtained during the contest.
             
Each team must also submit a written Design Report. A maximum of 100 points will be awarded for the team design
report. The overall team score is a combination of the Design Report score and Total Mission Score. The team with
the highest overall team score will be declared the winner. Scores will be FINAL 7 working days after the completion
of the contest. This period will allow for review of the scores in a timely fashion following the contest.
             
All submitted reports are the property of AIAA, Textron Aviation and Raytheon and may be published or reproduced
at their discretion.
''')
with st.expander('Units of Measure'):
    st.write('''
The units of measure for scoring will be based on the US English system. All times or physical measurements will be
rounded to the number of decimal places shown in Table 1. Conventional rounding will be implemented (<0.5 -->
round down, >= 0.5 --> round up).
''')
    image_unitsofmeasure = Image.open('assets/units_of_measure.png')
    st.image(image_unitsofmeasure, caption='Units of Measure', use_column_width=True)

with st.expander('Total Score'):
    st.write('''
Each team's overall score will be computed from their Design Report Score, Total Mission Score, and Participation
Score using the following formula:
             
Competition Score = Design Report Score * Total Mission Score + P
''')
    image_participationscore = Image.open('assets/participation_score.png')
    st.image(image_participationscore, caption='Participation Score', use_column_width=True)
    st.write('''
Ties in competition score will be ranked by highest Design Report Score. The Total Mission Score will be computed
from the individual Flight Mission and Ground Mission Scores using the following formula:
             
Total Mission Score = M1 + M2 + M3 + GM
''')

