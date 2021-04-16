import os
from pprint import pprint
from urllib.parse import urljoin

import requests

BASE_API_URL: str = 'https://api.huntflow.ru'
TOKEN: str = os.environ.get('TOKEN')

ACCOUNT_ID: int = os.environ.get('ACCOUNT_ID')
VACANCY_ID: int = os.environ.get('VACANCY_ID', 2664194)
APPLICANT_ID: int = os.environ.get('APPLICANT_ID', 14260086)
NEW_STATUS_ID: int = os.environ.get('NEW_STATUS_ID', 113243)

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'User-Agent': 'LDSO_APP (developer@ldso.ru)',
}


def set_applicant_status(applicant_id: int, vacancy_id: int, to_status_id: int) -> dict:
    """Установим этап для кандидата"""
    payload = {
        "vacancy": vacancy_id,
        "status": to_status_id
    }

    api_url = f'/account/{ACCOUNT_ID}/applicants/{applicant_id}/vacancy'
    url = urljoin(BASE_API_URL, api_url)

    response = requests.put(url, data=payload, headers=headers)
    return response.json()


if __name__ == '__main__':
    pprint(set_applicant_status(
        APPLICANT_ID,
        VACANCY_ID,
        NEW_STATUS_ID
    ))
