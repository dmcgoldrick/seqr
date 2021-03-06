#!/usr/bin/env bash

set -x

env

su kibana -c "/usr/local/kibana-${KIBANA_VERSION}-linux-x86_64/bin/kibana \
    --host=0.0.0.0 \
    --port=${KIBANA_SERVICE_PORT} \
    --elasticsearch.url=http://${ELASTICSEARCH_SERVICE_HOSTNAME}:${ELASTICSEARCH_SERVICE_PORT}"