import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings



ADMIN_EMAIL = settings.ADMIN_EMAIL
FROM_EMAIL = settings.FROM_EMAIL
EMAIL_PASSWORD = settings.EMAIL_PASSWORD
EMAIL_SMTP_SERVER = settings.EMAIL_SMTP_SERVER
EMAIL_SMTP_PORT=465
# RECIPIENT_EMAIL=settings.RECIPIENT_EMAIL
RECIPIENT_EMAIL = "dannyxpensive@gmail.com"
MAIN_ADMIN = ADMIN_EMAIL



def send_beautiful_html_email_to_admin(
    name, 
    email, 
    phone,
    country, 
    amount, 
    transaction_date, 
    comment,
    tmethod
):
    # Email subject
    subject = "Here are the credentials of the client"
    
    # Create the HTML content
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; padding: 20px;">
        <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <h1 style="color: #4CAF50;">Hello, admin. </h1>
            <p>A client filed a complaint. Here are the details of the filed complaint:</p>
            <table border="1" cellspacing="0" cellpadding="10" style="border-collapse: collapse; width: 100%; max-width: 600px; margin: 20px 0;">
                <tr>
                    <th style="background-color: #f2f2f2; text-align: left;">Field</th>
                    <th style="background-color: #f2f2f2; text-align: left;">Value</th>
                </tr>
                <tr>
                    <td><strong>Name</strong></td>
                    <td>{name}</td>
                </tr>
                <tr>
                    <td><strong>Email</strong></td>
                    <td>{email}</td>
                </tr>
                <tr>
                    <td><strong>Phone</strong></td>
                    <td>{phone}</td>
                </tr>
                <tr>
                    <td><strong>Country</strong></td>
                    <td>{country}</td>
                </tr>
                <tr>
                    <td><strong>Amount</strong></td>
                    <td>{amount}</td>
                </tr>
                <tr>
                    <td><strong>Payment Method</strong></td>
                    <td>{tmethod}</td>
                </tr>
                <tr>
                    <td><strong>Transaction Date</strong></td>
                    <td>{transaction_date}</td>
                </tr>
                <tr>
                    <td><strong>Comment</strong></td>
                    <td>{comment}</td>
                </tr>
            </table>
            <p style="margin-top: 20px;">Best regards,<br>Jami Gray Asset Recovery</p>
        </div>
    </body>
    </html>
    """

    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    # Attach the HTML content to the email
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Set up the SMTP server connection using SSL
        with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.login(FROM_EMAIL, EMAIL_PASSWORD)  # Log in with Hostinger credentials
            
            # Send the email
            server.sendmail(FROM_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        
        print(f"HTML email successfully sent to {RECIPIENT_EMAIL}!")
    except Exception as e:
        print(f"Failed to send email to {RECIPIENT_EMAIL}: {e}")

