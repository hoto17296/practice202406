#!/bin/bash -eu

CURRENT_DIR=$(cd $(dirname $0);pwd)

cd ${CURRENT_DIR}/backend
spec=$(python -c "import json; from main import app; print(json.dumps(app.openapi()))")

cd ${CURRENT_DIR}/frontend
echo ${spec} | bunx openapi-typescript -o src/api-spec.d.ts