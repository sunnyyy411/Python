import re
from email import message_from_string
from urllib.parse import urlparse
from collections import Counter

# Define suspicious keywords and domains
PHISHING_KEYWORDS = [
    "verify your account", "login now", "urgent action required", 
    "update your payment", "password reset", "account suspended"
]
SUSPICIOUS_DOMAINS = ["bit.ly", "tinyurl.com", "ow.ly", "t.co"]

# Function to check URLs in email content
def analyze_urls(email_content):
    urls = re.findall(r'https?://[^\s]+', email_content)
    suspicious_urls = []

    for url in urls:
        domain = urlparse(url).netloc
        if domain in SUSPICIOUS_DOMAINS:
            suspicious_urls.append(url)

    return suspicious_urls

# Function to check email headers
def analyze_headers(headers):
    suspicious_headers = {}
    if headers.get("From") and not headers["From"].endswith(("@legitdomain.com", "@trustedcompany.com")):
        suspicious_headers["From"] = headers["From"]
    if headers.get("Reply-To") and headers["Reply-To"] != headers.get("From", ""):
        suspicious_headers["Reply-To"] = headers["Reply-To"]
    return suspicious_headers

# Function to check phishing keywords
def analyze_content_for_keywords(email_content):
    keyword_count = Counter()
    for keyword in PHISHING_KEYWORDS:
        occurrences = email_content.lower().count(keyword)
        if occurrences > 0:
            keyword_count[keyword] += occurrences
    return keyword_count

# Main function to analyze an email
def analyze_email(email_raw):
    email_obj = message_from_string(email_raw)
    headers = dict(email_obj.items())
    email_body = email_obj.get_payload(decode=True).decode(errors="ignore") if email_obj.is_multipart() else email_obj.get_payload()

    # Analyze email content
    suspicious_urls = analyze_urls(email_body)
    suspicious_headers = analyze_headers(headers)
    keyword_analysis = analyze_content_for_keywords(email_body)

    # Generate report
    print("=== Phishing Email Analysis Report ===")
    if suspicious_headers:
        print("\nSuspicious Headers:")
        for key, value in suspicious_headers.items():
            print(f"{key}: {value}")
    else:
        print("\nNo suspicious headers detected.")

    if suspicious_urls:
        print("\nSuspicious URLs Found:")
        for url in suspicious_urls:
            print(url)
    else:
        print("\nNo suspicious URLs detected.")

    if keyword_analysis:
        print("\nPhishing Keywords Detected:")
        for keyword, count in keyword_analysis.items():
            print(f"{keyword}: {count}")
    else:
        print("\nNo phishing keywords detected.")

# Example usage
if __name__ == "__main__":
    # Example raw email string
    email_raw = """\
From: phisher@fake-domain.com
To: victim@domain.com
Subject: Urgent! Verify your account now

Dear user,

We noticed unusual activity in your account. Please verify your account immediately to avoid suspension: 
https://bit.ly/fake-url

Thank you,
Fake Support Team
"""
    analyze_email(email_raw)
