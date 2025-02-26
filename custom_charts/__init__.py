# custom_charts/__init__.py
import matplotlib.pyplot as plt
import matplotlib as mpl
import os


def set_custom_style():
    style_path = os.path.join(os.path.dirname(__file__), 'styles', 'mystyle.mplstyle')
    plt.style.use(['bmh', style_path]) # style_path connects to mystyle.mplstyle
    plt.set_cmap('crest') # select a colormap
    plt.rcParams['figure.figsize'] = (8,4) # Set default figure size
    plt.rcParams['axes.titlecolor'] = '#4f4f4f'  # Set title color
    plt.rcParams['axes.labelcolor'] = '#636365'  # Set label color
    plt.rcParams['ytick.labelcolor'] = '#636365' # Set y axis tick label color
    plt.rcParams['xtick.labelcolor'] = '#636365' # Set x axis tick label color

def add_watermark():
    fig = plt.gcf()
    fig.text(x=0.89, y=0.12, s="©2025 New Insight Analytics", 
                color='#4f4f4f', fontsize=10, weight='ultralight',
                ha='right', va='bottom', transform=fig.transFigure)
    



