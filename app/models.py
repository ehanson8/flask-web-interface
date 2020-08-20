from sickle import Sickle
import xml.etree.ElementTree as ET

namespace = {"dc": "http://purl.org/dc/elements/1.1/"}


def create_dict_report(url, format, set, field):
    client = Sickle(url)
    params = {'metadataPrefix': format, 'set': set}
    ids = client.ListIdentifiers(**params)
    title_dict = {}
    for id in ids:
        record = client.GetRecord(
            identifier=id.identifier,
            metadataPrefix=format
        )
        parsed_record = ET.fromstring(record.raw)
        title = parsed_record.find(f".//dc:{field}", namespace)
        if title is not None:
            title_dict[id.identifier] = title.text
    return title_dict
