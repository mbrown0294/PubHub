# main.py

from app import app
import db_setup
from forms import WorkSearchForm, WorkForm
from flask import flash, render_template, request, redirect
from models import Work, Author, association
from tables import Results # sort_url

db_session = db_setup.db_session
db_setup.init_db()

@app.route('/', methods=['GET','POST'])
def index():
	search = WorkSearchForm(request.form)
	if request.method == 'POST':
		return search_results(search)

	return render_template('index.html', form=search)
###########################################
@app.route('/all')
def full():
	qry = Work.query.join(association).join(Author).filter((association.c.work_id == Work.id) & (association.c.author_id == Author.id))
	results = qry.all()
	table = Results(results)
	table.border = True
	return render_template('results.html', table=table)
###########################################

@app.route('/results')
def search_results(search):
	results = []
	search_string = search.data['search']
	
	"""
	sort = request.args.get('sort', 'id')
	reverse  = (request.args.get('direction', 'asc') == 'desc')
	"""

	if search_string:
		if search.data['select'] == 'Author':
			qry = db_session.query(Work, Author).filter(
				Author.id == Work.author_id).filter(
					Author.name.contains(search_string))
			results = [item[0] for item in qry.all()]
		elif search.data['select'] == 'Work Title':
			qry = db_session.query(Work).filter(
				Work.title.contains(search_string))
			results = qry.all()
		elif search.data['select'] == 'Department':
			qry = db_session.query(Work).filter(
				Work.department.contains(search_string))
			results = qry.all()
		elif search.data['select'] == 'Publication Date':
			qry = db_session.query(Work).filter(
				Work.publication_date.contains(search_string))
			results = qry.all()
		else:
			qry = db_session.query(Work)
			results = qry.all()
		
	else:
		qry = db_session.query(Work)
		results = qry.all()

	if not results:
		flash('No results found.')
		return redirect('/')
	else:
		# display results
		table = Results(results)
		table.border = True
		return render_template('results.html', table=table)

	
@app.route('/new_work', methods=['GET','POST'])
def new_work():
	"""
	Add a new publication
	"""
	form = WorkForm(request.form)

	if request.method == 'POST' and form.validate():
		# save the work
		work = Work()
		save_changes(work, form, new=True)
		flash('Work published successfully.')
		return redirect('/')

	return render_template('new_work.html', form=form)

app.route('/hello')
def hello():
	return render_template('hello.html')

def save_changes(work, form, new=False):
	"""
	Save the changes to the database
	"""
	# Get data from form and assign it to the correct attributes
	# of the SQLAlchemy table object
	author = Author()
	author.name = form.author.data
	
	work.author = author
	work.title = form.title.data
	work.date = form.date.data

	if new:
		# Add the new album to the database
		db_session.add(work)
	
	# commit the data to the database
	db_session.commit()

@app.route('/item/<int:id>', methods=['GET','POST'])
def edit(id):
	qry = db_session.query(Work).filter(
		Work.id==id)
	work = qry.first()

	if work:
		form = WorkForm(formdata=request.form, obj=work)
		if request.method == 'POST' and form.validate():
			# save edits
			save_changes(work, form)
			flash('Publication edited successfully!')
			return redirect('/')
		return render_template('edit_work.html', form=form)
	else:
		return 'Error loading #{id}'.format(id=id)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
	"""
	Delete the item in the database that matches the specified id in the URL 	"""
	qry = db_session.query(Work).filter(
		Work.id==id)
	work = qry.first()

	if work:
		form = WorkForm(formdata=request.form, obj=work)
		if request.method == 'POST' and form.validate():
			# delete the item from the database
			db_session.delete(work)
			db_session.commit()

			flash('Work deleted successfully.')
			return redirect('/')
		return render_template('delete_album.html', form=form)
	else:
		return 'Error deleting #{id}'.format(id=id)

if __name__ == "__main__":
	app.run()
