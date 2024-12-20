from django.core.mail import send_mail
from django.conf import settings
import logging

def send_payment_email(user_email, username, amount, reservation_id, car):
    try:
        subject = "Payment Confirmation"
        message = (
            f"Dear {username},\n\n"
            f"Thank you for your payment for reservation ID {reservation_id} and Model Car {car}.\n"
            f"The total amount of ${amount:.2f} has been successfully received.\n\n"
            f"We appreciate your business!\n\n"
            f"Best regards,\n"
            f"The Car Rental Team"
        )
        send_mail(subject, message, 'no-reply@alsirental.com', [user_email])
        return True
    except Exception as e:
        print(f"Email sending error: {e}")
        return False