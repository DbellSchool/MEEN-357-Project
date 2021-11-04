from define_rovers import define_rover_4
from define_experiment import experiment1
import matplotlib.pyplot as plt

experiment = experiment1()[0]
end_event = experiment1()[1]

# Set end conditions

#print(end_event)
end_event['max_distance'] = 995
end_event['max_time'] = 10000
end_event['min_velocity'] = 0.01
#print(end_event)

rover = define_rover_4()[0]
planet = define_rover_4()[1]

sim = sb.simulate_rover(rover,planet,experiment,end_event)

t = sim['telementry']['time']
x = sim['telementry']['position']
v = sim['telementry']['velocity']
p = sb.mechpower(v,rover)


f, axs = plt.subplots(3,1,figsize=(10,10))

plt.subplot(3,1,1)
plt.plot(t, x)
plt.xlabel('time [s]')
plt.ylabel('Motor position [m]')

plt.subplot(3,1,2)
plt.plot(t, v)
plt.xlabel('time [s]')
plt.ylabel('Motor velocity [m/s]')

plt.subplot(3,1,3)
plt.plot(t, p)
plt.xlabel('time [s]')
plt.ylabel('Motor Power [W]')

plt.show()
