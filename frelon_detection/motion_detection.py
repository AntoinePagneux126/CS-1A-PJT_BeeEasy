import numpy as np

class motionDetector:

    def __init__(self, shape=None, height=None, width=None, img=None):
        self.M = None
        self.shape = None
        self.initialised = False
        self.V = None
        self.N = 10
        self.one = None
        self.D = None
        self.delta = None

    def compute_frame(self, img):
        img = np.array(img, dtype=np.int32)
        if self.initialised:
            mask = self.M < img
            self.M += self.one  * mask
            self.M -= self.one *  np.logical_not(mask)
            self.delta = np.absolute(img - self.M)
            mask = self.V < self.N * self.delta
            self.V += self.one * mask
            self.V -= self.one * np.logical_not(mask)
            mask = self.delta > self.V
            self.D = mask * self.one
        else:
            self.M = img
            self.shape = self.M.shape
            self.V = np.zeros(self.shape, dtype=np.uint8)

            self.one = np.ones(self.shape, dtype=np.uint8)
            self.initialised = True
