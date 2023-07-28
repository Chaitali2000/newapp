FROM python
RUN pip install flask 
WORKDIR /src
COPY . .
EXPOSE 4545
CMD python code.py
