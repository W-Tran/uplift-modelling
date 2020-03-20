import pandas as pd
import numpy as np


def compute_treatment_effect(results_df, for_response=True):
    if for_response:
        targeting_strategy = 'response_decile'
    else:
        targeting_strategy = 'uplift_decile'
    treatment_group = results_df[results_df.Treatment == 1]
    control_group = results_df[results_df.Treatment == 0]

    treatment_visit_rates = (treatment_group.groupby(targeting_strategy)['Outcome'].mean() * 100)
    control_visit_rates = (control_group.groupby(targeting_strategy)['Outcome'].mean() * 100)

    treatment_effect = (treatment_visit_rates - control_visit_rates).reset_index()
    treatment_effect[targeting_strategy] = treatment_effect[targeting_strategy].astype(str)
    treatment_effect.columns = [targeting_strategy, 'treatment_effect']
    return treatment_effect


def compute_visit_rates(results_df, for_response=True):
    if for_response:
        targeting_strategy = 'response_decile'
    else:
        targeting_strategy = 'uplift_decile'

    treatment_group = results_df[results_df.Treatment == 1]
    control_group = results_df[results_df.Treatment == 0]

    treatment_visit_rates = (treatment_group.groupby(targeting_strategy)['Outcome'].mean() * 100).reset_index()
    control_visit_rates = (control_group.groupby(targeting_strategy)['Outcome'].mean() * 100).reset_index()

    treatment_visit_rates[targeting_strategy] = treatment_visit_rates[targeting_strategy].astype(str)
    control_visit_rates[targeting_strategy] = control_visit_rates[targeting_strategy].astype(str)

    treatment_visit_rates.columns = [targeting_strategy, 'visit_rate']
    control_visit_rates.columns = [targeting_strategy, 'visit_rate']

    return treatment_visit_rates, control_visit_rates


def _compute_pooled_proportion(p1, n1, p2, n2):
    return ((p1 * n1) + (p2 * n2)) / (n1 + n2)


def _compute_se(p, n1, n2):
    return np.sqrt(p * (1 - p) * ((1 / n1) + (1 / n2)))


def cumulative_treatment_effect(results_df, for_response=True):
    if for_response:
        targeting_strategy = 'response_decile'
    else:
        targeting_strategy = 'uplift_decile'
    treatment_group = results_df[results_df.Treatment == 1]
    control_group = results_df[results_df.Treatment == 0]

    treatment_group_visits = treatment_group.groupby(targeting_strategy)['Outcome'].sum().reset_index()
    treatment_group_visits['total'] = treatment_group.groupby(targeting_strategy)['Outcome'].count().values
    control_group_visits = control_group.groupby(targeting_strategy)['Outcome'].sum().reset_index()
    control_group_visits['total'] = control_group.groupby(targeting_strategy)['Outcome'].count().values

    treatment_group_visits[targeting_strategy] = treatment_group_visits[targeting_strategy].astype(str)
    control_group_visits[targeting_strategy] = control_group_visits[targeting_strategy].astype(str)

    treatment_group_visits.columns = [targeting_strategy, 'num_website_visits', 'total_website_visits']
    control_group_visits.columns = [targeting_strategy, 'num_website_visits', 'total_website_visits']

    # Highest to Lowest decile groups
    treatment_group_visits, control_group_visits = treatment_group_visits.iloc[::-1], control_group_visits.iloc[::-1]

    treatment_group_visits['visits_cumul'] = treatment_group_visits['num_website_visits'].cumsum()
    treatment_group_visits['total_visits_cumul'] = treatment_group_visits['total_website_visits'].cumsum()
    treatment_group_visits['cumul_visit_rate'] = treatment_group_visits['visits_cumul'] / treatment_group_visits[
        'total_visits_cumul']
    control_group_visits['visits_cumul'] = control_group_visits['num_website_visits'].cumsum()
    control_group_visits['total_visits_cumul'] = control_group_visits['total_website_visits'].cumsum()
    control_group_visits['cumul_visit_rate'] = control_group_visits['visits_cumul'] / control_group_visits[
        'total_visits_cumul']

    treatment_effects = treatment_group_visits['cumul_visit_rate'].to_frame().copy().rename(columns={
        'cumul_visit_rate': 'treatment_cumul_visit_rate'})
    treatment_effects['control_cumul_visit_rate'] = control_group_visits['cumul_visit_rate']
    treatment_effects['cumul_treatment_effect'] = (treatment_group_visits['cumul_visit_rate'] - control_group_visits[
        'cumul_visit_rate'])
    p1, p2 = treatment_group_visits['cumul_visit_rate'], control_group_visits['cumul_visit_rate']
    n1, n2 = treatment_group_visits['total_visits_cumul'], control_group_visits['total_visits_cumul']
    treatment_effects['pooled_proportion'] = _compute_pooled_proportion(p1, n1, p2, n2)
    treatment_effects['standard_error'] = _compute_se(treatment_effects['pooled_proportion'].values, n1, n2)

    return treatment_effects.reset_index(drop=True)
