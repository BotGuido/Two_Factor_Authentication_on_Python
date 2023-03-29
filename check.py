import pyotp

key = "ItsNoneOfYourBusiness"

totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter Password:")))