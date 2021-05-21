# bin/bash -e

set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place book celery_tasks job settings utils --exclude=__init__.py migrations
black book job utils --exclude=migrations
