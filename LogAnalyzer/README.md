# LogAnalyzer

`LogAnalyzer` is a Python script for analyzing web server log files. It extracts useful information like the number of requests made by each IP address.

## Features
- Parses web server log files in a common log format.
- Counts the number of requests made by each IP address.
- Provides a simple report for quick analysis.

## Installation

1. Clone this repository or copy the script to your local machine.
2. Ensure Python 3 is installed on your system.

## Usage

### 1. Prepare Your Log File
Ensure your log file is in the format:

192.168.1.1 - - [01/Jan/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024 192.168.1.2 - - [01/Jan/2025:10:01:00 +0000] "POST /login HTTP/1.1" 302 512 192.168.1.1 - - [01/Jan/2025:10:02:00 +0000] "GET /about.html HTTP/1.1" 200 2048


### 2. Run the Script

### 3. Example Output
For the log file:

192.168.1.1 - - [01/Jan/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024

192.168.1.2 - - [01/Jan/2025:10:01:00 +0000] "POST /login HTTP/1.1" 302 512

192.168.1.1 - - [01/Jan/2025:10:02:00 +0000] "GET /about.html HTTP/1.1" 200 2048

192.168.1.3 - - [01/Jan/2025:10:03:00 +0000] "GET /contact.html HTTP/1.1" 404 256

192.168.1.2 - - [01/Jan/2025:10:04:00 +0000] "GET /dashboard HTTP/1.1" 200 4096

192.168.1.1 - - [01/Jan/2025:10:05:00 +0000] "GET /index.html HTTP/1.1" 200 1024

The output will be:

Requests per IP:

192.168.1.1: 3

192.168.1.2: 2

192.168.1.3: 1

How It Works:

The script reads the log file line by line.
It uses a regular expression to extract:
IP Address
Request Method
Requested URL
Status Code
Response Size
It counts the number of requests for each IP address.
The report is printed to the console.


Customization

You can modify the process_line method to extract additional information like:

Status codes distribution.
Requests per URL.
Requests per time period.
