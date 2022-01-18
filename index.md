# Benchmark Example

Now we will show our 10 examples below

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.
## c1:Cartpole system
The equation of motion for cartpole system is
<img src="https://latex.codecogs.com/svg.image?\begin{equation*}&space;&space;&space;\begin{bmatrix}&space;&space;&space;&space;&space;&space;&space;&space;\ddot{x}\\&space;&space;&space;&space;&space;&space;&space;&space;\ddot{\theta}&space;&space;&space;&space;\end{bmatrix}&space;&space;&space;&space;=&space;&space;&space;&space;\begin{bmatrix}&space;&space;&space;&space;&space;&space;&space;&space;\frac{u&plus;m_p&space;sin\theta(l\dot\theta^2&space;-gcos(\theta))}{m_c&plus;m_p&space;sin^2(\theta)}&space;\\&space;\frac{ucos(\theta)&plus;m_pl\dot{\theta}^2cos\theta&space;sin\theta&space;-(m_c&plus;m_p)gsin\theta}{l(m_c&plus;m_psin^2\theta)}&space;&space;&space;&space;\end{bmatrix}\end{equation*}" title="\begin{equation*} \begin{bmatrix} \ddot{x}\\ \ddot{\theta} \end{bmatrix} = \begin{bmatrix} \frac{u+m_p sin\theta(l\dot\theta^2 -gcos(\theta))}{m_c+m_p sin^2(\theta)} \\ \frac{ucos(\theta)+m_pl\dot{\theta}^2cos\theta sin\theta -(m_c+m_p)gsin\theta}{l(m_c+m_psin^2\theta)} \end{bmatrix}\end{equation*}" />
with the constants set as<img src="https://latex.codecogs.com/svg.image?m_c=1,m_p=1,m_p=1,g=1,l=1" title="m_c=1,m_p=1,m_p=1,g=1,l=1" />.Define the state space<img src="https://latex.codecogs.com/svg.image?\mathbf&space;x&space;=[x,\theta,\dot{x},\dot{\theta}]&space;" title="\mathbf x =[x,\theta,\dot{x},\dot{\theta}] " />,where
<img src="https://latex.codecogs.com/svg.image?\begin{equation*}\Psi=\{\mathbf&space;x&space;\in&space;\mathbb{R}^4&space;\,|\,&space;[-1.3,-1.3,-1.3,-1.3]^T\leq\mathbf&space;x&space;\leq&space;[1.3,1.3,1.3,1.3]^T\}\end{equation*}" title="\begin{equation*}\Psi=\{\mathbf x \in \mathbb{R}^4 \,|\, [-1.3,-1.3,-1.3,-1.3]^T\leq\mathbf x \leq [1.3,1.3,1.3,1.3]^T\}\end{equation*}" />
### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/JUZI1/RL.github.io/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
