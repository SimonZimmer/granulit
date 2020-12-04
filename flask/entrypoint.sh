#!/bin/bash
set -e

# update database schema
flask db upgrade

exec "$@"

