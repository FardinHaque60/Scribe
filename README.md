# Scribe
- Fardin Haque (@FardinHaque60)
- Carlos M. Quiroz-Vasquez (@carlosq-mv)
- Henry To (@tohenry15)

# Video
* [Link to our video](https://drive.google.com/file/d/1NnRAYytQ9PW6bd_A4yi0ejbqQcA4UdSv/view?usp=sharing)

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
* `cd Scribe/` to enter the repository 
* `python3 -m venv venv` to create a virtual environment.  
* `source venv/bin/activate` to activate virtual environment.  
* `pip3 install -r requirements.txt` to install all the dependencies needed to run the app.
* `python3 run.py` to run the application
* cntrl/cmd + click the link `http://127.0.0.1:5000` that is displayed in the output to run the application in your broswer

## Features
* Create Profile ~ by Fardin 
* Edit Profile ~ by Fardin
* Login ~ by Fardin
* Create Note ~ by Fardin + Carlos
* Edit Note & Page ~ by Fardin
* Delete Note & Page ~ by Carlos
* Recover Note & Page ~ by Carlos
* Share Note ~ by Carlos
* Create Page ~ by Fardin
* Create Template ~ Fardin
* Edit Template ~ Fardin
* Delete Template ~ Carlos
* Recover Template ~ Carlos
* Search Note ~ Carlos
* Delete Profile ~ Carlos

## How To Create Account
* Upon start up, click on Sign Up. Type username in username field. Type password in password field.  
Proceed to retype the same password in repeat password field.   
Enter a valid email in email field. Click on register. Account is now registered.

## How to Edit your Profile
* Upon signing in navigate to the top right hand corner of the dashbaord. Here you can find a profile button where you can click to view your profile details. Change your username, email, or templates (*see edit templates for more info) and click "Save Changes". Additionally, click the "Change Password" button to enter our change password request client.

## How To Login
* Enter existing username in username field then Enter the password for that username. Click on sign in. User is now logged in.

## How To Create Note
(Note: you can select a template if one is created, see *using templates)

* Click on Create Note button. *Fill in title field then fill in note body field. Click Enter. Note is now created.
    - *using templates:
        * Click on drop down menu. Choose a template (if no templates are available, blank note is default).  
        Note body field is populated with the template body. Proceed as expected.

## How To Edit Note & Page
* Click on an existing note or page from the side bar. Here you will see your details like title and body/description. Edit the fields and click "Save Changes".

## How To Delete Note & Page
* Click on an existing note or page from the side bar. Click red trash button, available when viewing.  
That page or note is now populated in trash. Go to trash folder(labled 'Trash' in top nav bar).   
Click on delete button that is next to note/page. Note/page is now deleted.

## How To Recover Note & Page
* Click on the trash icon in the top navigation bar. Navigate to the page or note you would like to recover and click recover. The page or note will be put back into your side bar master list.

## How To Share a Note
(Note: recipient must be an existing user of Scribe)
* Click on note you want to share. When viewing the note, click on share button.  
Enter email of intended recipient. Click on share. Note is now shared for intended recipient.

## How To Create a Page
* Click "+ Create Page" on the side navigation bar. Enter details about the page like its name and description. Click Create Page and your
page will appear on the side navigation bar. You can click your page to view notes below it. To add notes to your page, when creating a note select a page from the drop down menu to add it to that page.

## How To Create a Template
* Click on Create template button. Enter the title for template in title field.   
Enter the text to be saved in the body field. Click Enter. Template is now created

## How To Edit a Template
* Click on your profile icon in the top right hand corner. Select a template from the dropdown menu of your templates. Make changes to your template title and body and hit "Save Changes"

## How To Delete a Template
* Click on your profile icon in the top right hand corner. Select the template you would like to delete from the dropdown menu of templates. Click on the "Trash" button when viewing the template

## How To Recover a Template
* Click on the trash icon in the top bar. Navigate to the template you want to recover and click the "Recover" button next to it.

## How To Search
* Go to search.(labled 'Search' in top nav bar). In search field type in a search query.   
Click on Enter. All notes that contain that search query will populate Search Results section. Click on one of notes to view its contents.

## How to Delete Profile
* Click on the profile icon in the top right hand corner. Click on the "Delete" button in your profile section. You will be redirected to the login screen.
