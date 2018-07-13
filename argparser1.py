# from argparse import ArgumentParser

# def _parse_args():
#     args = ArgumentParser(
#         description='Create a Luhn number'
#     )
#     args.add_argument('number', help='Enter a 7 digit number', type=int)
#     args.add_argument('-e', '--encrypt', help='Encrypt nuner using 5')
#     args.parse_args()
#     return args

# def _create_nubers():
#     pass

# def Main():
#     arg = _parse_args()
#     if arg:
#         print('True')
#         print(arg._get_args())

# if __name__ == '__main__':
#     Main()

COMPANY_INFORMATION = {
    'company_name':'',
    'company_address':'',
    'website':'',
    'herbergeur': 'OVH',
    'herbergeur_address': '',
    'instagram':'',
    'twitter':'',
    'linkedin':'',
    'current_year':'',
    'legal': {
        'cnil': ''
    }
}

API_KEYS = {
    'GOOGLE_MAPS':'',
    'GOOGLE_SHEET':'',
    'LA_POSTE':'',
    'TWITTER': {
        'SECRET_KEY':'',
        'CONSUMER_KEY':'',
    },
    'facebook':'',
}

def get_api_key(api):
    try:
        return API_KEYS[api]
    except KeyError:
        return None

def get_company_info(**kwargs):
    if kwargs:
        for k, v in kwargs.items():
            COMPANY_INFORMATION[k] = v
    return COMPANY_INFORMATION

print(get_company_info(LA_POSTE='LA_POSTE'))
