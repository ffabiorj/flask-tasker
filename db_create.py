# project/db_create.py


from views import db
from models import Task
from datetime import date


# create the dabase and the db table
db.create_all()


# import data
db.session.add(Task("Finish this tutorial", date(2015, 3, 13), 10, 1))
db.session.add(Task("Finish Real Python", date(2015, 3, 13), 10, 1))


# commit the changes
db.session.commit()

