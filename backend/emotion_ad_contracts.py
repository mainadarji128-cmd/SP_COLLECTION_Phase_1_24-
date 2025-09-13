def deploy_emotion_ad(mood, platform):
    ad_asset = {
        "mood": mood,
        "platform": platform,
        "biometric_signature": True,
        "override_watermark": True,
        "vault_routing": "Auto",
        "blockchain_hash": "0xA1B2C3D4"
    }
    return ad_asset
