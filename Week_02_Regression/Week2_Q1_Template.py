# -*- coding: utf-8 -*-
"""Week2_Template_NR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JHbIfKN5lTgvibrMxcIPqy7rv9py4O76

# Nonlinear  Regression

Fill the blank spaces as required. 

Do not change name of any class, method name.
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from matplotlib import pyplot as plt

# %matplotlib inline

class nlr:
  # Evaluates the gradient of cost function (J). Hint: You can use this to optimize w
  def grad(self,x,y,w):
    grad_J = # 
    return grad_J

  # This function calculates the cost (J)
  def computeCost(self,x,y,w):
    J = 0    # J is cost function
    # write your code to calculate J
    return J
  
  # This function optimizes the weights w_0, w_1, w_2. Batch Gradient Descent method
  def BgradientDescent(self, x, y, w, alpha, iters):
    m =    # number of training examples
    w = w.copy() # To keep a copy of original weights
    
    J_history = []   # Use a python list to save cost in every iteration

    for i in range(iters):
      # Loop to update weights (w vector)
      # Also save cost at every step

    return w, J_history
  
  # This function optimizes the weights w_0, w_1, w_2. Stochastic Gradient Descent method
  def SgradientDescent(self, x, y, w, alpha, iters):
    m =    # number of training examples
    w = w.copy() # To keep a copy of original weights
    
    J_history_s = []   # Use a python list to save cost in every iteration

    for i in range(iters):
      r = # generate random integers (refer lab demo code)
      # create randomly a minibatch from whole data set and find weights based on that new data set.
      # Loop to update weights (w vector)
      # Also save cost at every step

    return w, J_history_s
  
  # This function implements line search Secant method
  # refer to class notes on optimization and lab demo copy.
  def ls_secant(self,x,y,w,d):
    # d is search direction d = -grad(J). Refer class and Lab notes
    epsilon = 10**(-4) # Line search tolerance
    
    alpha_curr = 0     # Alpha (x_i-1)
    alpha = 0.01       # initial value (x_i)

    dphi_zero =            # dphi_zero = (d^T)(grad J(w_0) # At every alpha updation loop you will have a given initial weight vector (w_0)
    dphi_curr = dphi_zero  # required for first alpha iteration
    i = 0
    while abs(dphi_curr) > (epsilon*abs(dphi_zero)):  # tolerance or looping criteria used here
      # write loop to update alpha


    return alpha

  # This function optimizes the weights w_0, w_1, w_2. Batch Gradient Descent method using variable alpha which you previously updated using ls_secant() method
  def AgradientDescent(self,x, y, w, iters):
    m =    # number of training examples
    w = w.copy() # To keep a copy of original weights
    eps = 10**(-12); # tolerance for J_history

    J_history_a = [0]   # Use a python list to save cost in every iteration

    for i in range(iters):
      d = # d is search direction d = -grad(J)
      alpha = # update alpha at every iteration
  
      # Loop to update weights (w vector)
      # Also save cost at every step in J_history_a
      # stopping criteria
      if (J_history_a[i+1] -J_history_a[i]) < eps:
        print('No. of iterations',i)
        break

    return w, J_history_a

