-- models/staging/stg_website_sessions.sql

SELECT
    website_session_id,
    user_id,
    utm_source,
    utm_medium,
    utm_campaign,
    is_repeat_session,
    created_at AS website_session_created_at,
    CURRENT_TIMESTAMP AS loaded_at
FROM raw.website_sessions
