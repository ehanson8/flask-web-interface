import csv
import datetime
import json
import os

from asnake.client import ASnakeClient


class AsOperations:
    def __init__(self, client):
        """Create instance and import client as attribute."""
        self.client = client

    def get_all_records(self, endpoint):
        """Retrieve all records from a specified endpoint."""
        ids = self.client.get(f'{endpoint}?all_ids=true').json()
        return ids

    def get_record(self, uri):
        """Retrieve an individual record."""
        record = self.client.get(uri).json()
        return record

    def search(self, string, repo_id, rec_type, field='keyword'):
        """Search for a string across a particular record type."""
        endpoint = f'repositories/{repo_id}/search?'
        query = {'query': {'field': field, 'value': string,
                 'jsonmodel_type': 'field_query'}}
        params = {'aq': json.dumps(query), 'page_size': 100,
                  'type[]': rec_type}
        uris = []
        for result in self.client.get_paged(endpoint, params=params):
            uri = result['uri']
            uris.append(uri)
        return uris


def create_client(url):
    username = os.environ['USER']
    password = os.environ['PASSWORD']
    client = ASnakeClient(baseurl=url, username=username, password=password)
    as_ops = AsOperations(client)
    return as_ops


def create_csv(dict_list):
    dt = datetime.datetime.utcnow().isoformat(timespec='seconds')
    with open(f'report-{dt}.csv', 'w') as fp:
        header = list(dict_list[0].keys())
        f = csv.DictWriter(fp, fieldnames=header)
        f.writeheader()
        for d in dict_list:
            f.writerow(d)
    return fp.name


def create_rec_dict(rec_obj, client):
    rec_dict = {}
    rec_dict['uri'] = rec_obj['uri']
    rec_dict['title'] = rec_obj['title']
    rec_dict['id'] = concat_id(rec_obj)
    return rec_dict


def concat_id(rec_obj):
    """Retrieve URI and concatenated IDs for record."""
    ids = [rec_obj.get(f'id_{x}', '') for x in range(4)]
    return '-'.join(filter(None, ids))


def filter_note_type(rec_obj, note_type):
    """Filter notes by type."""
    return (n for n in rec_obj['notes'] if n.get('type') == note_type)


def get_values(rec_obj, field):
    field_values = []
    note_type_fields = ['abstract', 'accessrestrict', 'acqinfo',
                        'altformavail', 'appraisal', 'arrangement',
                        'bibliography', 'bioghist', 'custodhist', 'prefercite',
                        'processinfo', 'relatedmaterial', 'scopecontent',
                        'userestrict']
    if field in note_type_fields:
        notes = filter_note_type(rec_obj, field)
        for note in notes:
            for subnote in note.get('subnotes', []):
                if 'content' in subnote:
                    field_values.append(subnote['content'])
                elif 'definedlist' in subnote:
                    field_values.append(subnote['definedlist'])
    else:
        field_values = [rec_obj.get(field, '')]
    return field_values


def rec_report(url, repo_id, rec_type, field1, values_or_count1, field2,
               values_or_count2):
    as_ops = create_client(url)
    endpoint = f'/repositories/{repo_id}/{rec_type}'
    ids = as_ops.get_all_records(endpoint)
    ids = ids[:10]
    dict_list = []
    for id in ids:
        rec_obj = as_ops.get_record(f'{endpoint}/{id}')
        rec_dict = create_rec_dict(rec_obj, as_ops)
        values1 = get_values(rec_obj, field1)
        if values_or_count1 == 'count':
            rec_dict[field1] = len(values1)
        else:
            rec_dict[field1] = values1
        if field2 != '':
            values2 = get_values(rec_obj, field2)
            if values_or_count2 == 'count':
                rec_dict[field2] = len(values2)
            else:
                rec_dict[field2] = values2
        dict_list.append(rec_dict)
    file = create_csv(dict_list)
    return file


def search_report(url, repo_id, rec_type, field, search):
    as_ops = create_client(url)
    uris = as_ops.search(search, repo_id, rec_type, field)
    uris = uris[:10]
    dict_list = []
    for uri in uris:
        rec_obj = as_ops.get_record(uri)
        rec_dict = create_rec_dict(rec_obj, as_ops)
        values = get_values(rec_obj, field)
        rec_dict[field] = values
        dict_list.append(rec_dict)
    file = create_csv(dict_list)
    return file
