#     Copyright 2019 Jonathan Niven
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
import jsonschema
import json
import yaml
from pathlib import Path


def test_secret_schema_template():
    """Checks that the secrets template adheres to schema"""
    template = Path('secrets_template.yml')
    schema = Path('schemas/secrets_schema.json')
    with template.open() as f:
        template_struct = yaml.safe_load(f)
    with schema.open() as f:
        schema_struct = json.load(f)
    jsonschema.validate(template_struct, schema_struct)
