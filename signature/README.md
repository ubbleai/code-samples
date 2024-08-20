# Check Webhook and API response Signature
## Set Your Data
- copy your data in `data` folder
  - `public.key`
  - `raw_webhook_body.txt`
  - `signature.txt`
  - 
## Python

- start the container: `docker compose up python -d`
- run check webhook signature: `dc exec python python /app/check_webhook_signature.py /data/raw_webhook_body.txt /data/signature.txt /data/public.key`

## Java
- start the container: `docker compose up java -d`
- compile java: `docker compose exec java javac CheckWebhookSignature.java`
- run the check webhook signature: `docker compose exec java java CheckWebhookSignature /data/raw_webhook_body.txt /data/signature.txt /data/public.key`


## Check PDF signature
### Set Your Data
- copy your data in `data/pdf_signature` folder
  - `signed_report.key`
  