# Phishing Email Detection Script

This Python script is designed to detect phishing emails by analyzing their content, headers, and URLs. It uses common patterns and characteristics found in phishing emails to identify potential threats, helping SOC Analysts and cybersecurity enthusiasts secure their environments.

---

## Features

### 1. **URL Analysis**
- Extracts all URLs from the email content.
- Flags URLs from suspicious or shortened domains (e.g., `bit.ly`, `tinyurl.com`).

### 2. **Header Analysis**
- Examines the `From` and `Reply-To` headers to identify inconsistencies or spoofed email addresses.

### 3. **Keyword Detection**
- Searches for common phishing phrases (e.g., "verify your account", "urgent action required").

### 4. **Report Generation**
- Provides a detailed analysis report highlighting suspicious elements in the email.

---

## Prerequisites

- Python 3.6 or higher

### Required Libraries
No external libraries are required. The script uses the following built-in Python modules:
- `re`
- `email`
- `urllib.parse`
- `collections`

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/phishing-email-detection.git
   ```
2. Navigate to the project directory:
   ```bash
   cd phishing-email-detection
   ```
3. Run the script:
   ```bash
   python phishing_email_detection.py
   ```

---

## Usage

### Example Input
Provide a raw email string as input. Here is a sample raw email:

```python
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
```

### Running the Script
Save the raw email string in the script or pass it dynamically, and then execute the script to generate a detailed analysis report.

---

## Code Explanation

### 1. **Importing Required Libraries**
The script uses built-in Python libraries:
- `re`: For extracting URLs and matching patterns.
- `email`: For parsing raw email strings.
- `urllib.parse`: For extracting domain information from URLs.
- `collections`: For counting occurrences of phishing keywords.

### 2. **Defining Suspicious Patterns**
The script defines:
- `PHISHING_KEYWORDS`: A list of common phishing phrases.
- `SUSPICIOUS_DOMAINS`: A list of domains often used for phishing.

### 3. **Analyzing URLs**
The `analyze_urls` function:
- Extracts all URLs from the email content using regex.
- Flags URLs if their domains match entries in `SUSPICIOUS_DOMAINS`.

### 4. **Analyzing Headers**
The `analyze_headers` function:
- Checks the `From` header for untrusted domains.
- Compares the `Reply-To` header with the `From` header to identify mismatches.

### 5. **Keyword Analysis**
The `analyze_content_for_keywords` function:
- Counts occurrences of phishing keywords in the email body.
- Returns a dictionary of detected keywords and their frequencies.

### 6. **Generating the Report**
The `analyze_email` function:
- Combines results from the URL, header, and keyword analysis.
- Prints a detailed report of suspicious findings.

### 7. **Example Execution**
The `__main__` block demonstrates the script's usage with a sample raw email string.

---

## Output

The script generates a detailed phishing analysis report. For example:

```
=== Phishing Email Analysis Report ===

Suspicious Headers:
From: phisher@fake-domain.com

Suspicious URLs Found:
https://bit.ly/fake-url

Phishing Keywords Detected:
verify your account: 1
urgent action required: 1
```

---

## Future Enhancements

1. **Integration with Threat Feeds**
   - Use APIs like VirusTotal or AlienVault to verify URLs and domains.

2. **Attachment Analysis**
   - Extend the script to scan email attachments for malware.

3. **User Interface**
   - Add a GUI or web-based interface for easier usage.

4. **Log Management**
   - Store analysis reports for future reference or compliance.

---
