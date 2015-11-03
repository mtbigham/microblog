from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')
	
	@property
	#Return true unless the object represents
	#user that shouldn't be allowed to authenticate
	def is_authenticated(self):
		return True
		
	@property
	#Return true unless user is inactive (banned)
	def is_active(self):
		return True
		
	@property
	#Return true only for fake users that aren't supposed to log in
	def is_anonymous(self):
		return False
		
	#Return unique id for user in unicode format
	def get_id(self):
		try:
			return unicode(self.id) #python2
		except NameError:
			return str(self.id) #python3
	
	def __repr__(self):
		return '<User %r>' % (self.nickname)
		
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return '<Post %r>' % (self.body)