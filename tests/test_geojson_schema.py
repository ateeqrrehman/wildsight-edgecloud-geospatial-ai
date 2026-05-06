import json
from pathlib import Path


def test_geojson_schema_has_required_contract_fields():
    schema_path = Path('schemas/geojson_feature.schema.json')
    schema = json.loads(schema_path.read_text())

    assert schema['type'] == 'object'
    assert set(schema['required']) == {'type', 'geometry', 'properties'}
    assert schema['properties']['type']['enum'] == ['Feature']
    assert 'geometry' in schema['properties']
    assert 'properties' in schema['properties']
