# vad365-azure-exercise
app.py exposes root at port 8080 and displays a simple "Hello World!" like message. To run app.py locally, you must have python installed with flask module installed. 

To run it in a docker container, install Docker desktop locally, and run the following commands.

```bash
docker build -t vad365-azure-exercise:latest .
docker run -d -p 8080:8080 vad365-azure-exercise
```

The application will be accessible at localhost:8080
