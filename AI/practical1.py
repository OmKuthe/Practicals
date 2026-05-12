"""
Experiment 1: Implementing AI Agents
Simple Reflex Agent and Model-Based Reflex Agent for Vacuum Cleaner World
"""

import random

# ============================================
# ENVIRONMENT
# ============================================

class VacuumEnvironment:
    def __init__(self):
        self.rooms = {'A': random.choice(['Dirty', 'Clean']),
                      'B': random.choice(['Dirty', 'Clean'])}
        self.agent_location = random.choice(['A', 'B'])
    
    def get_percept(self):
        return self.agent_location, self.rooms[self.agent_location]
    
    def execute_action(self, action):
        if action == 'Suck':
            self.rooms[self.agent_location] = 'Clean'
        elif action == 'Right':
            self.agent_location = 'B'
        elif action == 'Left':
            self.agent_location = 'A'
    
    def is_clean(self):
        return self.rooms['A'] == 'Clean' and self.rooms['B'] == 'Clean'


# ============================================
# SIMPLE REFLEX AGENT
# ============================================

class SimpleReflexAgent:
    def choose_action(self, percept):
        location, status = percept
        if status == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'Right'
        elif location == 'B':
            return 'Left'


# ============================================
# MODEL-BASED REFLEX AGENT
# ============================================

class ModelBasedAgent:
    def __init__(self):
        self.model = {'A': None, 'B': None}
    
    def choose_action(self, percept):
        location, status = percept
        self.model[location] = status
        
        if status == 'Dirty':
            return 'Suck'
        
        if self.model['A'] == 'Clean' and self.model['B'] == 'Clean':
            return 'NoOp'
        
        if location == 'A':
            return 'Right'
        else:
            return 'Left'


# ============================================
# SIMULATION
# ============================================

def run_simple_reflex():
    print("\n" + "=" * 50)
    print("SIMPLE REFLEX AGENT SIMULATION")
    print("=" * 50)
    
    env = VacuumEnvironment()
    agent = SimpleReflexAgent()
    
    print(f"\nInitial Environment: {env.rooms}")
    print(f"Agent starting at: {env.agent_location}\n")
    
    steps = 0
    while steps < 10:
        percept = env.get_percept()
        action = agent.choose_action(percept)
        env.execute_action(action)
        steps += 1
        print(f"Step {steps}: Action={action}, State={env.rooms}, Agent at {env.agent_location}")
        
        if env.is_clean() and steps >= 10:
            break
    
    print(f"\nFinal Environment: {env.rooms}")
    print(f"Both rooms clean: {env.is_clean()}")


def run_model_based():
    print("\n" + "=" * 50)
    print("MODEL-BASED REFLEX AGENT SIMULATION")
    print("=" * 50)
    
    env = VacuumEnvironment()
    agent = ModelBasedAgent()
    
    print(f"\nInitial Environment: {env.rooms}")
    print(f"Agent starting at: {env.agent_location}\n")
    
    steps = 0
    while steps < 10:
        percept = env.get_percept()
        action = agent.choose_action(percept)
        
        if action == 'NoOp':
            print(f"Step {steps + 1}: Agent knows both rooms are clean. Stopping.")
            break
        
        env.execute_action(action)
        steps += 1
        print(f"Step {steps}: Action={action}, State={env.rooms}, Agent at {env.agent_location}")
    
    print(f"\nFinal Environment: {env.rooms}")
    print(f"Agent Model: {agent.model}")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    run_simple_reflex()
    run_model_based()
    
    print("\n" + "=" * 50)
    print("CONCLUSION:")
    print("Model-Based Agent is more rational because it uses internal memory")
    print("to avoid unnecessary actions after both rooms are clean.")
    print("=" * 50)