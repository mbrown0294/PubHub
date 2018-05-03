# tables.py 

from flask_table import Table, Col, LinkCol
	
class Results(Table):
	classes = ['tablesorter']
	id = Col('Id', show=False)
	author = Col('Author')
	title = Col('Title')
	# department = Col('Department')
	date = Col('Publication Date')
	edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
	delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))
