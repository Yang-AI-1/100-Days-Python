def get_smtp_address(email):
    """
    Determines the SMTP server address based on the email domain.
    """
    if "@" not in email:
        return None

    domain = email.split("@")[1].lower()

    smtp_servers = {
        "gmail.com": "smtp.gmail.com",
        "yahoo.com": "smtp.mail.yahoo.com",
        "hotmail.com": "smtp.live.com",
        "outlook.com": "smtp.office365.com",
        "live.com": "smtp.live.com"
    }

    return smtp_servers.get(domain)
