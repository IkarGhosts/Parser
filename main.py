import requests
import re
from lxml.html import fromstring
from urllib.parse import urljoin
from urllib.request import urlopen


from settings import Settings


p_settings = Settings()


def parse_cruises():
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }

        r = requests.get(p_settings.URL, headers=headers, timeout=5)

        if r.status_code == 200:
            list_html = r.read().decode('utf-8')
            list_doc = fromstring(list_html)

            for elem in list_doc.cssselect(p_settings.ITEM_PATH):
                a = elem.cssselect('a')[0]
                href = a.get('href')
                url = urljoin(p_settings.URL, href)
                name = a.text

                details_html = urlopen(url).read().decode('utf-8')
                details_doc = fromstring(details_html)

                day_elem = details_doc.cssselect(p_settings.DAY_PATH)[0]
                day = day_elem.text_content()

                itinerary_elems = details_doc.cssselect(p_settings.TUR_PATH)
                itinerary = [i.strip() for i in [itinerary_elem.text for itinerary_elem in itinerary_elems]]

                itinerary_1 = []

                for item in itinerary:
                    itinerary_1.append(re.sub(r'\s+', ' ', item))

                data_elems = details_doc.cssselect(p_settings.DATA_PATH)
                data = [i.strip() for i in [data_elem.text for data_elem in data_elems]]

                ships_elems = details_doc.cssselect(p_settings.SHIP_PATH)
                ships = [i.strip() for i in [ships_elem.text for ships_elem in ships_elems]]

                coast_elems = details_doc.cssselect(p_settings.COAST_PATH)
                coast = [i.strip() for i in [coast_elem.text for coast_elem in coast_elems]]

                cruise = {'name': name, 'Days': day, 'itinerary': itinerary_1, 'dates': data, 'ship': ships,
                          'price': coast}

                print(cruise)

        if r.status_code == 404:
            print('Not pages')

    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))
    except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))
    except KeyboardInterrupt:
        print("Someone closed the program")


def main():

    parse_cruises()


if __name__ == '__main__':

    main()
