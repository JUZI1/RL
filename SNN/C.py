import torch
from torch import nn

example_id=1


inputs=[0,2,2,4,6,3,2,4,2,3,7]
hiddens=[0,20,20,40,50,30,20,50,20,30,50]
outputs=[0,1,1,1,2,1,1,2,1,1,1]
u_bounds=[0,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]

class Model(nn.Module):

    def __init__(self,n_obs,units, u_dim,u_bound):
        super(Model, self).__init__()
        self.dense=nn.ModuleList()
        self.dense.append(nn.Linear(n_obs, units))
        self.u_bound=u_bound
        self.out=nn.Linear(units,u_dim)


    def forward(self, x):
        x=torch.relu(self.h(x))
        x=torch.tanh(self.out(x))*self.u_bound
        return x

model=Model(inputs[example_id],hiddens[example_id],outputs[example_id],u_bounds[example_id])
model.load_state_dict(torch.load("cofe/SNN/model_{}.pth".format(example_id)))
print('w1:',model.state_dict()['dense.0.weight'])
print('b1:',model.state_dict()['dense.0.bias'])
print('----------------------------------------------------------------------------------------')
print('w2:',model.state_dict()['out.weight'])
print('b2:',model.state_dict()['out.bias'])
