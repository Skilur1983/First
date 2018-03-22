from ap import db
from ap.models import User
from werkzeug.security import generate_password_hash, check_password_hash

for id in range(4, 9):
    print(User.query.get(id).username)
    user = User.query.get(id)
    user.password_hash = generate_password_hash('pass')
    db.session.commit()
