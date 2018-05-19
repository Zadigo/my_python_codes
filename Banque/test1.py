# a='get_aurelie_from_user_model'

# import re
# a=re.search(r'(get)\_([a-zA-Z]+)\_from\_(\w.*)',a)
# qdict=dict(caller=a.group(1),criteria=a.group(2),getter=a.group(3),where='a')

# print(qdict)

def t(request, method, model, **criteria):
    # if not isinstance(request,'a'):
    #     pass
    s=''
    if method=='get':
        s+='SELECT ' + model + ' FROM'
        if criteria:
            if 'where' in criteria:
                if isinstance(criteria.get('where'), list):
                    s+='SELECT ' + model + ' FROM' + 'WHERE' + criteria.get('where')

    
    print(s)

t('a','get','a',p='p')
