import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

class MoveParticleProcess(ctrl.Process):
    k=0
    def __init__(self, particle=ctrl.Particle(), pid=ctrl.PID()):
        super(MoveParticleProcess, self).__init__()
        self.particle = particle
        self.pid = pid

    def target(self, t):
        if t < 20. or t >= 35. :
            return np.asarray([0.])
        else:
            return np.array([1.])
    
    def sense(self, t):
        return self.particle.x
    def correct(self, error, dt):
        self.k=self.k+1
        print(error,self.k)
        return self.pid.update(error, dt)

    def actuate(self, u, dt):
        self.particle.add_force(u)
        self.particle.update(dt)


def runner(pid_params):
    process = MoveParticleProcess(particle=ctrl.Particle(x0=[0], v0=[0], inv_mass=1.), pid=ctrl.PID(**pid_params))
    result = process.loop(tsim=50, dt=0.2)
    e = np.sum(np.square(result['e']))
    return e

def run():

    pid_params = [
        #dict(kp=0.1, ki=0., kd=0.),
        dict(kp=7, ki=0.1, kd=11),
       # dict(kp=0, ki=0, kd=0),

    ]

    params = ctrl.tune_twiddle(params=dict(kp=0., ki=0., kd=0.), costfunction=runner, eps=0.001)
    pid_params.append(params)

    handles = []
    for idx, c in enumerate(pid_params):
        process = MoveParticleProcess(particle=ctrl.Particle(x0=[0], v0=[0], inv_mass=1.), pid=ctrl.PID(**c))
        result = process.loop(tsim=100, dt=0.1)

        if idx == 0:
            fh, = plt.step(result['t'], result['y'] ,label='target')    
            handles.append(fh)    

        xh, = plt.plot(result['t'], result['x'], label='pid kp {:.2f} kd {:.2f} ki {:.2f}'.format(c['kp'], c['kd'], c['ki']))
        handles.append(xh)
    
    plt.title('Particle trajectory')
    plt.legend(handles=handles, loc=1)
    plt.xlabel('Time $sec$')
    plt.ylabel('Position $m$')
    plt.show()
    
if __name__ == "__main__":
    run() 

