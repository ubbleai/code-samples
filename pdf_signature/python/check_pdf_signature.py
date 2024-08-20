from pyhanko.keys import load_cert_from_pemder
from pyhanko_certvalidator import ValidationContext
from pyhanko.pdf_utils.reader import PdfFileReader
from pyhanko.sign.validation import validate_pdf_signature
from pyhanko.sign.validation.settings import KeyUsageConstraints
from pyhanko.sign.validation import (
    validate_pdf_ltv_signature, RevocationInfoValidationType
)

# load public certificate
cert_file_name = "data/cko_idv_api_signature_public_certificate.crt"
root_cert = load_cert_from_pemder(cert_file_name)

# initialize validator
vc = ValidationContext(trust_roots=[root_cert])
ku = KeyUsageConstraints(key_usage={'digital_signature'})

with open('data/signed_report.pdf', 'rb') as doc:
    r = PdfFileReader(doc)
    sig = r.embedded_signatures[0]
    # validate signature
    status = validate_pdf_signature(sig, vc, key_usage_settings=ku)
    print(status.pretty_print_details())
