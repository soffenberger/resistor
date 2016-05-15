import pip
	
def install(package):
	pip.main(['install',package])

install('python-opencv')
install('--upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0-cp27-none-linux_x86_64.whl')
install('numpy')
install('SQLAlchemy')
install('python-opencv')
