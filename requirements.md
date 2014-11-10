Given a list of objects containing data, TableView should

* generate an HTML table with appropriate headers (derived from the Field 
objects)
* generate rows, converting object attributes to an appropriate HTML
representation
    * Field objects retrieve the data from the object it and convert it into an
    appropriate representation for HTML
    * it should be possible to have an additional column with special action
    links (ex. View, Edit, Delete)
    