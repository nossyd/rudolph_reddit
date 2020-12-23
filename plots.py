import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


#------------------------------------------------------------------------------------------------------------------------
#               Token Frequency Plot
#------------------------------------------------------------------------------------------------------------------------
def plot_freqdist_freq(fd,
                       max_num=None,
                       cumulative=False,
                       title='Frequency plot',
                       linewidth=2):
    """
    As of NLTK version 3.2.1, FreqDist.plot() plots the counts
    and has no kwarg for normalising to frequency.
    Work this around here.

    INPUT:
        - the FreqDist object
        - max_num: if specified, only plot up to this number of items
          (they are already sorted descending by the FreqDist)
        - cumulative: bool (defaults to False)
        - title: the title to give the plot
        - linewidth: the width of line to use (defaults to 2)
    OUTPUT: plot the freq and return None.
    """
    plt.figure(figsize=(16,5))
    tmp = fd.copy()
    norm = fd.N()
    for key in tmp.keys():
        tmp[key] = float(fd[key]) / norm

    if max_num:
        tmp.plot(max_num, cumulative=cumulative,
                 title=title, linewidth=linewidth)
        degrees = 45
        plt.xticks(rotation=degrees)
        
        
    else:
        tmp.plot(cumulative=cumulative,
                 title=title,
                 linewidth=linewidth)
        degrees = 45
        plt.xticks(rotation=degrees)
    plt.gcf().clear()
    return



#------------------------------------------------------------------------------------------------------------------------
#               Token Frequency Plot Bar
#------------------------------------------------------------------------------------------------------------------------
def plot_freqdist_freq_bar(fd,
                       max_num=50,
                       title='Frequency plot'):
    """
    As of NLTK version 3.2.1, FreqDist.plot() plots the counts
    and has no kwarg for normalising to frequency.
    Work this around here.

    INPUT:
        - the FreqDist object
        - max_num: if specified, only plot up to this number of items
          (they are already sorted descending by the FreqDist)
        - cumulative: bool (defaults to False)
        - title: the title to give the plot
        - linewidth: the width of line to use (defaults to 2)
    OUTPUT: plot the freq and return None.
    """
    sns.set(style="ticks",
    rc={
        "figure.figsize": [17.5, 7.5],
        "text.color": "white",
        "axes.labelcolor": "white",
        "axes.edgecolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "axes.facecolor": "#5C0E10",
        "figure.facecolor": "#5C0E10"}
    )
    tmp = fd.copy()
    norm = fd.N()
    for key in tmp.keys():
        tmp[key] = float(fd[key]) / norm
    df = pd.DataFrame(data=tmp.most_common(max_num), columns=['words', 'freq'])

    sns.barplot(x=df['freq'], y=df['words'], palette="Blues_d", linewidth=0)
    plt.title("{}".format(title))
    degrees = 70
    plt.xticks(rotation=degrees)
    
    plt.tight_layout()
    plt.show()
    plt.clf()

    # Find at most 101 ticks on the y-axis at 'nice' locations  
    #max_yticks = 60
    #yloc = plt.MaxNLocator(max_yticks)
    #ax.yaxis.set_major_locator(yloc)
    plt.gcf().clear()
    return
