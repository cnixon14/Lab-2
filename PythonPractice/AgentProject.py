class Agent:

    def __init__(self, name, environment, actuators, sensors, performance_metrics):
        self.name = name
        self.environment = environment
        self.actuators = actuators
        self.sensors = sensors
        self.performance_metrics = performance_metrics

    def printInfo(self):
        print('Name: %s' % self.name)
        print('\tEnvironment: %s' % self.environment)
        print('\tActuators: %s' % self.actuators)
        print('\tSensors: %s' % self.sensors)
        print('\tPerformance Metrics: %s' % self.performance_metrics)


a = Agent('Me', 'Real world', ['hands', 'feet', 'joints', 'muscles'],
          ['eyes', 'nose', 'eyes'], ['heartrate', 'IQ', 'EQ'])
butter_passing_robot = Agent('Butter passing robot', 'Table', ['hooks', 'hands', 'speaker'], ['camera', 'microphone'],
                             ['number of people on table with butter'])
screaming_roomba = Agent('Screaming Roomba', 'Dirty Floor', ['wheels', 'vacuum', 'pressure plate', 'speaker'],
                         ['camera', 'bump sensor'], ['Number of walls hit', 'Percent of floor clean'])

enemy_entity_ghost = Agent('Ghost', 'Virtual Environment', ['Translation X-Axis, Translation Y-Axis', 'HP'], ['Pathfinding Grid', 'Collision Detection', 'Hit Box'], ['Distance to player', 'HP Gague'])
siri = Agent('Siri', 'Digital Space', ['speaker, wifi router'], ['microphone'], ['Wifi connectivity', 'voice detection'])
slap_bot = Agent('Slappy', 'table', ['Arm', 'Servo', 'Camera'], ['Facial Recognition', 'pressure sensor'], ['faces slapped'])
butter_passing_robot.printInfo()
screaming_roomba.printInfo()
enemy_entity_ghost.printInfo()
siri.printInfo()
slap_bot.printInfo()



