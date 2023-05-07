function mus_res = muscleGroup(hip_angle, knee_angle, ankle_angle, value)
y = load('trainedNetworks.mat');

keys = ["Hip Flexors","Hip Extensors", "Knee Flexors", "Knee Extensors","Ankle Dorsiflexors","Ankle Plantarflexors"];
hf = "Psoas Major";
he = ["Gluteus Maximus","Biceps Femoris"];
kf = "Gastrocnemius Lat";
ke = ["Rectus Femoris","Vastus Intermedius"];
ad = "Tibialis Anterior";
ap = ["Soleus","Gastrocnemius Med"];

valueArr = {hf,he,kf,ke,ad,ap};
M = containers.Map(keys, valueArr, 'UniformValues',false);

dispArr = M(value);

actVal = dictionary;
muscles = ["Psoas Major","Gluteus Maximus","Biceps Femoris","Gastrocnemius Lat","Rectus Femoris","Vastus Intermedius","Tibialis Anterior","Soleus","Gastrocnemius Med"];
act = [0,0,0,0,0,0,0,0,0];

hip = hip_angle * 0.0174533;
act(1) = y.H_psoas_net(hip);
act(2) = y.H_glut_net(hip);
act(3) = y.H_fem_net(hip);

knee = knee_angle * 0.0174533;
act(4) = y.k_gast_net(knee);
act(5) = y.K_rect_net(knee);
act(6) = y.K_vas_net(knee);

ankle = ankle_angle * 0.0174533;
act(7) = y.A_tib_net(ankle);
act(8) = y.A_sol_net(ankle);
act(9) = y.A_gast_net(ankle);

actVal(muscles) = act;

str = "";
for i = 1:length(dispArr)
    str = str + dispArr(i) + ":" + actVal(dispArr(i)) +  newline ;
end

mus_res = str;
end
