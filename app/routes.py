from datetime import datetime
from flask import jsonify, render_template, redirect, flash, request, url_for
from flask_login import current_user, login_user, login_required, logout_user
from app import myapp_obj, db
from datetime import date
from .forms import LoginForm, CreateAccount, SearchForm, CreateNote, NoteManagment, CreateTemplate, ShareNote, ViewNote, CreatePage, ViewProfile
from .models import User, Note, Template, Page

'''for all routes add the flashed messages to html files'''

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
    choices = Template.query.filter(Template.user_id == current_user.id).all()
    #inserts dummy template, default is a blank template for user to start with
    dummy_template = Template(id=0, title="Blank Note", body="", author=current_user)
    choices.insert(0, dummy_template)
    form.template_menu.choices = choices

    ''' for populating pages dropdown menu'''
    page_choices = Page.query.filter(Page.user_id == current_user.id).all()
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
    trashed_notes = Note.query.filter(Note.user_id == current_user.id, Note.trashed == True).all()
    form = NoteManagment()
    name, notes, page_notes, shared = home_helper()
    return render_template('trash_folder.html', trashed_notes=trashed_notes, form=form, notes=notes, name=name, page_notes=page_notes, shared=shared)
    
''' helper method for trash '''
# note management handles deletion and recovery
@myapp_obj.route('/trash/note_man/<int:note_id>', methods=['GET', 'POST'])
def note_man(note_id):
    form = NoteManagment()
    note = Note.query.get_or_404(note_id)
    if form.validate_on_submit():
        # user selects to delete note
        if form.delete.data:    
            db.session.delete(note)       
            print("Note is deleted")
            print(form.delete.data)
            flash(f'"{note.title}" has been deleted', 'deletionSuccess')
        # user selects to recover note
        elif form.recover_note.data:   
            note.trashed = False
            print("note is recoverd")
            flash(f'"{note.title}" has been recovered', 'recoverySuccess')
        db.session.commit()
    return redirect('/trash')


# moves note to trash
@myapp_obj.route('/view_note/move_to_trash/<int:note_id>', methods=['GET', 'POST'])
def move_to_trash(note_id):
    note = Note.query.get_or_404(note_id)
    try:
        note.trashed = True
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

@myapp_obj.route("/view_profile", methods=['GET', 'POST'])
def view_profile():
    name, notes, page_notes, shared = home_helper()
    form = ViewProfile()

    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.password.data = current_user.password
    return render_template('view_profile.html', form=form, name=name, notes=notes, page_notes=page_notes, shared=shared)

''' --------------------- helper method that holds home page info ---------------'''
#used for any pages that extend home.html
def home_helper():
    user = current_user
    name = user.username
    notes = Note.query.filter(Note.page == 0, Note.user_id == user.id, Note.trashed == False, Note.owner == current_user.id).all()
    shared = Note.query.filter(Note.page == 0, Note.user_id == user.id, Note.trashed == False, Note.owner != current_user.id).all()
    pages = Page.query.filter(Page.user_id == user.id).all() #pages
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