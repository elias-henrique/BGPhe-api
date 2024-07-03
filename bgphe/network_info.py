from bs4 import BeautifulSoup
import json


def extract_network_info(html_content):
    """
    Extrai dados de tabelas BGP do conteúdo HTML fornecido.

    Parameters:
        html_content (str): O conteúdo HTML como uma string.

    Returns:
        str: Uma string JSON contendo os dados extraídos.
    """
    try:
        # Parse o conteúdo HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        netinfo_div = soup.find('div', id='netinfo')

        if not netinfo_div:
            return json.dumps({"error": "Div 'netinfo' não encontrada"}, ensure_ascii=False, indent=4)

        tables = netinfo_div.find_all('table')
        if not tables:
            return json.dumps({"error": "Nenhuma tabela encontrada na div 'netinfo'"}, ensure_ascii=False, indent=4)

        dados = []

        for table in tables:
            rows = table.find_all('tr')[1:]  # Ignorar o cabeçalho
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    as_link = cols[0].find('a')
                    ip_link = cols[1].find('a')
                    description = cols[2].text.strip() if len(cols) > 2 else ""

                    dados.append({
                        "AS": as_link.text.strip() if as_link else "N/A",
                        "IP": ip_link.text.strip() if ip_link else "N/A",
                        "Nome": description
                    })

        return dados

    except Exception as e:
        return {}
