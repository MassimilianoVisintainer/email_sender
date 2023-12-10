# Email Sender using Python and Gmail SMTP

This Python script demonstrates how to send an email using Gmail's SMTP server. It uses environment variables stored in a `.env` file to fetch email credentials securely.

## Prerequisites

1. Python 3.x installed on your system.
2. `python-dotenv` library installed. You can install it via pip:

    ```bash
    pip install python-dotenv
    ```

## Setup

1. Create a `.env` file in the same directory as the Python script.
2. Add the following variables to the `.env` file:

    ```plaintext
    EMAIL_SENDER=your_email_sender@example.com
    PASSWORD=your_email_password
    EMAIL_RECEIVER=receiver@example.com
    ```

    Replace `your_email_sender@example.com`, `your_email_password`, and `receiver@example.com` with your actual email credentials.

## How to Run

1. Make sure the `dotenv` and required modules are installed.
2. Run the Python script.

## Code Explanation

1. Load environment variables from `.env`.
2. Access environment variables for email sender, password, and receiver.
3. Compose an email message using `EmailMessage()` from `email.message`.
4. Set sender, receiver, subject, and body of the email.
5. Create an SSL context for secure communication.
6. Use `smtplib` to establish an SMTP connection to Gmail's SMTP server (`smtp.gmail.com`) using port `465`.
7. Login with email credentials and send the email using `smtp.send_message()`.

**Note**: Ensure that your Gmail account allows access for less secure apps or consider enabling two-factor authentication.

Feel free to modify the script and customize the email subject, body, and other settings as needed.
