from bs4 import BeautifulSoup


def extract_info(text):
    """
    Extracts information from the given HTML text.

    Parameters:
        text (str): The HTML content as a string.

    Returns:
        list: A list containing extracted IPs, AS numbers, and company names.
    """
    try:
        # Parse the HTML content
        soup = BeautifulSoup(text, 'html.parser')
        links = soup.find_all('a', class_='boldlink')

        if not links:
            return {"error": "No boldlink class links found"}

        extracted_data = []

        for link in links:
            ip_or_as = link.text.strip()
            parent = link.parent
            company_name = parent.text.split(
                '(')[-1].split(')')[0].strip() if '(' in parent.text else ""

            # Ensure unique entries are added to the list
            if ip_or_as and ip_or_as not in extracted_data:
                extracted_data.append(ip_or_as)
            elif company_name and company_name not in extracted_data:
                extracted_data.append(company_name)

        return extracted_data

    except Exception as e:
        return {}
