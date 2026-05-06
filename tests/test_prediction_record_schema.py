import json
from pathlib import Path


def test_prediction_record_schema_has_required_contract_fields():
    schema_path = Path('schemas/prediction_record.schema.json')
    schema = json.loads(schema_path.read_text())

    assert schema['type'] == 'object'
    assert set(schema['required']) == {'image_id', 'source', 'predictions'}
    assert 'predictions' in schema['properties']
    assert schema['properties']['predictions']['type'] == 'array'
