import base64
from hashlib import sha512

from ecdsa.util import sigdecode_der
from ecdsa import VerifyingKey

import typer


def check_signature(raw_webhook_body_path: str, signature_path: str, key_path: str):
    signature = open(signature_path).read()
    raw_webhook_body = open(raw_webhook_body_path).read()
    (
        timestamp,
        ubble_signature_version,
        ubble_signature,
    ) = signature.split(":")
    
    # First we create the signed_payload
    signed_payload = (f"{timestamp}:{raw_webhook_body}").encode("utf-8")
    
    # Use the public key from the dashboard (check version from ubble_signature_version)
    public_key_file = open(key_path)
    
    # Generate veryfing key signature
    raw_key = public_key_file.read()
    verifying_key = VerifyingKey.from_pem(raw_key)

    # Verify the signature
    result = verifying_key.verify(
        base64.b64decode(ubble_signature.encode("utf-8")),
        signed_payload,
        hashfunc=sha512,
        sigdecode=sigdecode_der,
        allow_truncate=True,
    )
    if result:
        print("Success")
    else:
        print("Could not validate signature")


if __name__ == "__main__":
    typer.run(check_signature)