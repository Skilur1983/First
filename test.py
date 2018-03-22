from ap import db
from ap.models import User, Post

i = 0
for id in range(1, 9):
    user = User.query.get(id).username
    print(user, i)
    print("%(u)s says Hello %(i)s times" % {'u': user, 'i': i})
    i += 1