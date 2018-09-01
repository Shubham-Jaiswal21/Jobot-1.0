class Config(object):
#..
	UPLOAD_FOLDER = 'resume_uploads'
	ALLOWED_EXTENSIONS = '.jpg,.png,.pdf'
	SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/jobot'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	DEBUG = True