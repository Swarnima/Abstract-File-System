SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=amazon.yaml
SERVERDIR=server/
DESTDIR=server/amazonS3/flaskConnexion

all: service start 
	@echo "service started"

container: docker-build docker-start
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	sudo docker build -t cloudmesh-amazonS3 .
	@echo "image DONE"

docker-pull:
	@echo "pulling the image from dockerhub..."
	docker pull cloudmesh-amazonS3
	@echo "image DONE"

docker-start:
	@echo "starting the service in container..."
	docker run -p 8080:8080 cloudmesh-amazonS3

docker-stop:
	@echo "stoping the service..."
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-remove:
	@echo "removing the image..."
	docker rmi -f cloudmesh-amazonS3
	@echo "image removed"

docker-clean: docker-stop docker-remove
	@echo "DONE"

dest:
	mkdir $(SERVERDIR)

service:dest 
	wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate  -i $(YAML)  -l python-flask  -o $(DESTDIR)  -D supportPython2=true
	
	rm *.jar
	
	sudo chmod -R 777 $(SERVERDIR)
	
	cp -r *.py $(DESTDIR)/swagger_server/controllers
	cd $(DESTDIR) && pip install boto && pip install -r requirements.txt && \
	python setup.py install && python -m swagger_server	

test:
	curl http://127.0.0.1:8080/cloudmesh/amazonS3/listBuckets
	
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	sudo rm -r $(SERVERDIR)
	rm *.jar

