## <remove all of the example text and notes in < > such as this one>

## Functional Requirements
<should be 1 sentence that describes requirement>
1. Create Note: User is able to create a note
2. Edit Note: User is able to edit a note that has been created
3. Create Pages: User is able to create pages to organize notes
4. Create Template: User can create a template that acts as a boilerplate when creating notes
5. requirement
6. requirement
7. requirement
8. requirement
9. requirement
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