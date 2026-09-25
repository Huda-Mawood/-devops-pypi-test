import ssl
from cryptography import x509

for storename in ("CA", "ROOT"):
    for cert, encoding, trust in ssl.enum_certificates(storename):
        if encoding != "x509_asn":
            continue
        try:
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            ctx.load_verify_locations(cadata=cert)
        except ssl.SSLError as e:
            print(f"--- BAD CERT in {storename} store ---")
            print("Error :", e)
            c = x509.load_der_x509_certificate(cert)
            print("Subject:", c.subject.rfc4514_string())
            print("Issuer :", c.issuer.rfc4514_string())
            print("Serial :", c.serial_number)
            print()