    
% x=[1 2 3 4 5 6 7 8 9 10];
% avg = comp

% rand_vector = generate_random_vector(y)

x=[0:0.1:2*pi];

plot(x, cos(x), 'color', '#F5A9F7', 'LineWidth', 2);
ylabel('cos(x)', 'color', '#D21D55');
xlabel('x', 'color', '#D21D55');
title ('Cosine Wave Plost', 'color', '#0d6efd','FontSize',14,'FontName' ...
    ,'TimeNewRoman');
grid on;
legend('cosine wave');

%  for loop that calls rand vector and computes mean of each vector
% for i = 1:300
%     rand_vector = generate_random_vector(x)
%     avg = comput_mean(rand_vector)
% end

function rand_vector = generate_random_vector (x)

    rand_vector = randi([1 50],1,10);
    
end
function avg = comput_mean(x)

    avg = sum(x)/length(x);
    
end

 
