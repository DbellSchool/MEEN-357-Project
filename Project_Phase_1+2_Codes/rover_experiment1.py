from define_rovers import define_rover_4
from define_experiment import experiment1
import matplotlib.pyplot as plt
import subfunctions as sb
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
#p = v


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


#gets battery energy
j = sb.battenergy(t, v, rover)

print("Final Table:\n")
print("completion_time:",t[-1]) # last index
print("distance_traveled:",v[-1]-v[0])
print( "max_velocity:",max(v))
print( "average_velocity:",sum(v)/len(v))
print("battery_energy:",j)
print("batt_energy_per_distance:",j/(x[-1]-x[0]))




print("\n\nBattenergy = ", j)