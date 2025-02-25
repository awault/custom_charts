# Custom Charts
This package provides a quick and easy way to set custom global defaults for Matplotlib styles. Create a unique style that works seamlessly across Codespaces, virtual environments or cloud-based Jupyter instances.

# Installation
To install the package, use the following command:

`pip install git+https://github.com/awault/custom_charts.git`

# Requirements
- matplotlib.pyplot
- seaborn


# Usage
Once the package is installed, import it and apply your custom style:

    import matplotlib.pyplot as plt
    import seaborn as sns
    import custom_charts as cc

    # Call Function for Custom Style
    cc.set_custom_style()

You can also add a text watermark to your charts to provide attribution or prevent unauthorized use. The syntax to create a chart with pyplot remains the same- just add a call to `cc.add_watermark()`.

    plt.scatter(x_values,y_values)
    plt.title("Scatterplot")
    cc.add_watermark()
    plt.ylim(ymin=0,ymax=20)
    plt.show()


# Customization
To create your own unique style, update the settings in the `set_custom_style()` function within `__init__.py` in the `custom_charts` directory. There are additional settings available in the `mystyle.mplstyle` located in the `styles` directory.







