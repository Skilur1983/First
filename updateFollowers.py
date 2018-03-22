from ap import db
from ap.models import User, Post

f = 8
for id in range(1, 9):
    user = User.query.get(id).username
    followed = User.query.get(f).username
    User.query.get(id).follow(User.query.get(f))
    print("%(u)s follows %(f)s" % {'u': user, 'f': followed})
    f -= 1
    db.session.commit()