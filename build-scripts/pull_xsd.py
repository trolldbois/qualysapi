
def pull_xsd(server='qualysapi.qualys.com'):
    import requests
    import os
    todos = [('webapp.xsd', f'https://{server}/qps/xsd/3.0/was/webapp.xsd'),
             ('webappauthrecord.xsd', f'https://{server}/qps/xsd/3.0/was/webappauthrecord.xsd'),
             ('scan.xsd', f'https://{server}/qps/xsd/3.0/was/scan.xsd'),
             ('schedule.xsd', f'https://{server}/qps/xsd/3.0/was/schedule.xsd'),
             ('report.xsd', f'https://{server}/qps/xsd/3.0/was/report.xsd'),
             ('optionprofile.xsd', f'https://{server}/qps/xsd/3.0/was/optionprofile.xsd'),
             ('finding.xsd', f'https://{server}/qps/xsd/3.0/was/finding.xsd'),
             ]
    def dl_and_save(filename, url):
        response = requests.get(url, stream=True)
        # Throw an error for bad status codes
        response.raise_for_status()
        with open(filename, 'wb') as handle:
            for block in response.iter_content(1024):
                handle.write(block)
        return filename
    for fname, url in todos:
        dl_and_save(os.path.sep.join(['qualysapi', 'gen', fname]), url)
        print(f"Downloaded {fname}")
    return


if __name__ == '__main__':
    pull_xsd()