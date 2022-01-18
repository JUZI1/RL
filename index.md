# Benchmark Example

Now we will show our 10 examples below.
## C<sub>3</sub>:&nbsp;&nbsp;Cartpole system.
The equation of motion for cartpole system is

<div align=center>
<img src="https://latex.codecogs.com/svg.image?\bg_white&space;\begin{bmatrix}&space;&space;&space;&space;&space;&space;&space;&space;\ddot{x}\\&space;&space;&space;&space;&space;&space;&space;&space;\ddot{\theta}&space;&space;&space;&space;\end{bmatrix}&space;&space;&space;&space;=&space;&space;&space;&space;\begin{bmatrix}&space;&space;&space;&space;&space;&space;&space;&space;\frac{u&plus;m_p&space;sin\theta(l\dot\theta^2&space;-gcos(\theta))}{m_c&plus;m_p&space;sin^2(\theta)}&space;\\&space;\frac{ucos(\theta)&plus;m_pl\dot{\theta}^2cos\theta&space;sin\theta&space;-(m_c&plus;m_p)gsin\theta}{l(m_c&plus;m_psin^2\theta)}&space;&space;&space;&space;\end{bmatrix}" title="\bg_white \begin{bmatrix} \ddot{x}\\ \ddot{\theta} \end{bmatrix} = \begin{bmatrix} \frac{u+m_p sin\theta(l\dot\theta^2 -gcos(\theta))}{m_c+m_p sin^2(\theta)} \\ \frac{ucos(\theta)+m_pl\dot{\theta}^2cos\theta sin\theta -(m_c+m_p)gsin\theta}{l(m_c+m_psin^2\theta)} \end{bmatrix}" />
</div>

with the constants set as
<div align=center>
<img src="https://latex.codecogs.com/svg.image?m_c=1,m_p=1,m_p=1,g=1,l=1" title="m_c=1,m_p=1,m_p=1,g=1,l=1" />.
</div>
Define the state space as
<div align=center>
<img src="https://latex.codecogs.com/svg.image?\mathbf&space;x&space;=[x,\theta,\dot{x},\dot{\theta}]&space;" title="\mathbf x =[x,\theta,\dot{x},\dot{\theta}] " />.
</div>
where
<div align=center>
<img src="https://latex.codecogs.com/svg.image?\bg_white&space;\Psi=\{\mathbf&space;x&space;\in&space;\mathbb{R}^4&space;\,|\,&space;[-1.3,-1.3,-1.3,-1.3]^T\leq\mathbf&space;x&space;\leq&space;[1.3,1.3,1.3,1.3]^T\}" title="\bg_white \Psi=\{\mathbf x \in \mathbb{R}^4 \,|\, [-1.3,-1.3,-1.3,-1.3]^T\leq\mathbf x \leq [1.3,1.3,1.3,1.3]^T\}" />,
</div>

<div align=center>
<img src="https://latex.codecogs.com/svg.image?\bg_white&space;X_0=\{\mathbf&space;x\in&space;\mathbb{R}^4&space;\,|\,&space;&space;0.0\leq&space;\left\|&space;\mathbf&space;x\right\|_2\leq&space;0.7\}" title="\bg_white X_0=\{\mathbf x\in \mathbb{R}^4 \,|\, 0.0\leq \left\| \mathbf x\right\|_2\leq 0.7\}" />,
 </div>
 
<div align=center>
<img src="https://latex.codecogs.com/svg.image?\bg_white&space;X_u=\{\mathbf&space;x\in&space;\mathbb{R}^4&space;\,|\,&space;&space;1.0\leq&space;||\mathbf&space;x||_2\leq&space;1.3\}" title="\bg_white X_u=\{\mathbf x\in \mathbb{R}^4 \,|\, 1.0\leq ||\mathbf x||_2\leq 1.3\}" />,
</div>
 
<div align=center>
<img src="https://latex.codecogs.com/svg.image?\bg_white&space;X_g=\{\mathbf&space;x\in&space;\mathbb{R}^4&space;\,|\,&space;&space;0.0\leq&space;||\mathbf&space;x||_2\leq&space;0.1\}" title="\bg_white X_g=\{\mathbf x\in \mathbb{R}^4 \,|\, 0.0\leq ||\mathbf x||_2\leq 0.1\}" />.
</div>



Our results are as follows:

<div align=center>
<img src="https://latex.codecogs.com/svg.image?\bg_white&space;p(\mathbf&space;x)=-1.4954x_{1}-0.6050x_{2}-2.6590x_{3}-1.2333x_{4}-0.1398x_{1}^2&plus;0.0463x_{1}x_{2}&plus;1.0553x_{1}x_{3}&plus;0.0182x_{1}x_{4}&plus;0.2287x_{2}^2&plus;1.8307x_{2}x_{3}-0.1025x_{2}x_{4}&plus;2.6455x_{3}^2&plus;1.1557x_{3}x_{4}&plus;0.014x_{4}^2" title="\bg_white p(\mathbf x)=-1.4954x_{1}-0.6050x_{2}-2.6590x_{3}-1.2333x_{4}-0.1398x_{1}^2+0.0463x_{1}x_{2}+1.0553x_{1}x_{3}+0.0182x_{1}x_{4}+0.2287x_{2}^2+1.8307x_{2}x_{3}-0.1025x_{2}x_{4}+2.6455x_{3}^2+1.1557x_{3}x_{4}+0.014x_{4}^2" />
</div>
<center>
[Small NN](/Small_NN/C3)
</center>
#### [B(x)](/Barriers/C3.txt)

#### [V(x)](/Lyapunov/C3.txt)
