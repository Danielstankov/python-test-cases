import unittest
from unittest.mock import patch
from emails import send_email


class TestEmails(unittest.TestCase):
    @patch("emails.smtplib.SMTP")
    def test_send_email(self, mock):
        send_email("test@hi", "hi", "good morning")

        mock.assert_called_with("smtp.example.com")

        example = mock.return_value
        example.sendmail.assert_called_with(
            "noreply@example.com", "test@hi", "Subject: hi,good morning"
        )


if __name__ == '__main__':
    unittest.main()
