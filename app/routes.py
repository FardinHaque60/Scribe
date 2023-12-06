from flask import jsonify, render_template, redirect, flash, request, url_for
from flask_login import current_user, login_user, login_required, logout_user
from app import myapp_obj, db
from datetime import datetime
from .forms import ChangePassword, LoginForm, CreateAccount, SearchForm, CreateNote, NoteManagment, CreateTemplate, ShareNote, ViewNote, CreatePage, ViewProfile, ViewPage, TemplateMan
from .models import User, Note, Template, Page

'''for all routes add the flashed messages to html files'''
@myapp_obj.context_processor
def inject_current_time():
    return dict(current_time=datetime.now().strftime("%Y-%m-%d %H:%M"))

''' --------dashboard route below---------'''
# home route
@myapp_obj.route("/home")
@login_required # users that are not authenticated cannot access this link
def main_page():
    name, notes, page_notes, shared = home_helper()

    return render_template('home.html', name=name, notes=notes, page_notes=page_notes, shared=shared)

''' ---------------login page route below----------------'''
# login route
@myapp_obj.route("/", methods=['GET', 'POST'])
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    # checks if user is logged in
    if current_user.is_authenticated: 
        return redirect('/home')
    
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(username=form.username.data).first()    # queries database to find the user
        # checks password hash with attached to the user the user
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'loginError')
            return redirect("/login") 
        # Flask-Login function registers the user as logged in
        login_user(user, remember=form.remember_me.data)
        return redirect('/home')
    return render_template('login.html', form=form)

''' ------------------logout route below-------------------'''
# logout route
@myapp_obj.route("/logout")
def logout():
    # Flask-Login function registers the user as logged out
    logout_user()
    return redirect ("/")

''' ------------------create account route below--------------'''
# create account route
@myapp_obj.route("/create_account", methods=['GET', 'POST'])
def create_account():
    # checks if user is logged in
    if current_user.is_authenticated:
        return redirect('/home')
    form = CreateAccount()
    if form.validate_on_submit():
        u = User(username=form.username.data, email=form.email.data)
        u.set_password(form.password.data)  # sets password hash
        # adds new user to database
        db.session.add(u)
        db.session.commit()
        flash('New Account Created. You can now login', 'accSuccess')
        return redirect('/login')
    return render_template("create_account.html", form=form)

''' ----------------------view page route below ----------------'''
@myapp_obj.route("/view_page/<int:page_id>", methods=['GET', 'POST'])
def view_page(page_id):
    name, notes, page_notes, shared = home_helper()
    page = Page.query.get_or_404(page_id)
    form = ViewPage()

    if request.method == 'GET':
        form.title.data = page.title
        form.body.data = page.description

    if form.validate_on_submit():
        page.title = form.title.data
        page.description = form.body.data

        db.session.commit()
        flash("Edited Page Successfully", "editPageSuccess")
        return redirect(url_for("view_page", page_id=page_id))
    else:
        print(form.errors)
        print(request.form)
    return render_template('view_page.html', page=page, form=form, name=name, notes=notes, page_notes=page_notes, shared=shared)

" -----------------------view note route below-------------------"
# view note route
@myapp_obj.route('/view_note/<int:note_id>', methods=['GET', 'POST'])
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    form = ViewNote()
    owner = User.query.get_or_404(note.owner)  #gives the user as a user data entry

    if request.method == 'GET':
        form.title.data = note.title
        form.body.data = note.body

    if form.validate_on_submit():
        #add checks to make sure title is still unique
        note.title = form.title.data
        note.body = request.form['content']
        note.timestamp = datetime.now()
        db.session.commit()
        flash('Note edited successfully!', 'noteEditSuccess')
        return redirect(url_for('view_note', note_id=note_id))
    else:
        print(form.errors)
        print(request.form)
    name, notes, page_notes, shared = home_helper()
    return render_template('view_note.html', form=form, owner=owner.username, note=note, name=name, notes=notes, page_notes=page_notes, shared=shared)

''' --------------------create note route below------------------------'''
# create note route
@myapp_obj.route('/create_note', methods=['GET', 'POST'])
def create_note():
    form = CreateNote()

    ''' for populating templates dropdown menu'''
    choices = Template.query.filter(Template.user_id == current_user.id, Template.trashed == False).all()
    #inserts dummy template, default is a blank template for user to start with
    dummy_template = Template(id=0, title="Blank Note", body="", author=current_user)
    choices.insert(0, dummy_template)
    form.template_menu.choices = choices

    ''' for populating pages dropdown menu'''
    page_choices = Page.query.filter(Page.user_id == current_user.id, Page.trashed == False).all()
    default_page = Page(id=0, title="No Page", description="", author=current_user)
    page_choices.insert(0, default_page)
    form.page_menu.choices = page_choices
    print(page_choices)
    print(choices)

    if form.validate_on_submit():
        print("entered")
        notes = Note(owner=current_user.id, title=form.title.data, body=request.form['content'], page=form.page_menu.data, author=current_user)
        # clears form
        form.title.data = ''
        #form.body.data = ''
        
        # adds to database
        db.session.add(notes)
        db.session.commit()
        
        flash('Note created successfully! Find it on the side bar to make changes.', 'noteSuccess')
        return redirect('/create_note')
    else:
        print(form.errors) #this prints {} if there are no errors
        print(request.form) #prints ImmutableMultiDict([]) if there are no errors
    name, notes, page_notes, shared = home_helper()
    return render_template('create_note.html', form=form, name=name, notes=notes, page_notes=page_notes, shared=shared)

''' -----------------------create template methods below--------------------'''
# create template route
@myapp_obj.route('/create_template', methods=['GET', 'POST'])
def create_template():
    form = CreateTemplate()
    if form.validate_on_submit():
        template = Template(title=form.title.data, body=request.form['content'], author=current_user)
        
        # clears form
        form.title.data = ''
        #form.body.data = ''
        
        # adds to database
        db.session.add(template)
        db.session.commit()
        
        flash('Template created successfully!', 'templateSuccess')
        return redirect('/create_template')
    name, notes, page_notes, shared = home_helper()
    return render_template('create_template.html', form=form, name=name, notes=notes, page_notes=page_notes, shared=shared)

''' template helper method, used in create note '''
#handles getting a template based on its id, called from create_note.html
#helper method, not called to view page
@myapp_obj.route('/get_template_body/<int:entry_id>')
def get_body(entry_id):
    entry = Template.query.get(entry_id)
    
    if entry:
        return jsonify({'body': entry.body})
    elif entry_id == 0:
        return jsonify({'body': ""})
    else:
        return jsonify({'error': "entry not found"}), 404

''' -------------------------create page route below--------------------'''
# create page route
@myapp_obj.route('/create_page', methods=['GET', 'POST'])
def create_page():
    form = CreatePage()
    if form.validate_on_submit():
        page = Page(title=form.title.data, description=form.description.data, author=current_user)
        
        # clears form
        form.title.data = ''
        form.description.data = ''
        
        # adds to database
        db.session.add(page)
        db.session.commit()
        
        flash('Page created successfully!', 'pageSuccess')
        return redirect('/create_page')
    name, notes, page_notes, shared = home_helper()
    return render_template('create_page.html', form=form, name=name, notes=notes, page_notes=page_notes, shared=shared)

'''-------------------------- search route below ------------------------------'''
# search route
@myapp_obj.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    name, notes, page_notes, shared = home_helper()
    if form.validate_on_submit():
        search_query = form.searched.data
        #contains the notes that were sifted from search query
        results = Note.query.filter(Note.body.contains(search_query) | Note.title.contains(search_query)).all()
        all_notes = Note.query.filter(Note.user_id == current_user.id, Note.trashed == False).all()
        #makes sure that results is only from this user
        for result in results:
            if result not in all_notes:
                results.remove(result)

        return render_template("search.html", results=results, form=form, notes=notes, name=name, page_notes=page_notes, shared=shared)
    return render_template("search.html", form=form, notes=notes, name=name, page_notes=page_notes, shared=shared)

''' ------------------------- trash method below ----------------------------'''
# view trashed notes
@myapp_obj.route('/trash')
def trash():
    name, notes, page_notes, shared = home_helper()
    user = current_user
    trashed_notes = Note.query.filter(Note.user_id == current_user.id, Note.trashed == True).all()
    trashed_pages = Page.query.filter(Page.user_id == current_user.id, Page.trashed == True).all()
    trashed_templates = Template.query.filter(Template.user_id == current_user.id, Template.trashed == True)
    form = NoteManagment()
    return render_template('trash_folder.html', trashed_notes=trashed_notes, form=form, notes=notes, name=name, page_notes=page_notes, shared=shared, trashed_pages=trashed_pages, trashed_templates=trashed_templates)
    
''' helper method for trash '''
# note management handles deletion and recovery
# TODO: find a way to get the page of the note if applicable
@myapp_obj.route('/trash/note_man/<int:note_id>', methods=['GET', 'POST'])
def note_man(note_id):
    form = NoteManagment()
    note = Note.query.get_or_404(note_id)
    page_of_note = 

    if form.validate_on_submit():
        # user selects to delete note
        if form.delete.data:    
            db.session.delete(note)       
            print("Note is deleted")
            print(form.delete.data)
            flash(f'"{note.title}" has been deleted', 'deletionSuccess')
        # user selects to recover note
        elif form.recover_note.data:  
            if note.page == '0':
                note.trashed = False
                print("note is recoverd")
                flash(f'"{note.title}" has been recovered')
            elif note.page != '0' and note.page.trashed == True:   # cant recover a note inside a page when page is trashed
                flash("Error: Cannot recover a note from a trashed page", 'notePgError')
                return redirect ('/trash')
        db.session.commit()
    return redirect('/trash')


# moves note to trash
@myapp_obj.route('/view_note/move_to_trash/<int:note_id>', methods=['GET', 'POST'])
def move_to_trash(note_id):
    note = Note.query.get_or_404(note_id)
    try:
        note.trashed = True
        note.trashed_time = datetime.utcnow()
        db.session.commit()
        flash(f'"{note.title}" moved to trash', 'trashSuccess')
        print(f'"{note.title}" moved to trash')
    except:
        flash(f'Error: "{note.title} could not be moved to trash"', 'trashError')
        print(f'Error: "{note.title} could not be moved to trash"')
        
    return redirect('/trash')

''' ------------------ share note route below ----------------------- '''
# sharing between users
@myapp_obj.route('/share_note/<int:note_id>', methods=['GET', 'POST'])
def share_note(note_id):
    name, notes, page_notes, shared = home_helper()
    shared_note = Note.query.get_or_404(note_id)
    form = ShareNote()
    if form.validate_on_submit():
        # gets email of recipient of note
        recipient_email = form.recipient.data
        # look in db for user that has that email
        recipient = User.query.filter(User.email == recipient_email).first()
        form.recipient.data = ''
        
        if recipient:
            # creates a copy of shared note for recipient to recieve
            note = Note(owner=current_user.id, title=f"{shared_note.title}", body=shared_note.body, user_id=recipient.id)
            # commits note to recipients database
            db.session.add(note)
            db.session.commit()
            flash('Note Shared Succesfully', 'shareSuccess')
            
        else:
            flash('User not found', 'shareError')
    return render_template('share_note.html', form=form, shared_note=shared_note, name=name, notes=notes, page_notes=page_notes, shared=shared)

''' --------------------- view profile route below ------------------'''
@myapp_obj.route("/view_profile", methods=['GET', 'POST'])
def view_profile():
    name, notes, page_notes, shared = home_helper()
    form = ViewProfile()

    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data

        db.session.commit()

        flash("Profile Edited Succesfully!", "profileEditSuccess")
        return redirect('/view_profile')
    else:
        print(form.errors)
        print(request.form)
    return render_template('view_profile.html', form=form, name=name, notes=notes, page_notes=page_notes, shared=shared)

''' ----------- chage password route, button for this is on edit profile page --------- '''
@myapp_obj.route('/change_password', methods=['GET', 'POST'])
def change_password():
    name, notes, page_notes, shared = home_helper()
    form = ChangePassword()

    if form.validate_on_submit():
        if current_user.check_password(form.old_password.data):
            current_user.set_password(form.new_password.data)

            db.session.commit()
            flash("Password changed successfully", "changePasswordSuccess")
            return redirect('/change_password')
        else:
            flash("Incorrect password", "changePasswordFail")
            return redirect('/change_password')
    else:
        print(form.errors)
        print(request.form)
    return render_template('change_password.html', form=form, name=name, notes=notes, page_notes=page_notes, shared=shared)

''' --------------------- helper method that holds home page info ---------------'''
#used for any pages that extend home.html
def home_helper():
    user = current_user
    name = user.username
    notes = Note.query.filter(Note.page == 0, Note.user_id == user.id, Note.trashed == False, Note.owner == current_user.id).all()
    shared = Note.query.filter(Note.page == 0, Note.user_id == user.id, Note.trashed == False, Note.owner != current_user.id).all()
    pages = Page.query.filter(Page.user_id == user.id, Page.trashed == False).all() #pages
    notes_w_pages = Note.query.filter(Note.page != "[NO_PAGE]", Note.user_id == user.id, Note.trashed == False).all() #notes in pages
    page_notes = {}
    for page in pages:
        page_notes[page] = []
    #adds notes to a dictionary where { key: page -> value: [list of its notes] }
    for note in notes_w_pages:
        for page in pages:
            if page.id == int(note.page):
                page_notes[page].append(note)

    
    return name, notes, page_notes, shared


''' ---------------------- move page to trash route below ---------------- '''
@myapp_obj.route('/view_page/move_to_trash1/<int:page_id>', methods=['GET', 'POST'])
def move_to_trash1(page_id):
    page = Page.query.get_or_404(page_id)
    user = current_user
    notes = Note.query.filter(Note.page == page_id, Note.user_id == user.id, Note.trashed == False, Note.owner == current_user.id).all()
    # if a notes has pages then all those pages need to be trashed aswell
    try:
        if notes:   # if there a notes in the current page move them to trash aswell
            for note in notes:
                flash(f'"{note.title}" from "{page.title}" moved to trash', 'trashSuccess')
                print(f'"{note.title}" moved to trash')
                note.trashed = True
                page.trashed_time = datetime.utcnow()
        
        page.trashed = True  # move page to trash
        page.trashed_time = datetime.utcnow()   # captures time when page was trashed
        db.session.commit()
        flash(f'"{page.title}" moved to trash', 'trashSuccess')
        print(f'"{page.title}" moved to trash')
        
    except:
        flash(f'Error: "{page.title} could not be moved to trash"', 'trashError')
        print(f'Error: "{page.title} could not be moved to trash"')
        
    return redirect('/trash')


''' helper method for trashed pages '''
# handles the deletion and recovery of pages
@myapp_obj.route('/trash/page_man/<int:page_id>', methods=['GET', 'POST'])
def page_man(page_id):
    form = NoteManagment()
    page = Page.query.get_or_404(page_id)
    notes_in_page = Note.query.filter(Note.page == page_id, Page.user_id == current_user.id)
    user = current_user
    # notes = Note.query.filter(Note.page == page_id, Note.user_id == user.id, Note.trashed == False, Note.owner == current_user.id).all()
    if form.validate_on_submit():
        # user selects to delete page
        if form.delete.data:
            for notes in notes_in_page:     # if there are notes in the page, when page is deleted, all notes are deleted
                db.session.delete(notes)    
            db.session.delete(page)       
            print(form.delete.data)
            flash(f'"{page.title}" has been deleted with all its notes', 'deletionSuccess')
        # user selects to recover page
        elif form.recover_note.data:  
            page.trashed = False
            for notes in  notes_in_page:     # if there are notes in the page, when page is recovered, they are all recovered aswell
                notes.trashed = False
            flash(f'"{page.title}" has been recovered with all its notes', 'recoverySuccess')
        db.session.commit()
    return redirect('/trash')


''' ---------------------- template deletion below ---------------- '''
# user can see their templates here
@myapp_obj.route('/template', methods=['GET', 'POST'])
def templates():
    user = current_user
    name, notes, page_notes, shared = home_helper()
    templates = Template.query.filter(Template.user_id == user.id, Template.trashed == False, Template.user_id == current_user.id).all()
    return render_template('template.html', templates=templates, name=name, notes=notes, shared=shared, page_notes=page_notes)

''' helper method for moving templates to trash '''
# moves template to trash
@myapp_obj.route('/templates/move_to_trash2/<int:temp_id>', methods=['GET', 'POST'])
def move_to_trash2(temp_id):
    template = Template.query.get_or_404(temp_id)
    user = current_user
    try:
        # move page to trash
        template.trashed = True
        template.trashed_time = datetime.utcnow()
        db.session.commit()
        flash(f'"{template.title}" moved to trash', 'trashSuccess')   
    except:
        flash(f'Error: "{template.title} could not be moved to trash"', 'trashError')
        
    return redirect('/trash')

''' helper method for trashed templates '''
# handles the template deletion and recovery
@myapp_obj.route('/trash/temp_man/<int:temp_id>', methods=['GET', 'POST'])
def temp_man(temp_id):
    form = NoteManagment()
    template = Template.query.get_or_404(temp_id)

    if form.validate_on_submit():
        # user selects to delete template
        if form.delete.data:    
            db.session.delete(template)       
            print(form.delete.data)
            flash(f'"{template.title}" has been deleted', 'deletionSuccess')
        # user selects to recover template
        elif form.recover_note.data:  
            template.trashed = False
            flash(f'"{template.title}" has been recovered', 'recoverySuccess')
        db.session.commit()
    return redirect('/trash')


''' ---------------------- delete profile route ---------------- '''
@myapp_obj.route("/view_profile/delete_profile", methods=['GET', 'POST'])
def delete_profile():
    user = current_user
    name, notes, page_notes, shared = home_helper()
    templates = Template.query.filter(Template.user_id == current_user.id, Template.trashed == False).all()
    # if users had, notes, pages, shared notes, or templates, delete them all from database
    try:
        if notes:  
            for note in notes:
                db.session.delete(note)
        if page_notes:
            for pages in page_notes:
                db.session.delete(pages)
        if shared:
            for notes in shared:
                db.session.delete(notes)
        if templates:
            for template in templates:
                db.session.delete(template)
                
        db.session.delete(user) # deletes users from database
        db.session.commit()
        flash("Account successfully deleted. Sorry to see you go.", 'accDelete')
    except:
        print("Account deletion error.")
    
    return redirect('/login')