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


def fetch_data(address: str = '') -> str:
    """Faz a requisição HTTP e retorna o texto HTML."""
    base_url = 'https://bgp.he.net/'
    if address:
        if '/' in address:
            url = f'{base_url}net/{address}'
        else:
            url = f'{base_url}ip/{address}'
    else:
        url = base_url

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))

    return response.text


@app.get('/net')
def bgp(address: str) -> Dict[str, Any]:
    try:
        html_content = fetch_data(address)
        irr_data = extract_irr_data(html_content)
        net_info = extract_network_info(html_content)
        whois_data = extract_whois_data(html_content)

        return {
            'irr_data': irr_data,
            'net_info': net_info,
            'whois_data': whois_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/')
def meu_ip() -> Dict[str, Any]:
    try:
        html_content = fetch_data()
        info = extract_info(html_content)

        return {
            'info': info
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
