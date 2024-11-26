import os
from crewai_tools import BaseTool
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import csv

class HtmlLinkParserTool(BaseTool):
    name: str = "HTML Link Parser"
    description: str = "Parses all the links in an HTML file"

    def _run(self) -> list:
        html_file_path = 'out\email.html'
        with open(html_file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            links = []
            for a in soup.find_all('a', href=True):
                href = a['href']
                parsed_url = urlparse(href)
                if 'safelinks.protection.outlook.com' in parsed_url.netloc:
                    query_params = parse_qs(parsed_url.query)
                    if 'url' in query_params:
                        links.append(query_params['url'][0])
                else:
                    links.append(href)
                    
        links_file_path = 'out\links.csv'
        with open(links_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Link'])
            for link in links:
                writer.writerow([link])
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