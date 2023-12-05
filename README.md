# Scribe
- Fardin Haque (@FardinHaque60)
- Carlos M. Quiroz-Vasquez (@carlosq-mv)
- Henry To (@tohenry15)

# Table of Contents
* [General Info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [How To](#how-to-create-account)

# General Info
* Scribe is a note making web app built with Flask framework. 
You can create notes, and templates for those notes you always use.   
Plus with recovery features you don't have to worry about accidentally deleting an important note, since you can always recover them.  
Scribe also has the ability to share notes between users and includes a search feature.

# Setup
To run our application, run the following commands in a Linux terminal: 
* `git clone https://github.com/FardinHaque60/Scribe.git` to clone the repository in your current directory.
* `python3 -m venv venv` to create a virtual environment.  
* `source venv/bin/activate` to activate virtual environment.  
* `pip3 install -r requirements.txt` to install all the dependencies needed to run the app.
* `python3 run.py` to run the application
* cntrl/cmd + click the link `http://127.0.0.1:5000` that is displayed in the output to run the application in your broswer

## Features
* Create Profile ~ by Fardin 
* Login ~ by Fardin + Carlos
* Delete Notes ~ by Carlos
* Recover Notes ~ by Carlos
* Create Notes ~ by Fardin
* Create Templates ~ by Fardin
* Search Notes ~ by Fardin + Carlos
* Share Notes ~ by Carlos
* Create Pages ~ by Fardin 
* Export to Google Drive ~ by Carlos [Coming Soon!]
* Edit Notes ~ by Fardin 
* Edit Profile ~ by Fardin [Coming Soon!]

## How To Create Account
* Upon start up, click on Sign Up. Type username in username field. Type password in password field.  
Proceed to retype the same password in repeat password field.   
Enter a valid email in email field. Click on register. Account is now registered.

## How To Login
* Enter existing username in username field then Enter the password for that username. Click on sign in. User is now logged in.

## How To Create Note
(Note: you can select a template if one is created, see *using templates)

* Click on Create Note button. *Fill in title field then fill in note body field. Click Enter. Note is now created.

    - *using templates:
        * Click on drop down menu. Choose a template (if no templates are available, blank note is default).  
        Note body field is populated with the template body. Proceed as expected.

## How To Create Template
* Click on Create template button. Enter the title for template in title field.   
Enter the text to be saved in the body field. Click Enter. Template is now created

## How To Delete Note
* Click on an existing note. Click red trash button, available when viewing note.  
That note is now populated in trash. Go to trash folder(labled 'Trash' in top nav bar).   
Click on delete button that is next to note. Note is now deleted.

## How To Recover Note
* Click on an existing note. Click red trash button, available when viewing note. Go to trash folder (labled 'Trash' in top nav bar).  
Next, click on recover button that is next to note you want to recover.  
That note is back in users notes. Note is recovered.

## How To Search
* Go to search.(labled 'Search' in top nav bar). In search field type in a search query.   
Click on Enter. All notes that contain that search query will populate Search Results section. Click on one of notes to view its contents.

## How To Share
(Note: recipient must be an existing user of Scribe)
* Click on note you want to share. When viewing the note, click on share button.  
Enter email of intended recipient. Click on share. Note is now shared for intended recipient.

## How to Create a Page
* Click "+ Create Page" on the side navigation bar. Enter details about the page like its name and description. Click Create Page and your
page will appear on the side navigation bar. You can click your page to view notes below it. To add notes to your page, when creating a note select a page from the drop down menu to add it to that page.

## How to Export to Google Drive [Coming Soon!]

## How to Edit Notes 
* Click on the desired note in the side bar. Make changes to the note title or body and click save changes. The next time you view the note 
the changes will be displayed.

## How to Edit Profile [Coming Soon!]
