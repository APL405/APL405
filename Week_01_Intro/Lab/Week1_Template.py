
"""
Mohr circle in 3D.
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigvalsh
from matplotlib import rcParams
 
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

class mohr():
  def plot_mohr3d(self, S):
    """Plot 3D Mohr circles."""
    ''' This method "plot_mohr3d()" definition should evaluate the principal stress components from any arbitrary stress tensor(S).
        Then, calculate major, minor and intermediate radius of Mohr's circle.'''
    
    #-------Your Code-------- 
    
    # Write func to calculate Eigen values of the stress tensor in increasing order of magnitude i.e. Principal Stresses in this line.

    # R_maj =                #Major radius
    # cent_maj =             #Centre of the major circle
    
    #R_min =                 #Minor Radius
    #cent_min =              #Centre of the minor circle
    
    #R_mid =                 #Intermediate (Radius of circle which includes both major and minor circle)
    #cent_mid = 
    
    # Plot your FIGURE of Mohr circle
    S_eigen = np.linalg.eigvals(S)

    S_eigen_sorted = np.sort(S_eigen)
    S3 = S_eigen_sorted[2]
    S2 = S_eigen_sorted[1]
    S1 = S_eigen_sorted[0]

    R_maj = 0.5*(S3 - S1)
    cent_maj = 0.5*(S1+S3)
    
    R_min = 0.5*(S2 - S1)
    cent_min = 0.5*(S2 + S1)
    
    R_mid = 0.5*(S3 - S2)
    cent_mid = 0.5*(S3 + S2)
    
    circ1 = plt.Circle((cent_maj,0), R_maj, facecolor='#cce885', lw=3, 
                       edgecolor='#5c8037')
    circ2 = plt.Circle((cent_min,0), R_min, facecolor='w', lw=3,
                       edgecolor='#15a1bd')
    circ3 = plt.Circle((cent_mid,0), R_mid, facecolor='w', lw=3,
                       edgecolor='#e4612d')
    plt.axis('image')
    ax = plt.gca()
    ax.add_artist(circ1)
    ax.add_artist(circ2)
    ax.add_artist(circ3)
    ax.set_xlim(S1 - .1*R_maj, S3 + .1*R_maj)
    ax.set_ylim(-1.1*R_maj, 1.1*R_maj)
    plt.xlabel(r"$\sigma$", size=18)
    plt.ylabel(r"$\tau$", size=18)
    #plt.savefig('Mohr_circle_3D.svg')
    plt.show()

    return R_maj, R_min, R_mid
