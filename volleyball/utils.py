import datetime

def get_age(year_of_birth):
    return datetime.datetime.now().year - year_of_birth

# class ImageParser:
#     def __init__(self):
#         response = requests.get('https://www.fivb.org/Vis2009/Images/GetImage.asmx?No=77966&type=Press&width=300&height=450&stretch=uniformtofill', stream=True)
#         if response.status_code == 200:
#             with open(IMAGES_PATH, 'wb') as f:
#                 for chunk in response:
#                     f.write(chunk)

# ImageParser()

# def get_ids(self):
    #     """
    #     Return the player's iDs
    #     """
    #     player_ids=[]
    #     links = self.profile_links
    #     for link in links:
    #         player_id = re.search(r'\?id\=(\d+)$', str(link))

    #         if player_id:
    #             player_ids.append(player_id.group(1))

    #     return player_ids
