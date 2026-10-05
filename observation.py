class Observation:
    def __init__(self, target, observer,  filter_name, exposure):
        self.target = target
        self.observer = observer
        self.filter = filter_name
        self.exposure = exposure
    def summary_info(self):
        return f" target: {self.target}\n filter name: {self.filter}\n exposure: {self.exposure}\n Observer name: {self.observer}"

    def exposure_min(self):
        return self.exposure / 60


        
class Spectroscopic_observation(Observation):
    def __init__(self, target, observer,  filter_name, exposure, wavelength):
        super().__init__(target, observer,  filter_name, exposure)
        self.wavelength = wavelength
    def summary_info(self):
#         return f" target: {self.target}\n filter name: {self.filter}\n exposure: {self.exposure}\n Observer name: {self.observer} \n wavelength : {self.wavelength}"
        return super().summary_info() + f"\n wavelength : {self.wavelength}"


class Photometric_observation(Observation):
    def __init__(self, target, observer, filter_name, exposure,magnitude):
        super().__init__(target, observer, filter_name, exposure)
        self.magnitude = magnitude
    def summary_info(self):
        return super().summary_info() + f"\nmagnitude:{self.magnitude}"





