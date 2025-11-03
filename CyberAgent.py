from agent import Agent


class CyberAgent(Agent):
    def __init__(self, code_name, clearance_level, hacking):
        super().__init__(code_name, clearance_level)
        self.hacking = hacking

    def report(self):
        return f'Agent: {self.code_name} reporting , Clearance Level: {self._clearance_level}, Hacking: {self.hacking}'
