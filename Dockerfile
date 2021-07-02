FROM 589hero/kogpt2

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8051
EXPOSE 8080

CMD ( opyrator launch-ui server:generate_korean_contents & ) && opyrator launch-api server:generate_korean_contents