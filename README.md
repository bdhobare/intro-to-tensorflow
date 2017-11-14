This is support code for my presentation at Nairobi Devfest on Tensorflow.
It is an introduction to Machine Learning using [Tensorflow](https://www.tensorflow.org)
Inspired by Martin Gorner's [presentation](https://codelabs.developers.google.com/codelabs/cloud-tensorflow-mnist/) at I/O 17 and the official Tensorflow docs

## Installing

Python 3 is recommended. Python 2 works as well if you adapt the installation instructions.

Installation instructions for straightforward pip install below.

If you are a power user under a specific Python environment ((virtualenv, anaconda,
docker), please visit tensorflow.org and follow the Python 3 instructions.

MacOS:
	# If you do not have it already, install git
	# Install the latest version of python 3
	# and run this on the command line so that python3 can access https:// URLs:
	sudo /Applications/Python\ 3.6/Install\ Certificates.command
	# Now you can install tensorflow and matplotlib
	pip3 install --upgrade tensorflow
	pip3 install --upgrade matplotlib

Ubuntu/Linux:
	sudo -H apt-get install git
	sudo -H apt-get install python3
	sudo -H apt-get install python3-matplotlib
	sudo -H apt-get install python3-pip
	sudo -H pip3 install --upgrade tensorflow
	# you might alo need to upgrade matplotlib, the version pulled by
	# apt-get is sometimes stale (but comes with the gfx backend)
	sudo -H pip3 install --upgrade matplotlib

Windows:
	Install Anaconda, Python 3 version: https://www.continuum.io/downloads#windows
	Anaconda comes with matplotlib built in.
	In the Anaconda shell type: pip install --upgrade tensorflow
		If you get the error "Could not find a version that satisfies the requirement (...)" try the following alternative:
		conda config --add channels conda-forge
		conda install tensorflow

TEST YOUR INSTALLATION:
    git clone https://github.com/bdhobare/intro-to-tensorflow.git
    cd intro-to-tensorflow
    python3 mnist.py
    => A window should appear displaying a graphical visualisation and you should also see training data in the terminal.
TEST TENSORBOARD
    cd intro-to-tensorflow
    python3 tensorboard.py
    tensorboard --logdir=graphs
    => Go to http://127.0.0.1:6006/. You should see the graphical representation
