from kafka import KafkaProducer
import json

try:
    producer = KafkaProducer(
        bootstrap_servers='localhost:29092',
        security_protocol="PLAINTEXT",
        value_serializer=lambda v: json.dumps(v).encode('ascii')
    )

    producer.send(
     'allan',
     value={
         "name": "Evy Lina 2",
         "hotel": "Cheap Hotel são paulo",
         "dateFrom": "14-07-2024",
         "dateTo": "01-08-2021",
         "details": "Wish coffee ready"
         }
    )
    producer.flush()
    
except Exception as e:
    # Lidando com qualquer outra exceção não especificada acima
    print("Ocorreu um erro:", e)