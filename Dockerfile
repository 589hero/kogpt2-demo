FROM 589hero/kogpt2

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8051
CMD ["opyrator", "launch-ui", "server:generate_korean_contents"]