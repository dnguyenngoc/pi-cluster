# Pi Cluster Webscan

We want to deploy the webscan module to the Raspberry Pi Cluster.
For a test deployment we use 5 x Raspberry Pi 4 8GB RAM and a 32GB MicroSD.
Every Pi execute different task. We split it like that:
Pi1 - Router/Loadbalancer
Pi2 - FTP Fileserver
Pi3 - Database
Pi4 - Webserver and ML
Pi5 - Webserver and ML
The technology stack we use for the pi are the following:
Pi3 - MySQL, Redis
Pi4 - OCR/Tesseract
Pi5 - OCR/Tesseract