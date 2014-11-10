from collections import namedtuple
import flask
from view_generator import TableView, TextField, TableViewAction, DetailView

app = flask.Flask(__name__)
app.config['DEBUG'] = True


Contact = namedtuple('Contact', ['pk', 'name', 'email', 'phone'])
contacts = [
    Contact(0, "Marfa", "marfa@example.com", "541 555 0100"),
    Contact(1, "Ula", "ula@example.com", "541 555 0101"),
    Contact(2, "Cadence", "cadence@example.com", "541 555 0102")
]

contact_fields = [
    TextField(source="name", label="Name"),
    TextField(source="email", label="Email"),
    TextField(source="phone", label="Phone",)
]
contact_actions = [
    TableViewAction('contact_detail_view', 'View'),
    TableViewAction('contact_edit_view', 'Edit')
]


class ContactsTableView(TableView):
    fields = contact_fields
    template = "table.html"
    actions = contact_actions


class ContactsDetailView(DetailView):
    fields = contact_fields
    template = "detail.html"
    actions = contact_actions


@app.route('/')
@app.route('/contacts')
def contact_table_view():
    view = ContactsTableView()

    return flask.render_template('base.html',
                                 page_title="Contacts",
                                 content=view.render(contacts))


@app.route('/contacts/<pk>')
def contact_detail_view(pk):
    contact = [c for c in contacts if str(c.pk) == pk][0]
    view = ContactsDetailView()
    return flask.render_template('base.html',
                                 page_title="Contacts",
                                 content=view.render(contact))


@app.route('/contacts/<pk>/edit')
def contact_edit_view(pk):
    return "Not implemented"


if __name__ == '__main__':
    app.run()
