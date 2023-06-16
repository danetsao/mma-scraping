def validate(athlete):
    if not athlete['data']:
        return athlete
    if athlete['data']['first_round_finishes'] == '':
        athlete['data']['first_round_finishes'] = 0
    if athlete['data']['sig_strikes_landed'] == '':
        athlete['data']['sig_strikes_landed'] = 0
    if athlete['data']['sig_strikes_attempted'] == '':
        athlete['data']['sig_strikes_attempted'] = 0
    if athlete['data']['striking_accuracy'] == '':
        athlete['data']['striking_accuracy'] = 0
    if athlete['data']['take_downs_landed'] == '':
        athlete['data']['take_downs_landed'] = 0
    if athlete['data']['take_downs_attempted'] == '':
        athlete['data']['take_downs_attempted'] = 0
    if athlete['data']['take_down_accuracy'] == '':
        athlete['data']['take_down_accuracy'] = 0
    if athlete['data']['sig_strikes_landed_per_min'] == '':
        athlete['data']['sig_strikes_landed_per_min'] = 0
    if athlete['data']['sig_strikes_absorbed_per_min'] == '':
        athlete['data']['sig_strikes_absorbed_per_min'] = 0
    if athlete['data']['take_down_avg_per_15_min'] == '':
        athlete['data']['take_down_avg_per_15_min'] = 0
    if athlete['data']['submission_avg_per_15_min'] == '':
        athlete['data']['submission_avg_per_15_min'] = 0
    if athlete['data']['sig_strikes_defense'] == '':
        athlete['data']['sig_strikes_defense'] = 0
    if athlete['data']['take_down_defense'] == '':
        athlete['data']['take_down_defense'] = 0
    if athlete['data']['kockdown_avg'] == '':
        athlete['data']['kockdown_avg'] = 0
    if athlete['data']['average_fight_time'] == '':
        athlete['data']['average_fight_time'] = 0
    if athlete['data']['sig_strikes_standing'] == '':
        athlete['data']['sig_strikes_standing'] = 0
    if athlete['data']['sig_strikes_clinch'] == '':
        athlete['data']['sig_strikes_clinch'] = 0
    if athlete['data']['sig_strikes_ground'] == '':
        athlete['data']['sig_strikes_ground'] = 0
    if athlete['data']['sig_strike_head'] == '':
        athlete['data']['sig_strike_head'] = 0
    if athlete['data']['sig_strike_body'] == '':
        athlete['data']['sig_strike_body'] = 0
    if athlete['data']['sig_strike_leg'] == '':
        athlete['data']['sig_strike_leg'] = 0
    if athlete['data']['wins_by_knockout'] == '':
        athlete['data']['wins_by_knockout'] = 0
    if athlete['data']['wins_by_submission'] == '':
        athlete['data']['wins_by_submission'] = 0
    if athlete['data']['wins_by_decision'] == '':
        athlete['data']['wins_by_decision'] = 0
    if athlete['data']['fights'] == '':
        athlete['data']['fights'] = []
