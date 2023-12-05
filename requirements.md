## Functional Requirements
1. Create Note: User is able to create a note
2. Edit Note: User is able to edit a note that has been created
3. Create Pages: User is able to create pages to organize notes
4. Create Template: User can create a template that acts as a boilerplate when creating notes
5. Delete Note: When user chooses to delete a note, it will be stored in a trash folder and there they can permanently delete afterwards
6. Share Note: User is able to share their notes to other users
7. Recover Note: User is able to recover deleted notes
8. Search Note: User is able to search a note by its text contents
9. Create User Profile: User can create a profile from which they can log into 
10. Edit User Profiles: User can edit their profile
11. User Login: Allows user to login to their notes dashboard
12. Spell Check: User is given suggestions when they have improper grammar/spelling

## Non-functional Requirements
1. Application will run on Chrome Chrome
2. The application is responsive and changes size depending on window size

## Use Cases
1. Create Note - Fardin Haque\
![](images/Create_Note_UI.png)\
- **Pre-condition:** The user is on the main page
- **Trigger:** User clicks on the create note button
- **Primary Sequence:**
    1. The system prompts the user to enter which template they would like to choose (initally set to "blank" template), select a page to nest this note, name the note, and give it an optional description. (System assigns timestamp with this note visible as a text field to user)
    2. The user clicks the template and page options from a drop-down menu. 
    3. The system shows the user the list of saved templates and pages.
    4. User selects a template and page and enters name and description.
    5. The user clicks "Create Note"
    6. The system checks if the note name is unique
    7. The systems saves the note information 
    8. System displays note in navigation bar and opens the edit note page (See Use Case #2)
- **Primary Postconditions:** The user can access their created notes in expandable lists within the navigation folder
- **Alternate Sequence:** User tries to create a note with a name that is already taken by another note
    1. System displays error that this name is already taken
    2. User changes name to something that is unique
    3. System removes error that name is taken
- **Alternate Sequence #2:** User tries to click "Create Note" without filling out the name field
    1. System displays error that a name has to input
    2. User inputs a name that has not been taken yet
    3. System removes invalid name error

2. Edit Note - Fardin Haque\
![](images/Edit_Note_UI.png)\
- **Pre-condition:** The note they want to edit exists and is in the navigation bar
- **Trigger:** User clicks on a note in the navigation bar or creates a note
- **Primary Sequence:** 
    1. The system displays the note in a text area, presents style options like highlight, italics, bold, etc., and shows additionally buttons like insert images (See Use Case #12)
    2. User adds or deletes text from the note
    3. User selects text and clicks style option (highlight, italics, bold, etc.)
    4. System displays changes 
    5. User clicks "Save Changes"
    6. System saves the changes made to the note
    7. User clicks "Go Home"
    8. System opens the home page
- **Primary Postconditions:** The system saves the note with its changes
    - The user will be able to see their new changes upon revisiting the note
    - The system does not save the version before their changes
- **Alternate Sequence:** User makes changes to the note and clicks "Go Home" instead of "Save Changes"
    1. Systems displays warning message that changes have not been saved 
    2. User clicks "Cancel" and returns to note page
    3. User clicks "Save Changes" and then "Go Home"
    4. System saves updated note

3. Create Pages - Fardin Haque\
![](images/Create_Page_UI.png)\
- **Pre-condition:** User is on the main page
- **Trigger:** User clicks on the "Create Page" button
- **Primary Sequence:**
    1. System prompts user for this page's name and provides text area for an optional description. (System assigns timestamp for this page and is visible to user as a text field)
    2. User enters name and description then clicks "Create Page"
    3. The system saves the page information
    4. The system displays the page in the navigation bar and changes the screen to view the page details 
- **Primary Postconditions:** The user is able to view their page in the navigation bar and is available in the list of pages when creating a note.
- **Alternate Sequence:** User tries to create a page without giving it a name or uses a non-unique name
    1. The system will display an invalid name erorr
    2. The system will prompt the user to input a valid name to continue
    3. The user will change input the name or change the name to something unique
- **Alternate Sequence #2:** The user enters fields for page and clicks "Go Home"
    1. The system warns the user that their changes will not be saved
    2. The system allows the user to "Continue" or "Cancel"
    3. The user clicks "Cancel" and they return to the create page display

4. Create Template - Fardin Haque\
![](images/Create_Template_UI.png)\
- **Pre-condition:** The user is on the main page
- **Trigger:** The user clicks on the "Create Template" button
- **Primary Sequence:**
    1. The system prompts the user to enter this template's name and a generated time-stamp is visible as a text-field to the user
    2. The user inputs the name of the template
    3. The system scrolls down to a text-area that allows them to create boiler-plate for this template with all the same options as edit note (See Use Case #2)
    4. The user inputs text, styles, tables, images, etc. that they would like to populate this template with
    5. User clicks on "Save Template"
    6. System checks if name is valid and saves template
- **Primary Postconditions:** The template is available in the list of templates when creating a note now (See Use Case #1 for context)
- **Alternate Sequence:** The user assigns a non-unique or null name to the template
    1. The system displays an error that the template name is invalid
    2. The system prompts the user to change the name of the template
- **Alternate Sequence:** The user makes changes to template and clicks "Go Home"
    1. The system will warn the user that their template will not be saved
    2. The system presents "Cancel" and "Continue" options
    3. The user hits "Cancel" and returns to the create template page

5. Delete Note - Carlos Quiroz\
![](images/Trash_UI.png)
- **Pre-Condition:** Note that user wants to delete must have been created already
- **Trigger:** User clicks on delete button when viewing the note
- **Primary Sequence:**
    1. User selects "Options" in menu bar when viewing the note
    2. System will display a menu that includes a delete option
    3. User selects the delete option
    4. System will display a confirmation message with two options, "Cancel" or "Delete"
    5. User selects option to delete
    6. System moves the note to a trash folder
    7. System displays the home screen
- **Primary Postconditions:** The user selected note to be deleted is in the trash folder
    - Deleted note is removed from the navigation bar that stores all notes
- **Alternate Sequence:** User tries to delete note that exceeds the storage limit
    1. System will display an error message stating the trash folder is full
    2. System displays trash folder
    3. User can free space by cleaning trash folder

6. Share Note - Carlos Quiroz\
![](images/Share_UI.png)\
- **Pre-Condition:** User is logged in and sharing recipient has an account
- **Trigger:** User clicks on share button on notes menu bar
- **Primary Sequence:**
    1. System prompts user to enter email of recipient user in a text-field
    2. User enters emails of intended recipient
    3. System will check if it is a valid email and user
    4. User clicks send
    5. System adds a copy of the note to the recipients notes list
    6. System goes back to displaying edit notes screen
- **Primary Postconditions:** The shared note is available on intended recipients notes list
- **Alternate Sequence:** Email of recipient is not valid and/or not a valid user
    1. System will display an error message stating invalid recipient credentials
    2. System prompts user to re-enter email
    3. User can click send once re-entered email is verfied
- **Alternate Sequence #2:** User clicks on send button but note fails to send
    1. System prompts user to hit "Retry" button
    2. User clicks retry
    3. System will re-attempt to send note to recipient by re-initiating the sending process
    4. System displays success message

7. Recover Note - Carlos Quiroz
- **Pre-Condition:** User has deleted a note and the note is in the trash folder
- **Trigger:** User right clicks note and selects recover
- **Primary Sequence:** 
    1. System prompts the user if they are sure they want to recover the note
    2. User clicks on checkmark button to confirm recovery of note
    3. System moves note from trash folder back to where user had previously had stored the note
    4. System displays the note on the main screen
    5. User can edit note (See Use Case #2)
- **Primary Postconditions:** Selected note is recovered and available to user in their notes list
- **Alternate Sequence:** Previous location of note no longer exists
    1. System will move note to main notes section
    2. User can then select to move the location of the note as they wish

8. Search Notes - Carlos Quiroz\
![](images/Search_UI.png)\
- **Pre-condition:** User must be on main page
- **Trigger:** User clicks on search button
- **Primary Sequence:**
    1. System displays a search bar where user can type a text input of a phrase or keywords they seek
    2. User types a text input
    3. System find all notes that contain the user inputted substring
    4. System will display all note(s) that were found
    5. User selects a note from the list
    6. System displays note for editing
- **Primary Postconditions:** System displays notes that match user inputted string
- **Alternate Sequence:** System can not find a match for user inputted search request
    1. System displays an error message that states "No Results"
    2. System prompts user to try and search for a different term
    3. User inputs a different string

9. Create User Profile - Henry To\
![](images/Welcome+Login_UI.png)
- **Pre-condition:** User has the application open
- **Trigger:** User is on the create account page
- **Primary Sequence:**
    1. System prompts user to enter their username, password, and email
    2. User enters their information into the provided text-fields
    3. User clicks "Submit"
    4. Systems checks if username and email is available
    5. System creates a profile for the user
    6. System displays application home page for the new user
- **Primary Postconditions:** Systems saves user information for future login
- **Alternate Sequence:** The user inputs a username and email that is already taken by another user
    1. Systems displays error that username and/or email are taken
    2. System prompts user to enter a different username and/or email
    3. User changes their information so it is unique, or logs in to existing profile

10. Edit User Profiles - Henry To
- **Pre-condition:** User must have an existing profile and is logged into it
- **Trigger:** User clicks on edit profile on home page
- **Primary Sequence:**
    1. System displays profile information (username, password, and email) in text-fields
    2. User changes text-fields
    3. User clicks "Save Changes"
    4. System checks if username and/or email are available
    5. System updates the profile
- **Primary Postconditions:** User's profile reflects new changes
- **Alternate Sequence:** The username and password that the user is trying to change to has been taken
    1. The system displays an error that the inputted username and email are taken
    2. The system prompts the user to change them
    3. The user changes the non-unique fields to something that is available
   
11. User Login - Fardin\
![](images/Home_UI.png)\
- **Pre-condition:** User has an exisiting account
- **Trigger:** User is on login page and no one is currently signed in on the session
- **Primary Sequence:**
    1. System prompts user to enter their username and password. Additionally, provides a field to "remember me"
    2. User types in valid username and password then clicks "Submit"
    3. System looks for matching credentials
    4. System opens User's dashboard displaying notes
    5. User is free to operate on the home page
- **Primary Postconditions:** The system displays the user information and keeps user signed in until they logout
- **Alternate Sequence:** User inputs invalid credentials (invalid username and password or credentials that do not exist)
    1. System displays error message stating that they input an invalid username and/or password
    2. System prompts user to enter correct credentials or create an account
    3. Users inputs the create credentials or goes to create account page (see use case #10)

12. Spell Check - Fardin Haque
- **Pre-condition:** User is making changes within a note
- **Trigger:** System detects a mistake in their grammar/spelling
- **Primary Sequence:** 
    1. System underlines spelling/grammar suggestion in red
    2. User right clicks suggestion
    3. System will display the suggestion and have options for "Accept" or "Ignore"
    5. User selects "Accept"
    6. System closes menu and removes red underlined text, replacing it with the suggestion
- **Primary Postconditions:** The note is updated with the suggestion
- **Alternate Sequence:** User clicks "Ignore" when right clicking suggestion
    1. System will remove red underline from suggestion and keep users old entry