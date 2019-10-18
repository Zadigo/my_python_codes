from mailchimp import Stores

# mailchimp = MailChimp('us15', '03351c2235cfe08e38995805b658311c-us15')
# result = mailchimp
# result = mailchimp.get_list('9cb00a8368')
# result = mailchimp.get_stores()

list_id = '3335ddb952'
customer_id = '64e8396cda3a9b5e50fd'
store_id = '3b0c488c2c05b569914e'

stores = Stores('us15', '03351c2235cfe08e38995805b658311c-us15')
# result = stores.create('3335ddb952', 'Nawoka', 'https://nawoka.fr', 'contact.nawoka@gmail.com')
# result = stores.new_customer('3b0c488c2c05b569914e', 'pendenquejohn@gmail.com', 'John', 'Pendenque', 1, 13.75)
# print(result)
stores.new_order('zeirnzoeirnzo', store_id, {}, 178, 0, 178, [{'id': 'sdisnofi', 'product_id': 'sfoinsoi', 'quantity': 2, 'price': 74, 'discount': 0}])
