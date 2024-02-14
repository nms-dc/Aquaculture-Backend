#!/bin/bash
set -e

RESTORE_CONFIG="
shared_buffers = 128MB
work_mem = 256MB
maintenance_work_mem = 256MB
autovacuum = off
fsync = off
"

cd /docker-entrypoint-initdb.d/
# Switch to the postgres user context
su - postgres -c "cp ${PGDATA}/postgresql.conf ${PGDATA}/postgresql.conf-original"


if [ ! $(ls -t | grep -E 'dump$' | head -1) ]; then
    echo "No dump files found. Exiting."
    exit 1
else
    echo "Tweaking postgres config for dump restore. Using: ${RESTORE_CONFIG}"
    cp ${PGDATA}/postgresql.conf ${PGDATA}/postgresql.conf-original
    echo "${RESTORE_CONFIG}" >> ${PGDATA}/postgresql.conf
    echo "Restarting the cluster"
    # pg_ctl -D "$PGDATA" -m fast -w restart

    if [ "$(ls -t | grep -E 'dump$' | wc -l)" -gt "1" ]; then
        echo "Found multiple files. Using the newest one."
    fi

    DUMP_FILE=$(ls -t | grep -E 'dump$' | head -1)
    if [ -d ${DUMP_FILE} ]; then
        RESTORE_START=${SECONDS}
        echo "Restoring ${DUMP_FILE} using directory format..."
        pg_restore -e -Fd --no-owner --clean --create --no-acl -j ${POSTGRES_RESTORE_JOBS:-2} -U ${POSTGRES_USER} -d postgres ${DUMP_FILE}
        echo "Finished restoring. Took $(( SECONDS - RESTORE_START )) seconds."
    else
        RESTORE_START=${SECONDS}
        echo "Restoring ${DUMP_FILE} using custom format..."
        pg_restore -e -Fc --no-owner --clean --create --no-acl -j ${POSTGRES_RESTORE_JOBS:-2} -U ${POSTGRES_USER} -d postgres ${DUMP_FILE}
        echo "Finished restoring. Took $(( SECONDS - RESTORE_START )) seconds."
    fi

    mv ${PGDATA}/postgresql.conf-original ${PGDATA}/postgresql.conf
    echo "Restored pre-restore config. Exiting."
    exit 0  # Exit with a success code
fi
