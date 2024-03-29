# -*- coding: utf-8 -*-
"""GradientDescent&CostFunction_CB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ac7ygK-_CZOP48go_IgF02wq2phxEnUi
"""

import numpy as np

def gradientdescent(x,y):
  m_curr=b_curr=0
  iterations=1000
  learning_rate=0.0001
  n=len(x)

  for i in range (iterations):
    y_predicted=(m_curr*x)+b_curr
    cost=(1/n) * sum([val**2 for val in  (y-y_predicted)])
    md=(-2/n)*sum(x*(y-y_predicted))
    bd=(-2/n)*sum((y-y_predicted))
    m_curr=m_curr-learning_rate*md
    b_curr=b_curr-learning_rate*bd
    print("m=  {}   b=  {}    cost=  {}    iteration= {}".format(m_curr,b_curr, cost,i))

x=np.array([24,25,26,27,28])
y=np.array([29,30,31,32,33])
gradientdescent(x,y)

