from.neuron import SpikingNeuron

import numpy as np

class izk_neuron(SpikingNeuron):
    def __init__(self,id, activation_func, coding_rule, act_init =(-75,-4), parameters = np.array([0.02,0.2,-65,6]),
                 *args, **kwargs):
        SpikingNeuron.__init__(self, id, activation_func, coding_rule, act_init , parameters)

    def _set_type(self):
        pass



