from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    subject = 'Test Email Subject'
    message = 'This is a test email message.'
    from_email = 'noreply@example.com'  # Replace this with the sender's email address
    recipient_list = ['recipient@example.com']  # Replace this with the recipient's email address

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Test email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Error sending test email: {e}')
