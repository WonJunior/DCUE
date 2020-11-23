from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
from statistics import mean

def bar(x, title='', xlabel='', ylabel=''):
    freq = Counter(sorted(x))
    count = sum(freq.values())
    height = [f/count*100 for f in freq.values()]

    ax = plt.subplot()
    ax.bar(freq.keys(), height, align='center', color='#3c3c3c', alpha=0.5)
    ax.yaxis.set_major_formatter(tick.PercentFormatter())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def show_perf(state, source):
    nb_updates = len(state['losses'])
    nb_batches = nb_updates // state['epoch']
    losses = state['losses']
    accuracies = [acc*100 for acc in state['accuracies']]
    avg_losses = [mean(losses[i:i+nb_batches]) for i in range(0, nb_updates, nb_batches)]
    avg_accuracies = [mean(accuracies[i:i+nb_batches]) for i in range(0, nb_updates, nb_batches)]

    fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 7))
    fig.suptitle('Plotting from %s' % source, fontsize=11)

    x_ticks = range(0, nb_updates+nb_batches, nb_batches)
    x_labels = range(state['epoch']+1)

    ax1.set_xticks(x_ticks)
    ax1.set_xticklabels(x_labels)
    ax1.plot(range(0, nb_updates, nb_batches), avg_losses, linewidth=0.6, color='blue', label='loss over epochs')
    ax1.plot(losses, linewidth=0.2, color='black', label='loss over batches')
    ax1.legend(fontsize=9)
    ax1.set_ylabel('loss')

    ax2.set_xlabel('epochs')
    ax2.set_xticks(x_ticks)
    ax2.set_xticklabels(x_labels)
    ax2.plot(range(0, nb_updates, nb_batches), avg_accuracies, linewidth=0.6, color='red', label='acc over epochs')
    ax2.plot(accuracies, linewidth=0, color='black', label='accuracy over batches')
    ax2.set_ylim(bottom=min(avg_accuracies)-1, top=max(avg_accuracies)+1)
    ax2.set_ylabel('accuracy')
    ax2.grid()
    ax2.yaxis.set_major_formatter(tick.PercentFormatter())

    fig.tight_layout()
    plt.show()
