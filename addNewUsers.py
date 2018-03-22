from ap import db
from ap.models import User
from werkzeug.security import generate_password_hash, check_password_hash

u1 = User(username='john', email='john@example.com')
u2 = User(username='susan', email='susan@example.com')
u3 = User(username='mary', email='mary@example.com')
u4 = User(username='david', email='david@example.com')

db.session.add([u1, u2, u3, u4])
db.session.commit()