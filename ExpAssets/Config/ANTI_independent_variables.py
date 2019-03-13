from klibs.KLIndependentVariable import IndependentVariableSet


# Initialize object containing project's independent variables

ANTI_ind_vars = IndependentVariableSet()


# Define project variables and variable types


## Factors ##
# 'alerting_trial': the presence or absence of an auditory alerting signal
# 'cue_type': the type of cue ("valid" == same location as 'target_location')
# 'target_location': the location of the target and flanker arrows
# 'target_direction': the direction of the target arrow
# 'flanker_type': the type of flanker arrow (same direction, opposite direction, or plain line)
# 'soa': interval between cue on and target on. 500 in Callejas et al. (2005) E1, 100/500 in E2

ANTI_ind_vars.add_variable("alerting_trial", bool, [True, False])
ANTI_ind_vars.add_variable("cue_type", str, ["valid", "invalid", "none"])
ANTI_ind_vars.add_variable("target_location", str, ["above", "below"])
ANTI_ind_vars.add_variable("target_direction", str, ["left", "right"])
ANTI_ind_vars.add_variable("flanker_type", str, ["congruent", "neutral", "incongruent"])
ANTI_ind_vars.add_variable("soa", int, [500])
