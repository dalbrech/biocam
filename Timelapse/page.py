import web


urls = ( 
	'/', 'Index'
)


class Index: 
	def __init__(self):
		self.render=web.template.render('/home/pi/Templates/')
	def GET(self, name = None):
		return self.render('/home/pi/Timelapse/static/last_image.jpg')


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

