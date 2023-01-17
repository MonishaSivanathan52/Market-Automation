from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import utils
from post.models import Post
from user.models import User


def send_email(request):
    constant = utils.send_grid_key
    sg = SendGridAPIClient(constant)
    subject = Post.subject
    content = Post.caption
    message = Mail(
        from_email=('monishasivanathan@gmail.com', 'Hello'),
        to_emails=User.email,
        subject=subject,
        html_content=content)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)