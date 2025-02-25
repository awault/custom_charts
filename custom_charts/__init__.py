# custom_charts/__init__.py

def custom_charts(data):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8,4))
    # Create Watermark
    plt.figtext(x=0.89, y=0.12, s="©2025 New Insight Analytics", 
                color='#054f70', fontsize=10, weight='ultralight',
                ha='right', va='bottom', transform=plt.gcf().transFigure)
    plt.plot(data)
    plt.show()