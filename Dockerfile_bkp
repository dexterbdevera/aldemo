#Use official Python runtime image
FROM python:3.9

#Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

#Create directory and mount code to image
RUN mkdir -p /code
COPY . code /code/
WORKDIR /code

#Open port 
EXPOSE 8000

#Run the production server
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
