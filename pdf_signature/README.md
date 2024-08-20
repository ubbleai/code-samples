# Check PDF signature
## Set Your Data
- copy your data in `data/pdf_signature` folder
    - `signed_report.pdf`

## Python

- start the container: `docker compose up python -d`
- run check webhook signature: `dc exec python python /app/check_pdf_signature.py`