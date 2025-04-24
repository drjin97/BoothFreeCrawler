import requests
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup

def get_download_url(item_id):
    """상품 페이지에서 다운로드 URL을 찾는 함수"""
    item_url = f"https://booth.pm/ko/items/{item_id}"
    response = requests.get(item_url, cookies=cookies, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 다운로드 버튼 찾기
        download_button = soup.find('a', {'class': 'download-button'})
        if download_button and 'href' in download_button.attrs:
            return download_button['href']
    
    return None

cookies = {
    '__cf_bm': 'YS4XRP_k.2HNY78EmbhstOIC5MVC1yXQFhYnL8xlkoU-1745224697-1.0.1.1-iNShbwwlHUwRIrzaPKCedFvSdZzZ65GRjUPCd0mnrsJAv3KAfrf3_WLFOAcDX7sXNyTFOvWfSNb7p2DqCiaUhWNI.hoTkS37jTgsyX1WcjY',
    'cf_clearance': 'gde8xR_y0qWmnkq_oj6f.0mWU6fMDM741vRCTXnMuTs-1745224698-1.2.1.1-.MqVhyzLSwWWKdXSqFDU6nLsooksHp2xXR3ZvuOhgZiAey9UGHmGy6ZJid1rOs9v9X3.ij6H_3f5hQQ1cjszMEv2FBLBUwKX87Lk_la4TtghmM_58GoHCl8y53f9nBzDUR0yIf3UqH3MfR6.gOrW8BMJ2CGcKmUm9osiSQnSuKENl32oqnRmCx3xX4D3InQ7H_p7GyLLKSYBCNGmPWWDyhw2ruxWNj49HjSxL4j8aber0_Rg8yoP1N__16IS2mbg8dOFIE5dC1si3LC2Ak0lb6FtOhyztoTKzAjME7n2nxjvJtMULpVhxJ1nm4YfKQD8nJhWHT8T.FpoyeR4jPM0tN1XFkbrkR_9AYSN5a2_agc',
    '_ga': 'GA1.1.282198046.1745224699',
    'receive_mail': '1',
    'recent_items': '6823382',
    '_ga_RWT2QKJLDC': 'GS1.1.1745224698.1.1.1745224750.8.0.0',
    '_plaza_session_nktz7u': 'jhDvxpsSFsHE%2Bcvpvd9VfiTdFQR4WmKpYJZAPMjQ7evcZho43TkhtVxzDrHb9uOsgcUh9%2FU5jVAFpRbUJdGTrCD8d4q6H2UZFkK1pygpMXwxu6PilFoz63bdzWLYNoaEuK0C8w%2Fa07bTP3Hoh13dbP4UzBdE%2B1B2flayPeNZnFpGFZSCaG3mZU3G%2FjA%2BbdyOJQP2PTNfqpPQIAUm2HP1lsK4o7ApW1kW8Dm6JEaid7hYHYyYj2iF%2BbPB%2BA8B6%2BPoW43oycZt9KIpExA4DqAuwWwi7gjO3ZjvApxNkAU16Ay4bMyasljjqF%2BEkNh%2BCL3j59n8ik5xHvOmNjIqiRhllqdmaHTZpxpFYQ9gv2vE%2BT1q%2B15ZKXfEUXofCDkXgbAT6e1JHvGe1WtNXctiKHB396FssHZktxgItTGSjcOKhij6xf93pTB40BkLddD5EvQSV6V6SVaEUZjst%2B%2FB6gasw6gRPT2gcCyyKFORfeQ0bsDp%2F88Z%2FwfgQ9WIAUCO1lvxnM8oNddVr3TWsEhKg1CLcP4CjPhjNZhdcyZWKGL8876GwcI%2FqG%2FTChhskhIoW9BmSe5fEoqO2IECNWM2ZMCOFK58K7GudIy500Bnvc6hbpY2Q2R9JyI5lAzxPwkGisMJLgKMDNYrr20KOdKcrZS8SpOqNWGESndNHd8uiD1nhnILt76%2FxGGsjlzYLQtmOeQs%2B5pLAIBRKlR0LDoseePQG0AQDsPMXVCQZ6NIyUkiy4pxzEWrsZPPgs3cLne1TzdcEqlumOsHdprK85c%3D--XaZ6tmCGHd9%2F3A3S--CCE796v7xAtw%2BPrX6mhdtg%3D%3D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://booth.pm/ko/items/6823382',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

# 현재 시간을 기반으로 디렉토리 생성
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = f"crawl_results_{timestamp}"
os.makedirs(output_dir, exist_ok=True)

# referer에서 상품 ID 추출
referer = headers.get('referer', '')
item_id = referer.split('/items/')[-1] if '/items/' in referer else None

# 다운로드 URL 찾기
download_url = get_download_url(item_id) if item_id else None

response = requests.get(download_url or 'https://booth.pm/downloadables/6541267', cookies=cookies, headers=headers)

# 메타데이터 저장
metadata = {
    'timestamp': timestamp,
    'item_id': item_id,
    'referer_url': referer,
    'download_url': download_url,
    'status_code': response.status_code,
    'headers': dict(response.headers),
    'cookies': cookies,
    'request_headers': headers
}

# 메타데이터를 JSON 파일로 저장
with open(f"{output_dir}/metadata.json", 'w', encoding='utf-8') as f:
    json.dump(metadata, f, ensure_ascii=False, indent=4)

# 응답 내용을 별도 파일로 저장
with open(f"{output_dir}/response_content.html", 'w', encoding='utf-8') as f:
    f.write(response.text)

# 쿠키 정보를 별도 파일로 저장
with open(f"{output_dir}/cookies.json", 'w', encoding='utf-8') as f:
    json.dump(cookies, f, ensure_ascii=False, indent=4)

# 헤더 정보를 별도 파일로 저장
with open(f"{output_dir}/headers.json", 'w', encoding='utf-8') as f:
    json.dump(headers, f, ensure_ascii=False, indent=4)

print(f"크롤링 결과가 {output_dir} 디렉토리에 저장되었습니다.")
print("저장된 파일:")
print(f"- {output_dir}/metadata.json: 메타데이터")
print(f"- {output_dir}/response_content.html: 응답 내용")
print(f"- {output_dir}/cookies.json: 쿠키 정보")
print(f"- {output_dir}/headers.json: 헤더 정보")