""" Exogenous inputs
"""

# Initiating time parameter
T = 40
num_firms = 8
num_consumers = 2000

# Initial cost per unit of energy
pe_combustion = None
pe_electric = None
# Emissions
em_combustion = 1
em_electric = 1

# Distance of consumers
Dk = 100

# Taxes
IVA = None

# Costs of adoption of new technology
Cost_adoption = 0

# ROI
p_lambda = 1
min_rd = .05
alpha1 = 1

# External limits parameters
PC_min = None
EE_max = None
EC_max = None
QL_max = None

Fixed_Costs = 0

# Station availability for each type of energy
# Global
# electric_cars participation in the market
market_share_electric = 0
W_electric = 1 + market_share_electric
W_combustion = 2

# Constraints
# t == 0:
# PC_min < PCij = 'combustion' < PCij = 'electric' - cost production







