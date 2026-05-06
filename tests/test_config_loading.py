import yaml


def test_config_yaml_exists():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    assert isinstance(config, dict)
