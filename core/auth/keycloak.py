from fastapi_keycloak import FastAPIKeycloak
from core.config import config

idp = FastAPIKeycloak(
    server_url=config.IDP_SERVER_URL,
    client_id=config.IDP_CLIENT_ID,
    client_secret=config.IDP_CLIENT_SECRET,
    admin_client_secret=config.IDP_ADMIN_CLIENT_SECRET,
    realm=config.IDP_REALM,
    callback_uri=config.CALLBACK_URI
)