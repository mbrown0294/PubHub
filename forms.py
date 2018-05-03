# forms.py

from wtforms import Form, StringField, SelectField, validators

class WorkSearchForm(Form):
	choices = [('Work Title','Work Title'),
		('Author', 'Author'),
		('Department','Department'),
		('Publication Date','Publication Date')]
	select = SelectField('', choices=choices)
	search = StringField('')

class WorkForm(Form):
	author = StringField('Author', [validators.InputRequired(message="Please fill in all required fields")], render_kw={"placeholder": "Last, First (MI)"})
	title = StringField('Work Title')
	department = StringField('Department')
	date = StringField('Publication Date', [validators.Regexp(regex="(0[1-9]|1[012])/(0[1-9]|[12][0-9]|3[01])/(19|20)\d\d", message="Please use valid date syntax")], render_kw={"placeholder": "MM/DD/YYYY"})
