from bs4 import BeautifulSoup
import json


def extract_irr_data(text):
    """
    Extracts IRR data from the given HTML text.

    Parameters:
        text (str): The HTML content as a string.

    Returns:
        str: A JSON string containing the extracted IRR data.
    """
    try:
        # Parse the initial HTML content
        soup = BeautifulSoup(text, 'html.parser')
        div_irr = soup.find('div', id='irr')

        if not div_irr:
            return json.dumps({"error": "No IRR div found"}, ensure_ascii=False, indent=4)

        div_content = str(div_irr.find_all('div'))

        # Parse the inner div content
        soup = BeautifulSoup(div_content, 'html.parser')
        irr_boxes = soup.find_all('div', class_='irrbox')

        if not irr_boxes:
            return json.dumps({"error": "No IRR boxes found"}, ensure_ascii=False, indent=4)

        dados = []

        for box in irr_boxes:
            source = box.find('div', class_='irrsource').text.strip()
            data_span = box.find('span', class_='irrdata')
            links = data_span.find_all('a')
            route = links[0].get('title') if links else ''
            origin = links[1].get('title') if len(links) > 1 else ''
            member_of = links[2].get('title') if len(links) > 2 else ''

            geoidx = [geoidx.strip() for geoidx in data_span.text.split(
                'geoidx:') if geoidx.strip()][1:]
            if geoidx:
                geoidx[-1] = geoidx[-1].split('\n')[0]

            lines = data_span.text.split('\n')
            descr = next((line.split('descr:')[1].strip()
                         for line in lines if 'descr:' in line), '')
            notify = next((line.split('notify:')[1].strip(
            ) for line in lines if 'notify:' in line), '')
            mnt_by = next(
                (line.split('mnt-by:')[1].strip() for line in lines if 'mnt-by:' in line), '')
            changed = next((line.split('changed:')[1].strip(
            ) for line in lines if 'changed:' in line), '')
            last_modified = next((line.split(
                'last-modified:')[1].strip() for line in lines if 'last-modified:' in line), '')

            dados.append({
                'source': source,
                'route': route,
                'descr': descr,
                'origin': origin,
                'member-of': member_of,
                'notify': notify,
                'geoidx': geoidx,
                'mnt-by': mnt_by,
                'changed': changed,
                'last-modified': last_modified
            })

        return dados

    except Exception as e:
        return {}
