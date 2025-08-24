def create_link_token(user_id: str) -> dict:
    return {"link_token": "sandbox-link-pretend-token"}

def exchange_public_token(public_token: str) -> dict:
    return {"access_token": "access-sandbox-xyz", "item_id": "item-sandbox-abc"}
