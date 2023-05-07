function results = calculateMS(weight, hip_angle, knee_angle, ankle_angle)

y = load('trainedNetworks.mat');

xIn = [weight; hip_angle; knee_angle; ankle_angle];

hT = y.HipNet(xIn);
kT = y.KneeNet(xIn);
aT = y.AnkleNet(xIn);

results = [hT kT aT];

%mres = jsonencode(results)
end