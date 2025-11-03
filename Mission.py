from agent import Agent


class Mission:
    def __init__(self, mission_name, target_location):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = None

    def assign(self, agent: Agent):
        self.assigned_agent = agent

    def brief(self):
        return f'Mission: {self.mission_name}, Target: {self.target_location}, Agent: {self.assigned_agent.code_name}'


