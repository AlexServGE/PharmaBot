class ProcurementDatesBlock:

    def __init__(self, soup):
        procurement_dates_block = soup.find_all('div', 'col')[2].get_text(strip=True, separator="|").split("|") #[2] - procurement_dates_block
        pass
