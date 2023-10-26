
import numpy as np
import pandas as pd
import scipy.stats as stats

def cohen_d(dataset: pd.DataFrame, trait: str, feature: str) -> float:
    '''
    This function retutns Cohen's d calculated for a certain linguistic marker for a given data subset.  
    '''
    
    sample1,sample2 = dataset[dataset[trait] == 1][feature], dataset[dataset[trait] == 0][feature]
    
    # Calculate the means of the two samples
    mean1, mean2 = np.mean(sample1), np.mean(sample2)
    
    # Calculate the pooled standard deviation
    n1, n2 = len(sample1), len(sample2)
    var1, var2 = np.var(sample1, ddof=1), np.var(sample2, ddof=1) 
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))

    # Calculate Cohen's d
    d = (mean1 - mean2) / pooled_std

    return d

def mann_whitney_u(dataset: pd.DataFrame, trait: str, feature: str) -> tuple[float, float]:
  '''
  This function returns p value calculatad for a single trait for a given data subset.
  '''

  sample_pos, sample_neg = dataset[dataset[trait] == 1], dataset[dataset[trait] == 0]
  u_statistic, mann_whitney_pue = stats.mannwhitneyu(sample_pos[feature], sample_neg[feature], alternative='two-sided')

  return u_statistic, mann_whitney_pue


def is_correct(dataset:pd.DataFrame, baseline: pd.DataFrame, trait: str, feature: str) -> bool:
  '''
  This function returns True Cohen's d calculated for fictional characters
  and Cohen's d obtained for real people have the same sign (positive or negative).
  '''
  
  correct_marker = list(baseline[baseline['feature'] == feature]['gender'])[0]
  sample_pos, sample_neg = dataset[dataset[trait] == 1][feature], dataset[dataset[trait] == 0][feature]

  mean1, mean2 = np.mean(sample_pos), np.mean(sample_neg)


  return True if (correct_marker == 'M' and mean1 - mean2 > 0) or (correct_marker == 'F' and mean1 - mean2 < 0) else False

def d_corresp(baseline: pd.DataFrame, d_fict: dict) -> tuple[list,list,list]:
  '''
  This function returns a list of Cohen's d calculated for real people, 
  a list of Cohen's d calculated for fictional characters, and the names
  of linguistic markers showing statistically significant correlation 
  on a given data subset.
  '''

  real, fict, names = [], [], []

  for marker in d_fict:
    real_d = list(baseline[baseline['feature'] == marker]['cohen_d'])[0]
    if real_d == 'ns':
      continue
    real_d = -float(real_d.replace('–', '-'))
    
    real.append(real_d)
    fict.append(float(d_fict[marker]))
    names.append(marker)

  return real, fict, names

def pb_corr_full(dataset: pd.DataFrame, trait: str, markers: list, alpha:float=0.05) -> dict:
  '''
  This function returns the dictionary of lingusitic markers having statistically
  signigicant correlation with the given trait for the whole dataset
  '''
  
  sign_markers = {}

  for marker in markers:
    corr, pval = stats.pointbiserialr(list(dataset[trait]), list(dataset[marker]))
    if pval < alpha:
      sign_markers[marker] = corr

  return sign_markers

def pb_corr_author(dataset: pd.DataFrame, trait: str, markers: list, alpha:float=0.05) -> dict:
  '''
  This function returns the dictionary of lingusitic markers having statistically
  significant correlation with the given trait per each author
  '''
  
  authors = set(dataset['author'])

  sign_markers = {}

  for author in authors:
    dataset_a = dataset[dataset['author'] == author]
    sign_markers[author] = []

    for marker in markers:
      corr, pval = stats.pointbiserialr(list(dataset_a[trait]), list(dataset_a[marker]))
      if pval < alpha:
        sign_markers[author].append(marker)

  return sign_markers    
