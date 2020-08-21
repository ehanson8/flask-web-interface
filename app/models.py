import os
import requests


def create_dict_report(url, repo_id, rec_type, field):
    user = os.environ['USER']
    password = os.environ['PASSWORD']
    auth = requests.post(
        f'{url}/users/{user}/login?password={password}'
    ).json()
    headers = {
        'X-ArchivesSpace-Session': auth['session'],
        'Content_Type': 'application/json'
    }
    endpoint = f'/repositories/{repo_id}/{rec_type}'
    ids = requests.get(f'{url}{endpoint}?all_ids=true', headers=headers).json()
    ids = ids[:10]
    report_dict = {}
    for id in ids:
        rec_obj = requests.get(f'{url}{endpoint}/{id}', headers=headers).json()
        report_dict[rec_obj['uri']] = rec_obj.get(field, '')
    return report_dict
