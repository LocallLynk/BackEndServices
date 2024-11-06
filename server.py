import os
from dotenv import load_dotenv
import stripe


load_dotenv()

secret_key = os.getenv("SECRET_KEY")
stripe.api_key = "pk_test_51QHrdOC7mvmfqFsYwFgPTN8xrhgFwwHc1AiYwfoSzTZMIHx9L58V3GxOkVyTNuREDyf7vKsAWc8wPBQzybe6C7lf00tNzbLCbX"


stripe.PaymentIntent.create(
  amount=500,
  currency="usd",
  payment_method="pm_card_visa",
  payment_method_types=["card"],
)

# test card number: 4242 4242 4242 4242
# test card expiration date: 12/25
# test card CVC: 123
# test card type: Visa