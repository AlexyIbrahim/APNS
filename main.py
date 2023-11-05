from aipkgs_notifications import apns
from aipkgs_notifications.response import APNSResponse

if __name__ == '__main__':
    KEY_ID = ''
    TEAM_ID = ''
    BUNDLE_ID = 'com.test.app'
    IS_PROD = False
    P8_KEY_PATH = 'path/to/p8/key'
    PEM_FILE_PATH = 'path/to/pem/file'
    APNS_PRIORITY = 10
    APNS_EXPIRATION = 0

    assert KEY_ID, "KEY_ID is null or empty"
    assert TEAM_ID, "TEAM_ID is null or empty"
    assert BUNDLE_ID, "BUNDLE_ID is null or empty"

    apns.initialize_apns(key_id=KEY_ID,
                         team_id=TEAM_ID,
                         bundle_id=BUNDLE_ID,
                         is_prod=IS_PROD,
                         p8_key_path=P8_KEY_PATH,
                         pem_file_path=PEM_FILE_PATH,
                         apns_priority=APNS_PRIORITY,
                         apns_expiration=APNS_EXPIRATION,)
    apns.config().verbose = True

    device_token = ""
    data = {}
    title = "Hello World!"

    assert device_token, "device_token is null or empty"
    assert title, "title is null or empty"

    response: APNSResponse = apns.push(device_token=device_token, title=title, data=data, badge=None, push_type=apns.PushType.alert, collapse_id=None)
