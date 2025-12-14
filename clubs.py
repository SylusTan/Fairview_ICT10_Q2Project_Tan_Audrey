# Importing necessary modules from PyScript
from js import document  
from pyscript import when 

# --- CLUB DATA DICTIONARY ---
# This dictionary stores information about different school clubs.
# Each key is the name of the club, and the value is another dictionary with detailed info.
clubs = {
    "Marching Band": {
        "description": "A performing ensemble focused on musical marching routines.",  # What the club does
        "meeting": "Tuesday and Wednesday, 3:00–4:30 PM",  # Days and times the club meets
        "location": "Band Room",  # Where the club meets
        "moderator": "Mr. Emilio Alumno",  # Club advisor
        "members": "N/A",  # Number of members 
        "category": "Arts & Music"  # Type of the club
    },

    "Glee Club": {
        "description": "A vocal music group for singers who enjoy choral and pop arrangements.",
        "meeting": "Monday, 3:00–5:00 PM",
        "location": "High School Music Room",
        "moderator": "Mr. Denver Martin",
        "members": "N/A",
        "category": "Arts & Music"
    },

    "Dance Club": {
        "description": "A club for students who enjoy practicing and performing dance routines.",
        "meeting": "Tuesday, 3:00–5:00 PM",
        "location": "Teatro Preciosa",
        "moderator": "Mr. Alfred Cases",
        "members": "N/A",
        "category": "Arts & Music"
    },

    "Math Club": {
        "description": "A club for students who enjoy problem-solving and competitions.",
        "meeting": "Monday, 2:30–3:00 PM",
        "location": "Room 404",
        "moderator": "Mr. Nicole Gabuya",
        "members": "N/A",
        "category": "Academic"
    },

    "Science Club": {
        "description": "A club focused on scientific exploration, experiments, and research.",
        "meeting": "Tuesday, 3:00–4:00 PM",
        "location": "Room 404",
        "moderator": "Ms. Jameelyn Maramag",
        "members": "N/A",
        "category": "Academic"
    },

    "Communications Arts Club": {
        "description": "A club dedicated to journalism, public speaking, and creative writing.",
        "meeting": "Wednesday 3:00–4:00 PM, Friday 3:00–4:00 PM",
        "location": "Room 406",
        "moderator": "Ms. Yannis Fernandez",
        "members": "N/A",
        "category": "Academic"
    },

    "COCC": {
        "description": "Cadet Officer Candidate Course focusing on leadership and discipline.",
        "meeting": "Wednesday, 2:30–4:30 PM",
        "location": "Quadrangle / Teatro Preciosa",
        "moderator": "SSgt. Jemima David PA (Res)",
        "members": "N/A",
        "category": "Leadership"
    },

    "Social Science Club": {
        "description": "A club for students interested in history, culture, and current events.",
        "meeting": "Tuesday, 3:00–4:00 PM",
        "location": "Room 409",
        "moderator": "Mr. Roberto Lim",
        "members": "N/A",
        "category": "Academic"
    },

    "Volleyball Varsity": {
        "description": "Varsity-level volleyball team for student athletes.",
        "meeting": "Wednesday, 3:00–4:00 PM",
        "location": "Quadrangle",
        "moderator": "Mr. Adrian Ruiz",
        "members": "N/A",
        "category": "Sports"
    },

    "Basketball Varsity": {
        "description": "Varsity-level basketball team for student athletes.",
        "meeting": "Monday, 3:00–4:00 PM",
        "location": "Quadrangle",
        "moderator": "Mr. Adrian Ruiz",
        "members": "N/A",
        "category": "Sports"
    }
}


# --- FUNCTION TO DISPLAY CLUB INFO ---
# This function is triggered when the button with id="showBtn" is clicked.
@when("click", "#showBtn")  # 'when' binds the click event of #showBtn to this function
def show_info(event):
    # Get the currently selected club from the dropdown with id="clubSelect"
    selected = document.getElementById("clubSelect").value

    # Get the HTML element where we want to display the club details
    details = document.getElementById("details")

    # If no club is selected, prompt the user to select one
    if selected == "":
        details.innerHTML = "Please select a club."
        return  # Stop the function here

    # Retrieve the dictionary of data for the selected club
    data = clubs[selected]

    # Create a formatted HTML string to display the club's information
    output = (
        f"<b>{selected}</b><br><br>"  # Club name in bold
        f"<b>Description:</b> {data['description']}<br>"
        f"<b>Meeting Time:</b> {data['meeting']}<br>"
        f"<b>Location:</b> {data['location']}<br>"
        f"<b>Advisor:</b> {data['moderator']}<br>"
        f"<b>Number of Members:</b> {data['members']}<br>"
        f"<b>Category:</b> {data['category']}"  # Type of club
    )

    # Update the inner HTML of the 'details' element to show the club information
    details.innerHTML = output
