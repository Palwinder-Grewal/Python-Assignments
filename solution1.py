# 1 Fetch url from dict
# 2 Add new entity in flow_3
# 3 Update url in all flows
# 4 Delete the entity in flow_1


from flows import *

all_flows = [flow_1, flow_2, flow_3]

def del_entity(flow, entity):
    if entity == 0 or entity == 1:
        del flow['entities'][entity]
    else:
        print('Enter correct index')


def fetch_url(flow):
    return (flow.get('api_data').get('url'))

def fetch_all_url():
    all_urls = []
    for i in all_flows:
        all_urls.append(i.get('api_data').get('url'))
    return all_urls


def add_entity(flow, new_entity):
    flow.get('entities').append(new_entity)


def update_url(new_url):  # upates url in all flows
    for i in all_flows:
        i["api_data"]["url"] = new_url


print(fetch_url(flow_2))

print(fetch_all_url())

add_entity(flow_3, {'new_key': 'new_value'})

update_url('new_url_updated')

del_entity(flow_1, 0)

updated_flows = [flow_1, flow_2, flow_3]
print('\n\n', updated_flows)
