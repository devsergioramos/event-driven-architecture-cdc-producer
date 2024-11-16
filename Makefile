pip-install:
	pip install -r requirements.txt

up:
	docker compose -f docker-compose.yaml up -d --remove-orphans

up-logs:
	docker compose -f docker-compose.yaml up

down:
	docker compose -f docker-compose.yaml down

create-connector:
	curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @register-postgres.json

start-monitoring:
	docker compose -f docker-compose.yaml exec broker /kafka/bin/kafka-console-consumer.sh \
    --bootstrap-server broker:9092 \
    --from-beginning \
    --property print.key=true \
    --topic dbserver1.public.package_status