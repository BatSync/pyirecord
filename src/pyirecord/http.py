def headers(access_token: str):
    """Set the headers to authenticate with our"""
    # Set the authorisation header to USER:[client system ID]:SECRET:[secret]
    return {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}
