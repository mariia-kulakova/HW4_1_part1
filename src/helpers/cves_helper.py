from json import loads

CVES_FILENAME = 'known_exploited_vulnerabilities.json'

def retrieve_cves():
    with open(CVES_FILENAME, 'r') as file:
        cves = loads(file.read())

        return cves.get('vulnerabilities', {})
