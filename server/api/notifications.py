import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests


# To post to Slack, create an app with a bot, and get its bot token: https://api.slack.com/apps 
# Bot tokens access scope: chat:write chat:write.customize
def post_msg_to_slack(text):
    print('📬️ Sending a Slack message')
    data = {
        "channel": os.getenv('SLACK_CHANNEL'),
        "text": text,
        # 'icon_emoji': ':date:',
        # 'username': 'DSRI GPU booker',
    }
    print(data)
    print(str(os.getenv('SLACK_BOT_TOKEN')))
    try:
        return requests.post(
            'https://slack.com/api/chat.postMessage', 
            json.dumps(data), 
            headers={
                'Authorization': 'Bearer ' + str(os.getenv('SLACK_BOT_TOKEN')),
                'Content-type': 'application/json; charset=utf-8'
            }
        ).json()
    except Exception as e:
        return e


## Send an email with UM smtp server (require VPN connection)
# https://kb.icts.maastrichtuniversity.nl/display/ISM/E-mail+-+Universal+UM+email+server+names
def send_email(msg, to):
    fromaddr = 'vincent.emonet@maastrichtuniversity.nl'
    # Service with 100 emails/day free: https://sendgrid.com/
    
    # smtp_user = os.getenv('SMTP_USER', 'Vincent.Emonet')
    # password = os.getenv('SMTP_PASSWORD', 'password')
    toaddrs  = [to]

    print(f"📬️ Sending an email from {fromaddr} to {toaddrs}")

    # Create message container - the correct MIME type is multipart/alternative.
    email = MIMEMultipart('alternative')
    email['Subject'] = "📀 DSRI GPU bookings"
    email['From'] = fromaddr
    email['To'] = ', '.join(toaddrs)

    # Create the body of the message (a plain-text and an HTML version).
    text = msg
    html = f"""\
    <html>
    <head>
        <style></style>
    </head>
    <body>
        {msg}
    </body>
    </html>
    """
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    # Attach parts into message container.
    msg.attach(part1)
    msg.attach(part2)

    try :
        server = smtplib.SMTP(host='smtp.maastrichtuniversity.nl', port=25)
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server = smtplib.SMTP()
        # server.connect(server_smtp, port_smtp)
        # server.set_debuglevel(True)
        # server.starttls()
        # server.ehlo()
        # server.login(smtp_user, password)
        # server.sendmail(fromaddr, toaddrs, BODY.encode('utf-8'))
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()
    except Exception as e:
        print(e)

