# vad365-azure-exercise
app.py exposes root at port 8080 and displays a simple "Hello World!" like message. To run app.py locally, you must have python installed with flask module installed. 

## Running on a virtual machine
* In order to run this app on a server, you'll need to install python. The easiest way to install python is using the operating system's package manager. Here's an example of how you'd do this on an Ubuntu machine.

```bash
sudo apt-get update
sudo apt-get install python3.8
```

* If you're using a windows virtual machine, you can download and install python using the graphical installer from https://www.python.org/downloads/windows/

* Once python is installed, you'll need to install a dependency that the app uses called `flask`. Issue the following command at the commandline of the server.

```bash
pip install flask
```
* Next step is to run the app. Issue the following command on the command line from the same directory where you copied app.py into.

```bash
python app.py
```

## Running it as a Docker container
To run it in a docker container, install Docker desktop locally, and run the following commands.

```bash
docker build -t vad365-azure-exercise:latest .
docker run -d -p 8080:8080 vad365-azure-exercise
```

The application will be accessible at localhost:8080
