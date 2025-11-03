class Agent:
    total_agents = 0
    def __init__(self, code_name, clearance_level):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.total_agents += 1




    def report(self):
        return f'Agent: {self.code_name} reporting , Clearance Level: {self._clearance_level}'

    def get_clearance_level(self):
        return self._clearance_level

    def set_clearance_level(self, level: int):
        if 1 < level < 10:
            self._clearance_level = level
            return level

    @staticmethod
    def get_total_agents():
        return Agent.total_agents


