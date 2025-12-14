from pyscript import document, display

# List of subjects in order
subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']

# Tuple representing the number of units/credits for each subject
units_subject = (5, 5, 5, 3, 2, 1)   

# Function to calculate General Weighted Average 
def general_weighted_average(e):
    """
    Calculates the General Weighted Average (GWA) of a student based on
    their grades and the unit value of each subject.
    
    Note: All input fields (first name, last name, and grades) must be filled
    before clicking the calculate button.
    """

    # Clear previous outputs in the HTML
    document.getElementById("student_info").innerText = ""
    document.getElementById("summary").innerText = ""
    document.getElementById("output").innerText = ""

    # Retrieve student information from HTML inputs 
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    # Check if names are entered 
    if first_name == "" or last_name == "":
        display("Please enter both your first and last name.", target="output")
        return  # Stop the function if names are missing

    # Retrieve grades from HTML inputs 
    # IMPORTANT: All fields must be filled before calculation
    try:
        science = float(document.getElementById("science").value)
        math = float(document.getElementById("math").value)
        english = float(document.getElementById("english").value)
        filipino = float(document.getElementById("filipino").value)
        ict = float(document.getElementById("ict").value)
        pe = float(document.getElementById("pe").value)
    except ValueError:
        display("Please enter all grades before calculating.", target="output")
        return  # Stop the function if any grade field is empty or invalid

    # Store all grades in a list
    grades = [science, math, english, filipino, ict, pe]

    # Compute weighted sum of grades 
    weighted_sum = (
        science * units_subject[0] +
        math * units_subject[1] +
        english * units_subject[2] +
        filipino * units_subject[3] +
        ict * units_subject[4] +
        pe * units_subject[5]
    )

    # Total number of units
    total_units = sum(units_subject)

    # Calculate GWA: weighted sum divided by total units
    gwa = weighted_sum / total_units

    # Prepare a summary of the grades 
    summary = f"""
{subjects[0]}: {science:.0f}
{subjects[1]}: {math:.0f}
{subjects[2]}: {english:.0f}
{subjects[3]}: {filipino:.0f}
{subjects[4]}: {ict:.0f}
{subjects[5]}: {pe:.0f}
"""

    # Display results in HTML 
    display(f"Name: {first_name} {last_name}", target="student_info")  # Show student name
    display(summary, target="summary")  # Show all subject grades
    display(f"Your general weighted average is {gwa:.2f}", target="output")  # Show GWA
