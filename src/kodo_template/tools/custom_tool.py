import os
from crewai_tools import BaseTool
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup

class HtmlLinkParserTool:
    def __init__(self):
        pass

    def parse_links(self, html_file_path):
        with open(html_file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            links = [a['href'] for a in soup.find_all('a', href=True)]
        return links

class EmlToHtmlTool(BaseTool):
    name: str = "Eml to Html"
    description: str = "Converts an eml file to html"

    def _run(self,email_file: str):
        with open(email_file, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
        
        # Extract the HTML part of the email
        html_content = None
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                html_content = part.get_payload(decode=True).decode(part.get_content_charset())
                break
        
        if html_content:
            html_file_path = 'out\email.html'
            with open(html_file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            return f"HTML content written to {html_file_path}"
        else:
            return "No HTML content found in the .eml file"