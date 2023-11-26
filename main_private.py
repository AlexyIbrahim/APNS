from aipkgs_notifications import apns
from aipkgs_notifications.enums import PushType
from aipkgs_notifications.payload import AlertPayload, Payload
from aipkgs_notifications.response import APNSResponse

if __name__ == '__main__':
    apns.initialize_apns(key_id='395YTGT8R8',
                         team_id='G2P4AFMWD6',
                         bundle_id='ai.kindly.Example',
                         is_prod=False,
                         p8_key_path='/Users/alexy/Documents/DataHub/Kindly/iOS/Keys/Push notification/AuthKey_395YTGT8R8.p8',
                         pem_file_path='/Users/alexy/Documents/DataHub/Kindly/iOS/APNS ai.kindly.Example/AuthKey.pem',
                         apns_priority=10,
                         apns_expiration=0)
    apns.config().verbose = True

    device_token = "80d008379d580b49cb40b8f8ff2b6652c089a64f8b2d40e3ade7bde783f215411363dd99844d0f379edffac87c4facd281f8031081db995dbc743ae8b01dea9c08c60547c59ae0a3d168b5ba8b3077cf"
    data = {'test': 'test'}
    title = "test title"

    alert_payload = AlertPayload(title=title, body=None)
    payload = Payload(alert=alert_payload, badge=None, data=data, content_available=True)

    response: APNSResponse = apns.push_raw(device_token=device_token, payload=payload, push_type=PushType.background, collapse_id=None)

