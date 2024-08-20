# integration-demo project

## Purpose
The purpose of this project is to have a simple way to create integration demo code in multiple languages.
This project includes
- a docker-compose file to configure languages environments
- a folder by language containing demo code
- a data folder shared by all languages

# Demo code list
## Check Webhook and API response Signature
### Set Your Data
- copy your data in `data/signature` folder
  - `public.key`
  - `raw_webhook_body.txt`
  - `signature.txt`
  - 
### Python

- start the container: `docker compose up python -d`
- run check webhook signature: `dc exec python python /app/check_webhook_signature.py /data/signature/raw_webhook_body.txt /data/signature/signature.txt /data/signature/public.key`

### Java
- start the container: `docker compose up java -d`
- compile java: `docker compose exec java javac CheckWebhookSignature.java`
- run the check webhook signature: `docker compose exec java java CheckWebhookSignature /data/signature/raw_webhook_body.txt /data/signature/signature.txt /data/signature/public.key`


## Check PDF signature
### Set Your Data
- copy your data in `data/pdf_signature` folder
  - `signed_report.key`

### Python

- start the container: `docker compose up python -d`
- run check webhook signature: `dc exec python python /app/check_pdf_signature.py`