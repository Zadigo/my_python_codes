from collections import namedtuple

__version__  = '0.1.0'

_AGENTS_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
]

class UserAgent(object):
    @property
    def get_user_agent(self, agent_index=0):
        return _AGENTS_LIST[agent_index]

    def get_user_agents(self):
        agents = namedtuple('Agents', ['headers'])
        return agents(_AGENTS_LIST)