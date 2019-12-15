
import numpy as np

class PID(object):

    def __init__(self, kp=0.5, ki=0.0, kd=0.01):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.first = True
    def update(self, error, dt):
        if self.first:
            self.lastError = np.copy(error)
            self.sumError = np.zeros(error.shape)
            self.first = False

        derr = (error - self.lastError) / dt

        self.sumError += error * dt
        self.lastError[:] = error

        u = self.kp * error + self.kd * derr + self.ki * self.sumError

        return u