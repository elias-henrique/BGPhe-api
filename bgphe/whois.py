from bs4 import BeautifulSoup
import json
import re


def extract_whois_data(text):
    """
    Extrai dados de um bloco de texto WHOIS HTML e os converte em um JSON formatado.

    Parameters:
        text (str): O conteúdo HTML como uma string.

    Returns:
        str: Uma string JSON contendo os dados extraídos.
    """
    try:
        # Parse o conteúdo HTML
        soup = BeautifulSoup(text, 'html.parser')
        whois_div = soup.find('div', id='whois')

        if not whois_div:
            return json.dumps({"error": "Div 'whois' não encontrada"}, ensure_ascii=False, indent=4)

        pre_content = str(whois_div.find_all('pre')[0])
        data = {}

        patterns = {
            "NetRange": r"NetRange:\s*(.+)",
            "CIDR": r"CIDR:\s*(.+)",
            "NetName": r"NetName:\s*(.+)",
            "NetHandle": r"NetHandle:\s*(.+)",
            "Parent": r"Parent:\s*(.+)",
            "NetType": r"NetType:\s*(.+)",
            "OriginAS": r"OriginAS:\s*(.+)",
            "Organization": r"Organization:\s*(.+)",
            "RegDate": r"RegDate:\s*(.+)",
            "Updated": r"Updated:\s*(.+)",
            "Ref": r"Ref:\s*(.+)",
            "OrgName": r"OrgName:\s*(.+)",
            "OrgId": r"OrgId:\s*(.+)",
            "Address": r"Address:\s*(.+)",
            "City": r"City:\s*(.+)",
            "StateProv": r"StateProv:\s*(.+)",
            "PostalCode": r"PostalCode:\s*(.+)",
            "Country": r"Country:\s*(.+)",
            "OrgAbuseHandle": r"OrgAbuseHandle:\s*(.+)",
            "OrgAbuseName": r"OrgAbuseName:\s*(.+)",
            "OrgAbusePhone": r"OrgAbusePhone:\s*(.+)",
            "OrgAbuseEmail": r"OrgAbuseEmail:\s*(.+)",
            "OrgAbuseRef": r"OrgAbuseRef:\s*(.+)",
            "OrgTechHandle": r"OrgTechHandle:\s*(.+)",
            "OrgTechName": r"OrgTechName:\s*(.+)",
            "OrgTechPhone": r"OrgTechPhone:\s*(.+)",
            "OrgTechEmail": r"OrgTechEmail:\s*(.+)",
            "OrgTechRef": r"OrgTechRef:\s*(.+)",
            "inetnum": r"inetnum:\s*(.+)",
            "aut-num": r"aut-num:\s*(.+)",
            "abuse-c": r"abuse-c:\s*(.+)",
            "owner": r"owner:\s*(.+)",
            "ownerid": r"ownerid:\s*(.+)",
            "responsible": r"responsible:\s*(.+)",
            "owner-c": r"owner-c:\s*(.+)",
            "tech-c": r"tech-c:\s*(.+)",
            "inetrev": r"inetrev:\s*(.+)",
            "nserver": r"nserver:\s*(.+)",
            "nsstat": r"nsstat:\s*(.+)",
            "nslastaa": r"nslastaa:\s*(.+)",
            "created": r"created:\s*(.+)",
            "changed": r"changed:\s*(.+)",
            "nic-hdl-br": r"nic-hdl-br:\s*(.+)",
            "person": r"person:\s*(.+)"
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, pre_content, re.MULTILINE)
            if match:
                data[key] = match.group(1).strip()

        multivalued_fields = ["inetrev", "nserver", "nsstat", "nslastaa"]
        for field in multivalued_fields:
            matches = re.findall(patterns[field], pre_content, re.MULTILINE)
            if matches:
                data[field] = list(set(matches))

        return data

    except Exception as e:
        return {}
