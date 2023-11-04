## Functional Requirements

1. Create Note: User is able to create a note
2. Edit Note: User is able to edit a note that has been created
3. Create Pages: User is able to create pages to organize notes
4. Create Template: User can create a template that acts as a boilerplate when creating notes
5. Delete Note: When user chooses to delete a note, it will be stored in a trash folder and there they can permanently delete afterwards
6. Share Note: User is able to share their notes to other users
7. Export & Import w/ Google Drive API: User can connect to their Google Drive to export and import to an from their Drive
8. Recover Note: User is able to recover deleted notes
9. Search Note: User is able to search a note by its text contents
10. requirement
11. requirement
12. requirement
13. requirement
14. requirement

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. Data must persist in the database and populate the page upon start-up
2. The application must be able to run on all OS’s such as Edge, Chrome, Firefox, etc.

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>
<example/template below>
1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
1. Ut enim ad minim veniam, quis nostrum e
2. Et sequi incidunt
3. Quis aute iure reprehenderit
4. ...
5. ...
6. ...
7. ...
8. ...
9. ...
10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to
describe multiple issues that may arise and their outcomes>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
<example/template end>

1. Create Note
- **Pre-condition:** The user is on the main page
- **Trigger:** User clicks on the create note button
- **Primary Sequence:**
1. The user clicks on the create note button
2. User is given an option to assign note to a page or generate it from a template
3. The user is requested to input a name and description for this note
4. The system checks if the name for this note is unique
5. Page opens up with a new note that they may edit and save changes to
6. The User can either go home without saving their changes or save this new note
7. The database is updated with this new note
- **Primary Postconditions:** The user can access their created notes in an expandable list in the navigation folder
- **Alternate Sequence:** User tries to create a note without giving it a name
1. User will be able to create note
2. When user hits save they will be prompted to give it a name before saving
3. User is unable to continue until they have given it a name
- **Alternate Sequence #2:** User tries to create a note with the same name as an existing note
1. User is prompted to change the name of this note since it already exists in another note
2. User will not be able to save the note until they change the name to something unique

2. Edit Note
- **Pre-condition:** The note they want to edit has already been made
- **Trigger:** User makes edits to a note and clicks save
- **Primary Sequence:** 
1. User clicks on a note to open it
2. User makes changes to the note
3. User clicks save to persist the changes
4. The database is updated with the new information on the note 
5. The database will overwrite the original data entry on this note
- **Primary Postconditions:** The note is saved onto the database reflected its updated changes
    - The user will be able to see their new changes upon revisiting the note
    - They no longer have access to the version before the changes
- **Alternate Sequence:** The user tries to save the note without making any changes
1. The program will allow them to save it without warning
2. The database will be re-written with its original entry 
- **Alternate Sequence #2:** User makes changes to the note, but does not press save and instead tries to go home/back.
1. User is prompted that their changes will not be saved if they go back/home
2. User may choose to confirm and go home or can cancel and save their changes before leaving

3. Create Pages
- **Pre-condition:** User is on the main page
- **Trigger:** User clicks on the create page button
- **Primary Sequence:**
1. User clicks on the create page button
2. User is prompted to enter details on the page such as the name and a description
3. The system checks to see if this name is unique
4. The user is able to save this page and add notes under this
5. The database allocates space for this page and gives it the ability to store notes underneath it
- **Primary Postconditions:** The user is able to view their page in the side navigation bar
- **Alternate Sequence:** User tries to create a page without giving it name
1. The system will prompt the user to enter a name
2. The user will not be able to save the page until a name is given to it 
- **Alternate Sequence #2:** The user tries to create a page with the same name as another
1. The user is warned that this page has the same name as another
2. The user is allowed to save this page with the same name as long as they confirm upon the alert

4. Create Template
- **Pre-condition:** The user is the main page
- **Trigger:** The user clicks on the create template page
- **Primary Sequence:**
1. The user clicks on the create template page
2. The user is asked to fill information related to the template such as the name and description
3. They are able to certain characteristics they want this template to have such as headers, preset organization, tables, and images
4. The system checks if the name is not taken yet
5. The system creates the template and adds it to the list of templates the user can choose from when making a note 
- **Primary Postconditions:** The template is available to make a note from now
- **Alternate Sequence:** The user tries to create a template with the same name as another
1. The system will prompt the user to change the name of the template
2. The user will not be able to make a template unless they change the name to something that is available

5. Delete Note
- **Pre-Condition:** User must have a note created
- **Trigger:** User clicks on delete button
- **Primary Sequence:**
1. User selects note options menu
2. System will display menu that includes a delete option
3. User selects delete option
4. System will display a confirmation message with two options to the user, cancel or delete
5. User selects option to delete
6. System stores the deleted note in a trash folder
7. System displays all deleted notes inside of trash folder
8. User has options to do a permanent deletion of note, recover the note or leave as is and system will permanently delete note in 30 days
- **Primary Postconditions:** The note user selected to be deleted is in trash folder
    - Deleted note is removed from users current notes
- **Alternate Sequence:** User tried to delete note but fails due to storage limit
1. System will display an error message
2. User can free space by cleaning trash folder
3. System allows user to delete note again
- **Alternate Sequence #2:** User selects to permanently delete note
1. User selects note to delete
2. System displays confirmation message
3. User selects to delete note
4. Note is permanently deleted from users account
5. System displays message that note is deleted permanently

6. Share Note
- **Pre-Condition:** User is logged in and recipient has an account
- **Trigger:** User clicks on share button
- **Primary Sequence:**
1. User selects note they want to share
2. User clicks on share button
3. System prompts user to enter email of recipient user
4. User enters emails of intended recipient
5. System will check if it is a valid email and valid user attached to email
6. User clicks send
7. Selected note are shared between owner(user) and recipient.
- **Primary Postconditions:** The shared note is available to all intended recipients
    - Recipient can view note
- **Alternate Sequence:** Email of recipient is not valid and or not a valid user
1. System will display an error message stating invalid recipient credentials
2. System prompts user to re enter email again
3. User can click send once re entered email is verfied
- **Alternate Sequence #2:** User clicks on send button but note fails to send
1. System prompts user to retry with a retry button
2. System will re attempt to send note to recipient by re initiating the sending process
3. System display success message once action is completed

7. Export & Import w/ Google Drive API
- **Pre-Condition:** User has connected Google Drive with their account
- **Trigger:** User clicks on export/import button
- **Primary Sequence:**
1. User clicks on export/import button 
2. System prompts user to select import or export 
3. User clicks on export
4. System prompts user to choose a file format(pdf, txt, docx, etc)
5. User chooses a format and clicks on export button
6. System connect to Google Drive api
7. User selects destination where note will go in their Google Drive
8. User clicks upload button to google drive
9. System displays message when export was successful
- **Primary Postconditions:** Selected note has been exported to Google Drive or Selected file in Google Drive has been imported into note
- **Alternate Sequence:** User clicks on import
1. System connects to Google Drive api with user credentials
2. User selects which file they want to import(restricted to supported files)
3. File is now imported to users notes
- **Alternate Sequence #2:** System fails to connect to Google Drive
1. System displays error message stating failed connection
2. User can reload page to establish a connection

8. Recover Note
- **Pre-Condition:** User has deleted a note
- **Trigger:** User clicks on recover button
- **Primary Sequence:** 
1. User is inside of the trash folder
2. User clicks on recover button
3. System prompts user to select the note they want to recover
4. User selects note
5. User clicks on checkmark button to confirm recovry of note
6. System prompts user to confirm their choice (cancel or recover buttons) w/ a message
7. User confirm by clicking on recover
8. System moves note from trash folder back to where user had previously had stored the note
- **Primary Postconditions:** Selected note is recovered and available to user
    - User has access to note with their current notes
- **Alternate Sequence:** Previous location of note no longer exists
1. System will move note to main Notes section
2. User can then select to move the location of the note as they wish
- **Alternate Sequence #2:** Trash Folder is empty and user clicks on recover button
1. System will display a message that folder is empty
2. User can leave trash folder and the folder will remain the same

9. Search Note
- **Pre-condition:** User must have an existing note
- **Trigger:** User clicks on search button
- **Primary Sequence:**
1. User clicks on search button
2. System display a search bar where user can type a text input of a phrase or keywords they seek
3. User types a text input
4. System will look through all notes seeking those that match users input
5. System will display all note(s) that contains users input
6. User can select the note that contain the text content they seek
- **Primary Postconditions:** User finds notes that contains the text contents they were seeking for
- **Alternate Sequence:** System can't find a match for user search input
1. System displays an error message
2. System prompts user to try and search for a different term
3. System will continue once it finds a match to the given search input