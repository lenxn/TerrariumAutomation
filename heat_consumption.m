A_wood = 1.7*1.8 + 2*1.8 + 1.7*1.8 - 1.5*1.4; % [m^2] Area Wood
A_glas = 1.5 * 1.4;
A_pst = A_wood; % [m^2] Area Polystyrol


lambda_pst = 0.17; % [W m^-1 K^-1] Thermal Conductivitiy Polystyrol
lambda_wood = 0.15; % [W m^-1 K^-1] Thermal Conductivitiy Wood
lambda_glas = 0.76;

delta_pst = 0.02; % [m] Thickness PST
delta_wood = 0.02; % [m] Thickness Wood
delta_glas = 0.0008;

To = 295.15; % [K] Temperature Outside (22 C)
Ti = 303.15; % [K] Temperature Inside (30 C)

%% Overall Q_dot by Superposition

delta_T = Ti - To;

Q_dot_pst = lambda_pst/ delta_pst * A_pst * delta_T;
Q_dot_wood = lambda_wood/ delta_wood * A_wood * delta_T;
Q_dot_glas = lambda_glas/ delta_glas * A_glas * delta_T;

Q_dot = Q_dot_pst + Q_dot_wood + Q_dot_glas
