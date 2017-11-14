This is support code for my presentation at the 2017 Nairobi Devfest on Tensorflow.
It is an introduction to Machine Learning using [Tensorflow](https://www.tensorflow.org)
Inspired by Martin Gorner's [presentation](https://codelabs.developers.google.com/codelabs/cloud-tensorflow-mnist/) at I/O 17 and the official Tensorflow docs

## Installing

Python 3 is recommended. Python 2 works as well if you adapt the installation instructions.

Installation instructions for straightforward pip install below.

If you are a power user under a specific Python environment ((virtualenv, anaconda,
docker), please visit tensorflow.org and follow the Python 3 instructions.

### MacOS:
	# If you do not have it already, install git

	# Install the latest version of python 3

	# and run this on the command line so that python3 can access https:// URLs:

	sudo /Applications/Python\ 3.6/Install\ Certificates.command

	# Now you can install tensorflow and matplotlib

	1. pip3 install --upgrade tensorflow
	2. pip3 install --upgrade matplotlib

### Ubuntu/Linux:
	1. sudo -H apt-get install git
	2. sudo -H apt-get install python3
	3. sudo -H apt-get install python3-matplotlib
	4. sudo -H apt-get install python3-pip
	5. sudo -H pip3 install --upgrade tensorflow

	# you might alo need to upgrade matplotlib, the version pulled by

	# apt-get is sometimes stale (but comes with the gfx backend)

	6. sudo -H pip3 install --upgrade matplotlib

### Windows:
	1. Install Anaconda, Python 3 version: https://www.continuum.io/downloads#windows
	2. Anaconda comes with matplotlib built in.
	3. In the Anaconda shell type: pip install --upgrade tensorflow
		If you get the error "Could not find a version that satisfies the requirement (...)" try the following alternative:
		⋅⋅* conda config --add channels conda-forge
		⋅⋅* conda install tensorflow

TEST YOUR INSTALLATION:
    1. git clone https://github.com/bdhobare/intro-to-tensorflow.git
    2. cd intro-to-tensorflow
    3. python3 mnist.py
    ⋅⋅* => A window should appear displaying a graphical visualisation and you should also see training data in the terminal.
TEST TENSORBOARD
    1. cd intro-to-tensorflow
    2. python3 tensorboard.py
    3. tensorboard --logdir=graphs
    ⋅⋅* => Go to http://127.0.0.1:6006/. You should see the graphical representation
