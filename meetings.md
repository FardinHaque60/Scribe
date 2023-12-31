## Meetings
### 2023-11-10 at 14:00
- Attendees: Fardin, Henry, Carlos
- Team Updates:
    - Fardin: Worked on putting in my 4.5 requirements into github, getting repo and google drive set-up for collaboration
    - Henry: Worked on the 4 requirements and pushed changes from requirement.md file
    - Carlos: Worked on 5.5 requirements and sketches for the base plate UI and other features
- Group Progress:
    - We have completed our requirements and now looking into implementing some features such as:
- This Week Goals:
    - Fardin: Create Template, Page, Notes
    - Henry: Edit, Create, Login for User profile
    - Carlos: Share, Delete, Search Notes

### 2023-11-17 at 14:00
- Attendees: Fardin, Carlos, Henry
- Team Updates:
    - Carlos: Made the top navbar and worked on making the vertical nav bar
    - Fardin: Made login and create account page, set-up db, and made writing to DB for creating an account work
    - Henry:
- Group Progress:
    - We have a login, create account, and some dashboard made. Looking into creating the details and features into dashboard now.
- This Week Goals:
    - Everyone: Scrub through entries for use cases and check if any reference from database is there
        - Look if your alt seqs look good or not
        - Comment from prof: "A bit more attention to detail is needed in these requirements. Be clear about what the user will see and do. Alt Seq should be things the user does wrong and the steps your app will take to help them fix it."
    - Carlos: Will merge table and insert images reqs into one, will have 13 reqs total + ethical implications write up
    - Fardin: Look into trigger being the same as #1 on use cases, look into creating a pop up for making things
    - Henry: Will work on login page and create account page and revise Milestone #1 details

### 2023-11-27 at 18:00
- Attendees: Fardin, Carlos
- Team Updates:
    - Carlos: Made delete, and recover note features, worked on login and create acc to have better functionality
    - Fardin: Worked on create note, template, and fixed/ contributed to search and viewing notes in navigation bar implementation
- Group Progress:
    - We have a working application that allows the user to login, create an account, create notes, create templates, delete, recover, and search
    - All features are smooth and we are looking to improve UI/ functionality of creating notes and viewing them
    - The other features are well set and may look to only make minor changes to them
- This Week Goals:
    - Everyone: 
        - look into updating readme
        - make creating notes look better etc.
        - Questions to ask in class:
        1. For the ethical implications write-up does the "impact of engineering solutions" regard our application specifically, i.e. do you want us to write about the impacts our notes app makes on the lists areas?
        2. For groups of smaller size do they have to implement less use cases?
        3. Can we just link a pr # if we have multiple commits that are just under there?
        - potentially look into displaying notes under a page as a drop down
        - collapsable list (i dont know how to implement)
        - as of right how: implement it as indentiations basically -> later look into drop down menu (collapsable list, etc.)
        - look into dropping insert images (replace this with login)

        - Milestone #2 submission reqs hit:
            - Create Profile
            - Login (not in req doc yet)
            - Delete
            - Recover
            - Create Note
            - Create Template
            - Search

            - other features to implement if we have to for this milestone: sharing & editing notes
    - Carlos: look into ethical implications write-up suggestions
        - Share note implementation ideas: 
            - we have all the users in the db, so when we say put in a users name in the field to share, we just add the current note
            to that users notes table. Notes with user_id, so for that note just create another note like Note(title="", body="", user_id=which_ever_user was typed)
        - Google drive API
    - Fardin: creating pages, editing notes
        - clean up this meeting write-up and fix creating notes, push this so carlos can create a pr for his share implementation

### 2023-11-28 at 10:45
- Attendees: Fardin, Carlos
- Team Updates:
    - Fardin: Made design plan for home page and how new side bar will look like, some search improvements
    - Carlos: Made some bootstrap changes to home page and made plan for implemenitng erorr messages and additional bootstraps
- Group Progress:
    - Working app with the above mentioned features, with improved search functionality. 
- This Week Goals:
    - Everyone: Get app to have all but API related requirements by end of next week
    - Carlos: Implement Google Drive API, error messages, and bootstrap polishes
    - Fardin: Implement creating pages, improve editing notes (+spell check), and side bar tweaks

### 2023-12-01 at 15:30
- Attendees: Fardin, Carlos
- Team Updates:
    - Fardin: Worked on editing note functionality, currently working on implementing Quill API and side bar bootstraps
    - Carlos: Worked on getting erorr messages to show up on screen, looking to add Google Drive API
- Group Progress:
    - We have implemented 8 functional requirements so far with full functionality in login, create account, search, trash, and recover. 
    - We are still looking to make future changes to edit note, create note, create template with enhanced abilities like adding markdown/styles to notes
    - We are on track to implement the remaining features: google drive API, spell check, creating pages and are looking to allocate the last few days to polishing (making things look nice and testing)
- This Week Goals:
    - Everyone: Testing!
    - Fardin: Must ~ Implement creating pages, spell check library, editing notes styles. Polishes ~ side bar bootstrap for collapsable menu
    - Carlos: Must ~ Implement error messages, export to google drive API. Polishes ~ bootstrap/ UI styles wherever it seems neccessary

### 2023-12-05 at 10:45
- Attendees: Fardin, Carlos
- Team Updates:
    - Fardin: Worked on creating and editing pages functionality alongside implementing Quill for editing boxes
    - Carlos: Worked on trashing, recovering, and Google Drive API progress
- Group Progress:
    - We have implemented all the functional requirements that we initially set out for except spell check and google drive API. 
    - We are still looking to make polished to some UI aspects of the side bar and find bugs related to sharing, editing, and recovering
    - We are planning on droppping google drive API with something else
- This Week Goals:
    - Everyone: Look for bugs, testing, and updating documentation
    - Fardin: Must ~ Implement viewing profile, templates, pages; editing pages, templates, and profile
    - Carlos: Must ~ Implement deleting, recovering temoplates, pages, and profile; UI polishes, flash messages