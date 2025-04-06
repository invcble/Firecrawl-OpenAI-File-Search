from firecrawl import FirecrawlApp
import os
import json
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()

# Initialize the Firecrawl app with your API key
api_key = os.environ.get('FIRECRAWL_API_KEY')
app = FirecrawlApp(api_key)

# Define the crawl parameters
target_url = 'https://derrick.com/'
crawl_params = {
    # 'allowedDomains': ['scrapeme.live'],
    'limit': 100,
    'scrapeOptions': {'formats': ['markdown']},
    'allowBackwardLinks': True
}

# Extract domain for naming the file
parsed_url = urlparse(target_url)
domain_for_filename = parsed_url.netloc.replace('.', '_')

# Start the crawl
try:
    crawl_status = app.crawl_url(
        target_url,
        params=crawl_params,
        poll_interval=30
    )
    print("Crawl completed successfully.")
    print(f"Credits used: {crawl_status['creditsUsed']}")
    print(f"Pages crawled: {len(crawl_status['data'])}")

    # Dump the entire crawl_status dict
    output_file = f"crawled_{domain_for_filename}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(crawl_status, f, ensure_ascii=False, indent=2)

    print(f"Full crawl data written to {output_file}")

except Exception as e:
    print(f"An error occurred during crawling: {str(e)}")
