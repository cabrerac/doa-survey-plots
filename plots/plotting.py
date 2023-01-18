import pandas as pd
pd.options.mode.chained_assignment = None
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from pathlib import Path


# figures variables
SMALL_SIZE = 20
MEDIUM_SIZE = 26
LARGE_SIZE = 32
plt.rc('font', size=SMALL_SIZE, family='Times New Roman')
plt.rc('font', size=SMALL_SIZE)
plt.rc('axes', titlesize=MEDIUM_SIZE)
plt.rc('axes', labelsize=MEDIUM_SIZE)
plt.rc('axes', linewidth=2.0)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)
plt.rc('figure', titlesize=LARGE_SIZE)
sns.set_palette("Paired")


# plots experiment results
def plot_results(data_path):
    results = pd.read_csv(data_path)
    total_papers = len(results.index)
    results = results.drop(columns=['id', 'research work'])
    counts = results.apply(pd.value_counts)
    counts = counts.fillna(0)
    counts = counts/total_papers
    counts = counts.reindex(['full', 'partial', 'no'])

    data_first = counts[["data driven", "shared data model", "data coupling"]]
    xticks = ["Data-driven", "Shared data \n model", "Data coupling"]
    yticks = ["Full", "Partial", "No"]
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    sns.heatmap(data_first, annot=True, cmap="Blues", vmin=0, vmax=1, fmt='.1%', cbar=False, linewidth=.5, xticklabels=xticks, yticklabels=yticks, ax=ax)
    ax.set(xlabel="Principle", ylabel="Adoption")
    fig.savefig('./figs/data-first.pdf')

    decentralised = counts[["local data chunks", "local first", "wireless first"]]
    xticks = ["Local data \n chunks", "Local first", "Peer-to-peer \n first"]
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    sns.heatmap(decentralised, annot=True, cmap="Blues", vmin=0, vmax=1, fmt='.1%', cbar=False, linewidth=.5, xticklabels=xticks, yticklabels=yticks, ax=ax)
    ax.set(xlabel="Principle", ylabel="Adoption")
    fig.savefig('./figs/decentralised.pdf')

    openness = counts[["autonomous entities", "asynchronous entities", "message protocol"]]
    xticks = ["Autonomous \n entities", "Asynchronous \n entities", "Message protocol"]
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    sns.heatmap(openness, annot=True, cmap="Blues", vmin=0, vmax=1, fmt='.1%', cbar=False, linewidth=.5, xticklabels=xticks, yticklabels=yticks, ax=ax)
    ax.set(xlabel="Principle", ylabel="Adoption")
    fig.savefig('./figs/openness.pdf')