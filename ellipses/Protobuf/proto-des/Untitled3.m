a = xlsread ('Cartel1.xlsx');
x = a (:,1);
B = fft (x);
y = a (:,2);
D = fft (y);
X = a (:,3);
Y = a (:,4);
Ax = a (:,5);
Ay = a (:,6);
Cx = a (:,7);
Cy = a (:,8);
Fivecirclex = a (:,9);
Fivecircley = a (:,10);
Onecirclex = a (:,11);
Onecircley = a (:,12);
Sqx = a (:,13);
Sqy = a (:,14);
Mx = a (:,15);
My = a (:,16);
dot1x = a (:,17);
dot1y = a (:,18);
linexx = a (:,25);
linexy = a (:,26);
lineyx = a (:,23);
lineyy = a (:,24);

% figure (1)
% plot (x,y,X,Y)
% 
% figure (2)
% plot (Ax,Ay)
% 
% figure (3)
% plot (Cx,Cy)
% 
% figure (4)
% plot (Fivecirclex,Fivecircley)
% 
% figure (5)
% plot (Onecirclex,Onecircley)
% 
% %figure (6)
% %plot (Sqx,Sqy)
% 
% %figure (7)
% %plot (Mx,My)

% figure (8)
% plot (dot1x,dot1y)
% 
% figure (9)
% plot (linexx,linexy)
% 
% figure (10)
% plot (lineyx,lineyy)


