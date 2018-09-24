class Config(object):
#..
	UPLOAD_FOLDER = 'resume_uploads'
	ALLOWED_EXTENSIONS = '.jpg,.png,.pdf'
	SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/jobot'
	MONGO_DBNAME='jobot'
	MONGO_URI='mongodb://shubham21:shubham21@ds111913.mlab.com:11913/jobot'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEBUG = True
