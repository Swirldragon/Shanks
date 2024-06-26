import os
import json

env_file = "env.json"
if os.path.exists(env_file):
    with open(env_file) as f:
        env_vars = json.loads(f.read())
else:
    env_vars = dict(os.environ)

