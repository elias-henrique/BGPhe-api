from fastapi import FastAPI, HTTPException
from typing import Dict, Any
import requests

from bgphe import (
    extract_irr_data,
    extract_info,
    extract_network_info,
    extract_whois_data
)

app = FastAPI()

BASE_URL = 'https://bgp.he.net/'


def fetch_data_he(address: str = '') -> str:
    """Faz a requisição HTTP e retorna o texto HTML."""
    if address:
        if '/' in address:
            url = f'{BASE_URL}net/{address}'
        else:
            url = f'{BASE_URL}ip/{address}'
    else:
        url = BASE_URL

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(
            status_code=400, detail=f"Error fetching data from {url}: {e}")

    return response.text


def fetch_data(asn: int) -> Dict[str, Any]:
    """Faz a requisição HTTP e retorna os dados JSON."""
    urls = [
        f'https://api.bgpview.io/asn/{asn}',
        f'https://api.bgpview.io/asn/{asn}/peers'
    ]
    data = {'data': {}}

    try:
        for url in urls:
            response = requests.get(
                url, headers={'Accept': 'application/json'})
            response.raise_for_status()
            if 'peers' in url:
                data['data']['peers'] = response.json()['data']
            else:
                data['data']['as'] = response.json()['data']
    except requests.RequestException as e:
        raise HTTPException(
            status_code=400, detail=f"Error fetching data from {url}: {e}")

    return data


@app.get('/net')
def bgp(address: str = None, asn: int = None) -> Dict[str, Any]:
    try:
        if asn is not None:
            return fetch_data(asn)

        html_content = fetch_data_he(address)
        irr_data = extract_irr_data(html_content)
        net_info = extract_network_info(html_content)
        whois_data = extract_whois_data(html_content)

        return {
            'irr_data': irr_data,
            'net_info': net_info,
            'whois_data': whois_data
        }

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {e}")


@app.get('/')
def meu_ip() -> Dict[str, Any]:
    try:
        html_content = fetch_data_he()
        info = extract_info(html_content)

        return {'info': info}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
