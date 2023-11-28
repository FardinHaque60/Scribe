from flask import jsonify, render_template, redirect, flash, url_for
from flask_login import current_user, login_user, login_required, logout_user
from app import myapp_obj, db
from datetime import date
from .forms import LoginForm, CreateAccount, SearchForm, CreateNote, NoteManagment, CreateTemplate
from .models import User, Note, Template

'''for all routes add the flashed messages to html files'''

# dynamic code of home.html will work if I pass all the vars in main_page route(name, notes) to all routes
# TODO: it's too redundant so need to find a better solution
# REPLY: look into making notes = ... global then
# home route
@myapp_obj.route("/home")
@login_required # users that are not authenticated cannot access this link
def main_page():
    user = current_user
    name = user.username
    notes = Note.query.filter(Note.user_id == user.id, Note.trashed == False).all()

    return render_template('home.html', name=name, notes=notes)

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
            flash('Invalid username or password', 'error')
            return redirect("/login") 
        # Flask-Login function registers the user as logged in
        login_user(user, remember=form.remember_me.data)
        return redirect('/home')
    return render_template('login.html', form=form)


# logout route
@myapp_obj.route("/logout")
def logout():
    # Flask-Login function registers the user as logged out
    logout_user()
    return redirect ("/")


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
        db.session.add(u)
        db.session.commit()
        flash('New Account Created. You can now login')
        return redirect('/login')
    return render_template("create_account.html", form=form)


# view note route
@myapp_obj.route('/view_note/<int:note_id>', methods=['GET', 'POST'])
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    
    name =  current_user.username
    notes = Note.query.filter(Note.user_id == current_user.id, Note.trashed == False).all()
    
    return render_template('view_note.html', note=note, name=name, notes=notes)
    

# create note route
@myapp_obj.route('/create_note', methods=['GET', 'POST'])
def create_note():
    form = CreateNote()
    notes = Note.query.filter(Note.user_id == current_user.id, Note.trashed == False).all()
    choices = (Template.query.filter(Template.user_id == current_user.id).all())
    #inserts dummy template in first, just a blank template
    choices.insert(0, Template(id=0, title="blank note", body="", author=current_user))
    form.template_menu.choices = choices
    if form.validate_on_submit():
        notes = Note(title=form.title.data, body=form.body.data, author=current_user)
        
        # clears form
        form.title.data = ''
        form.body.data = ''
        
        # adds to database
        db.session.add(notes)
        db.session.commit()
        
        flash('Note created successfully!', 'success')
        return redirect('/home')
    
    return render_template('create_note.html', form=form, name=current_user.username, notes=notes)

#handles getting a template based on its id, called from create_note.html
@myapp_obj.route('/get_template_body/<int:entry_id>')
def get_body(entry_id):
    entry = Template.query.get(entry_id)
    
    if entry:
        return jsonify({'body': entry.body})
    else:
        return jsonify({'body': ""})

# create template route
@myapp_obj.route('/create_template', methods=['GET', 'POST'])
def create_template():
    form = CreateTemplate()
    notes = Note.query.filter(Note.user_id == current_user.id, Note.trashed == False).all()
    if form.validate_on_submit():
        template = Template(title=form.title.data, body=form.body.data, author=current_user)
        
        # clears form
        form.title.data = ''
        form.body.data = ''
        
        # adds to database
        db.session.add(template)
        db.session.commit()
        
        flash('Template created successfully!', 'success')
        return redirect('/home')
    
    return render_template('create_template.html', form=form, name=current_user.username, notes=notes)

# create page route
@myapp_obj.route('/create_page', methods=['GET', 'POST'])
def create_page():
    form = CreateTemplate()
    notes = Note.query.filter(Note.user_id == current_user.id, Note.trashed == False).all()
    if form.validate_on_submit():
        template = Template(title=form.title.data, body=form.body.data, author=current_user)
        
        # clears form
        form.title.data = ''
        form.body.data = ''
        
        # adds to database
        db.session.add(template)
        db.session.commit()
        
        flash('Template created successfully!', 'success')
        return redirect('/home')
    
    return render_template('create_page.html', form=form, name=current_user.username, notes=notes)

# search route
@myapp_obj.route('/search', methods=['GET', 'POST'])
def search():
    user = current_user
    form = SearchForm()
    #contains all the notes for this user
    notes = Note.query.filter(Note.user_id == user.id, Note.trashed == False).all()
    
    if form.validate_on_submit():
        search_query = form.searched.data
        #contains the notes that were sifted from search query
        results = Note.query.filter(Note.body.contains(search_query) | Note.title.contains(search_query)).all()
        #below sets results to the intersection of this users notes and the resultant notes
        #TODO: not sure if this will always work since it converts to a set
        results = set(results) & set(notes)

        return render_template("search.html", form=form, results=results, notes=notes, name=current_user.username)

    return render_template("search.html", form=form, notes=notes, name=current_user.username)

# view trashed notes
@myapp_obj.route('/trash')
def trash():
    user = current_user
    name =  user.username
    notes = Note.query.filter(Note.user_id == current_user.id, Note.trashed == False).all()
    
    trashed_notes = Note.query.filter(Note.user_id == user.id, Note.trashed == True).all()
    form = NoteManagment()
    
    return render_template('trash_folder.html', trashed_notes=trashed_notes, form=form, notes=notes, name=name)
    
# note management(choose a better name for note_man) handles deletion and recovery
@myapp_obj.route('/trash/note_man/<int:note_id>', methods=['GET', 'POST'])
def note_man(note_id):
    user = current_user
    # trashed_notes = Note.query.filter(Note.user_id == user.id, Note.trashed == True).all()
    form = NoteManagment()
    note = Note.query.get_or_404(note_id)
    if form.validate_on_submit:
        
        if form.delete.data:    
            db.session.delete(note)       
            print("Note is deleted")
        elif form.recover_note.data:   
            note.trashed = False
            print("note is recoverd")
        db.session.commit()
    return redirect('/trash')
    # return render_template('trash_folder.html', trashed_notes=trashed_notes, form=form)

# moves note to trash
@myapp_obj.route('/view_note/move_to_trash/<int:note_id>', methods=['GET', 'POST'])
def move_to_trash(note_id):
    user = current_user
    note = Note.query.get_or_404(note_id)
    # trashed_notes = Note.query.filter(Note.user_id == user.id, Note.trashed == True).all()
    # form = NoteManagment()
    try:
        note.trashed = True
        db.session.commit()
        flash("Note moved to trash")
        print("Note moved to trash")
        
    except:
        flash("There a problem moving note to trash")
        print("There a problem moving note to trash")
        
    return redirect('/home')
