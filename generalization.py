import matplotlib.pyplot as plt
import pandas as pd

import model


# Which figures do we want?
# Which data is necessary to save to produce those figures (everything related to benchmarket)?
# All data needs to be collected for all 'Ts'
# 1. EMISSIONS
# 2. Green market-share increase
# 3. Public income? (how to calculate net benefits)


def processing_averages(pol_results):
    # Receives a specific policy dictionary of results of runs and processes the averages
    averages = dict()
    cols = ['green_market_share', 'new_firms_share', 'emissions_index', 'public']
    for col in cols:
        averages[col] = pd.DataFrame()
    for run in pol_results:
        for col in cols:
            averages[col].loc[:, run] = pol_results[run][col]
    for col in cols:
        averages[col] = averages[col].mean(axis=1)
    return averages


def plot_details(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    # ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))
    plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
    plt.tick_params(axis='both', which='both', bottom=False, top=False,
                    labelbottom=True, left=False, right=False, labelleft=True)
    return ax


def plotting(results, n):
    # Receives a dictionary of results for policies and inside Ts runs with DataFrame reports
    notes = {'green_market_share': ['Green market percentage (%)', 'yellowgreen'],
             'new_firms_share': ['Share of new firms (%)', 'dimgrey'],
             'emissions_index': ['Emissions index', 'darkblue'],
             'public': ['Net public expenditure ($)', 'firebrick']}
    for pol in results:
        res = processing_averages(results[pol])
        fig, ax = plt.subplots()
        for key in res:
            ax.plot(res[key].index, res[key], label=notes[key][0], color=notes[key][1])
        ax.legend(frameon=False)
        ax = plot_details(ax)
        ax.set(xlabel='T periods', ylabel='value', title=f'Results after {n} runs using policy: {pol}')
        plt.savefig(f'results/{pol}.png', bbox_inches='tight')
        plt.show()
    return res


def running(n=10):
    # Available policies are: 'max_e', 'tax', 'discount', 'green_support'
    # Available levels are: 'low' and 'high'
    pol, level = None, None
    # pol = 'green_support'
    # level = 'low'
    p = {'policy': pol, 'level': level}
    v = False
    # For each run policy, when dictionary with all runs is saved.
    # Thus, result collected is a dictionary of dictionaries containing DataFrames
    results = {pol: dict()}
    for i in range(n):
        s = model.main(p, v)
        results[pol][i] = s.report
    return results


if __name__ == '__main__':
    m = 4
    r = running(m)
    a = plotting(r, m)
