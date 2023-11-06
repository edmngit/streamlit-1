FROM python:3.10

# Expose port you want your app on
EXPOSE 8080

# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

# Copy app code and set working directory
#COPY text_explorer text_explorer
COPY stream.py stream.py
#COPY references references
WORKDIR .

# Run
ENTRYPOINT [“streamlit”, “run”, “stream.py”, “–server.port=8080”, “–server.address=0.0.0.0”]
