width=1;
angle = -10.54/30*0.0; %TO ROTATE CLOCKWISE BY X DEGREES
R = [cos(angle) -sin(angle);sin(angle) cos(angle)];  %CREATE THE MATRIX
%R = [0.97 -0.03;0.03 0.97];
x = linspace(-width*0.0,width);
y = linspace(-width,width);
[Xq,Yq] = meshgrid(x,y); % Original
XY = [Xq(:) Yq(:)]; % Create Matrix Of Vectors
%Z = sin(X) + cos(Y);
rotXY=XY*R';  %MULTIPLY VECTORS BY THE ROT MATRIX
Z = Xq.*exp(-(Xq.^2+Yq.^2)/width^2); % ‘Z’ To Provide A Surface
phi=det(R*R);
%Z = sin(X)

%contourf(X,Y,Z,10)
%colorbar("on")
Xqr = reshape(rotXY(:,1), size(Xq,1), []);
Yqr = reshape(rotXY(:,2), size(Yq,1), []);


Zr = exp(-(Xqr.^2+Yqr.^2-2*Xqr.*sqrt(Xqr.^2+Yqr.^2)*phi+phi^2)/width^2); % ‘Z’ Provides A Surface


%Zr = Zr/max(max(Zr));

contour(Xqr,Yqr,Zr,10,'ShowText',"on", 'linecolor','k') % Rotated contour(X,Y,Z,'ShowText','on')
t = xlabel('z_R');
t = ylabel('r');
%,true,"LabelFormat","%0.1f m"

%contour(Zr,10,"ShowText","on","LabelFormat",@mylabel, 'linecolor','b')
xlim([0 width])
ylim([-width width])

function labels = mylabel(vals)
feetPerMeter = 3.28084;
feet = round(vals.*feetPerMeter);
labels = vals + " m (" + feet + " ft)";
labels(vals == 0) = "0 nm";
end
