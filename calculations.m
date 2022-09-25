% FINAL EQUATION
syms X pat X0 theta Emu p1 Smu N0 dNdE(Emu,theta,pat) Imu(pat, theta)
g = 9.81; % m/s²
% pat = 98650; % N/m²
X0 = pat/g; % kg/m²
alph = 0.0002; % GeV/(kg/m²)
epsmu = 1;
epsK = 850;
gam = 1.7;
rpi = 0.5731;
LambdaPi = 148;
LambdaN = 115;
rK = 0.0458;
LambdaK = 147;
ZNpi = 0.08;
ZNK = 0.012;
ZNN = 0.2609;
mmu = 0.1056583755; % GeV/c²
c = 299792458; % m/s
p1 = epsmu/(Emu*cos(theta)+alph*X0);
N0 = 1.7*Emu^(-2.7);

Apimu = ZNpi*(1-rpi^(gam+1))/(1-rpi)/(1+gam);
AKmu = ZNK*(1-rK^(gam+1))/(1-rK)/(1+gam);
Bpimu = (gam+2)/(gam+1)*(1-rpi^(gam+1))/(1-rpi^(gam+2))*(LambdaPi-LambdaN)/(LambdaPi*log(LambdaPi/LambdaN));
BKmu = (gam+2)/(gam+1)*(1-rK^(gam+1))/(1-rK^(gam+2))*(LambdaK-LambdaN)/(LambdaK*log(LambdaK/LambdaN));
Smu = (LambdaN*cos(theta)/X0)^p1*(Emu/(Emu+alph*X0/cos(theta)))^(p1+gam+1)*gamma(p1+1);

dNdE(Emu,theta,pat) = Smu*N0/(1-ZNN)*(Apimu/(1+Bpimu*cos(theta)*Emu/epsmu) + 0.635*AKmu/(1+BKmu*cos(theta)*Emu/epsK));

% Imu(pat, theta) = vpaintegral(dNdE,Emu,mmu*c^2,inf);

%% PLOT
pressure = linspace(1,103000);
EmuDist = 10.^linspace(0,4);
% Flux = subs(Imu(pat, 0), pat, pressure);
dNdEPlot = subs(dNdE,{Emu,pat},{EmuDist,pressure}).*EmuDist.*EmuDist.*EmuDist;

%% CREATE GRAPHS
% figure;
% plot(pressure, Flux);
figure;
surf(EmuDist, pressure, dNdE(EmuDist, 0, pressure).*EmuDist.*EmuDist.*EmuDist);
set(gca,'XScale','log')
set(gca,'ZScale','log')
