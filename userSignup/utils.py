from django.core import mail


class Util:
    @staticmethod
    def send_email(data):
        connection = mail.get_connection()

        # Manually open the connection
        connection.open()

        # Construct an email message that uses the connection
        email1 = mail.EmailMessage(
            data['subject'],
            data['email_body'],
            'princepreem1@gmail.com',
            [data['email']],
            connection=connection,
        )
        email1.send()
        connection.close()
