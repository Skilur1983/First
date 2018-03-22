from ap import db
from ap.models import User, Post
from datetime import datetime, timedelta

for id in range(1, 9):
    now = datetime.utcnow()
    p = Post(body="post from " + User.query.get(id).username, author=User.query.get(id), timestamp=now + timedelta(seconds=1))
    db.session.add(p)
    db.session.commit()