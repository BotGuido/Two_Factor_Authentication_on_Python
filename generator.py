import pyotp
import qrcode

key = "ItsNoneOfYourBusiness"

uri = pyotp.totp.TOTP(key).provisioning_uri(name="MyNameOMG", issuer_name="MyAppOMG")

qrcode.make(uri).save("totp.png")