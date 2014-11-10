import flask


class Field:
    def __init__(self, source, label=None):
        self.source = source
        self.label = label or source

    def get_obj_data(self, obj):
        """
        Internal function for retrieving the appropriate object attribute.
        Can be overridden to support more complex field types.
        :param obj: The object to be represented.
        :return:
        """
        return getattr(obj, self.source)

    def render_short(self, obj):
        """
        Converts an object's data to an HTML format for display where there's
        not a lot of space (ex. a table view).

        May perform some kind of truncation or leave out parts of data.
        :param obj: The object containing the data to represent.
        :return: HTML representation of the corresponding data.
        """
        raise NotImplementedError("TableField is an abstract base class")

    def render(self, obj):
        """
        Converts an object's data to an HTML format for display where space is
        not restricted (ex. a detail view).

        Should produce a full representation of the data.
        :param obj: The object containing the data to represent.
        :return: HTML representation of the corresponding data.
        """
        raise NotImplementedError("TableField is an abstract base class")


class TextField(Field):
    """
    Simple text field that converts the given data to a string.
    """
    def render(self, obj):
        return str(self.get_obj_data(obj))

    def render_short(self, obj):
        return self.render(obj)


class TableViewAction:
    """
    Allows special actions to be provided for a given Table based on reverse
    URL lookups for URLs.
    """
    def __init__(self, view, label):
        self.view = view
        self.label = label

    def get_url(self, obj):
        """
        Converts an object into its URL representation.
        """
        return flask.url_for(self.view, pk=obj.pk)


class TableView:
    """
    Ideally, this should be subclassed and have the attributes fields, template,
    and actions declared at the class level.
    """
    def __init__(self, fields=None, template=None, actions=None):
        if not hasattr(self, "fields"):
            self.fields = fields

        if not hasattr(self, "template"):
            self.template = template

        if not hasattr(self, "actions"):
            self.actions = actions

    def render(self, data):
        """
        Generates an HTML representation of the table.
        :param data: An iterable of objects to display.
        :return: The rendered table, wrapped in a Markup object so it can be
            inserted into a template.
        """
        return flask.Markup(
            flask.render_template(self.template, table=self, data=data))


class DetailView:
    """
    Ideally, this should be subclassed and have the attributes fields, template,
    and actions declared at the class level.
    """
    def __init__(self, fields=None, template=None, actions=None):
        if not hasattr(self, "fields"):
            self.fields = fields

        if not hasattr(self, "template"):
            self.template = template

        if not hasattr(self, "actions"):
            self.actions = actions

    def render(self, data):
        """
        Generates an HTML representation of the table.
        :param data: An iterable of objects to display.
        :return: The rendered table, wrapped in a Markup object so it can be
            inserted into a template.
        """
        return flask.Markup(
            flask.render_template(self.template, detail=self, record=data))
