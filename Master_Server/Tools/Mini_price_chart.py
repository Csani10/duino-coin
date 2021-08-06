# Create a small chart of duco exchange price
# 2021 revox from the Duino team

import matplotlib
import datetime
from scipy.interpolate import make_interp_spline, BSpline
from scipy.interpolate import interp1d
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

pricefile = "prices.txt"

dayinterval = 3
length = 20
outputfile = "/home/debian/websites/duino-coin-websocket-proxy/mini_prices.png"
chartColors = ["#0abde3"]


def splitData(pricefile):
    """Read prices from text file generated by the server to list"""
    priceList = []
    with open(pricefile) as file:
        content = file.read()
        priceList = content.replace("\n", "").split(",")
    return priceList


def createGraph(y_ducoe, dayinterval, length, outputfile, chartColors):
    """Create matplotlib price graph with given arguments"""
    now = datetime.datetime.now() - datetime.timedelta(days=len(y_ducoe))
    then = now + datetime.timedelta(days=len(y_ducoe))
    days = mdates.drange(
        now,
        then,
        datetime.timedelta(days=1))
    xnew = np.linspace(
        days.min(),
        days.max(),
        len(y_ducoe))

    spl = interp1d(days, y_ducoe)
    y_smooth = spl(xnew)

    plt.plot(
        xnew,
        y_smooth,
        "-ok",
        linewidth=4,
        color=chartColors[0])
    plt.axis('off')
    plt.savefig(
        outputfile,
        dpi=40, bbox_inches='tight',
        transparent=True)


y_ducoe = splitData(pricefile)[-length:]
createGraph(
    y_ducoe, dayinterval, length, outputfile, chartColors)

print("Successfully updated the plot")