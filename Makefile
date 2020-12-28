
PP=python
TARGETS=install

server:
	$(PP) weather_tcpserver.py
install:
	sudo cp weather_tcpserver.service /lib/systemd/system/
	sudo cp weather_tcpserver.py /usr/bin
	sudo chmod +x weather

clean:
	sudo rm -f /usr/bin/weather_tcpserver.py
	sudo rm -f /lib/systemd/system/weather_tcpserver.service
	sudo systemctl daemon-reload
	sudo systemctl stop weather_tcpserver.service

run:
	sudo systemctl enable weather_tcpserver.service
	sudo systemctl start weather_tcpserver.service



