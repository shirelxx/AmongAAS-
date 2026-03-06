from fastapi import HTTPException

import config


def validate_prefix(data):
    if not data.db_name.startswith(config.PREFIX):
        raise HTTPException(status_code=400,
                            detail="db name has to start with the user prefix")


def validate_min_length(data):
    if len(data.username) < config.MIN_LEN:
        raise HTTPException(status_code=400,
                            detail="username length has to be above 3"
                            )
