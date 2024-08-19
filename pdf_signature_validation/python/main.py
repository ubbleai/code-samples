from pyhanko.keys import load_cert_from_pemder
from pyhanko_certvalidator import ValidationContext
from pyhanko.pdf_utils.reader import PdfFileReader
from pyhanko.sign.validation import validate_pdf_signature
from pyhanko.sign.validation.settings import KeyUsageConstraints
from pyhanko.sign.validation import (
       validate_pdf_ltv_signature, RevocationInfoValidationType
   )

# load public certificate
cert_file_name = "public_cert.crt" # available in documentation 
root_cert = load_cert_from_pemder(cert_file_name)

# initialize validator
vc = ValidationContext(trust_roots=[root_cert])
ku = KeyUsageConstraints(key_usage={'digital_signature'})

with open('signed_pdf.pdf', 'rb') as doc:
  r = PdfFileReader(doc)
  # fetch embedded signature
  sig = r.embedded_signatures[0]
  # validate signature
  status = validate_pdf_ltv_signature(
  sig, RevocationInfoValidationType.ADOBE_STYLE,validation_context_kwargs={'trust_roots': [root_cert]})
  
  print(status.pretty_print_details())