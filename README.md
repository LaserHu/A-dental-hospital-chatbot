# A-dental-hospital-chatbot

Setup the service


1. Initialize dentist and timeslot data on MongoDB:
Open a new terminal under the folder initialization, type:
pip3 install -r requirements.txt python3 initialization.py


2. Run dentist service on port 5000:
Open a new terminal under the folder Dentist, type:
docker build -t doctor_service .
docker run -p 127.0.0.1:5000:5000 -t doctor_service


3. Run timeslot service on port 8888:
Open a new terminal under the folder Timeslot, type:
docker build -t timeslot_service .
docker run -p 127.0.0.1:8888:8888 -t timeslot_service


4. Run the chatbot service on:
Open a new terminal under the folder ChatbotApp, type:
pip3 install -r requirements.txt
python3 app.py
Open your browser and type http://127.0.0.1:10898/ in address bar to access the chatbot.
