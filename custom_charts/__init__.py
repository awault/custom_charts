# custom_charts/__init__.py

import matplotlib.pyplot as plt
import matplotlib as mpl

def custom_charts(data):
    plt.figure(figsize=(8,4))
    # Create Watermark
    plt.figtext(x=0.89, y=0.12, s="©2025 New Insight Analytics", 
                color='#054f70', fontsize=10, weight='ultralight',
                ha='right', va='bottom', transform=plt.gcf().transFigure)
    plt.plot(data)
    plt.show()