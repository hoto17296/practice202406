#!/bin/bash -eu

WORKSPACE_DIR=$(cd $(dirname $0)/..; pwd)

cd ${WORKSPACE_DIR}/backend
poetry install --with dev

prisma generate --schema ${WORKSPACE_DIR}/postgres/schema.prisma

cd ${WORKSPACE_DIR}/frontend
npm install

bash -eu ${WORKSPACE_DIR}/generate-api-spec.sh