function g = sigmoid(z)
%SIGMOID Compute sigmoid function
%   g = SIGMOID(z) computes the sigmoid of z.

% You need to return the following variables correctly 
g = zeros(size(z));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%               vector or scalar).
z_size = size(z);
for z_i = 1: z_size(1)
  for z_j = 1: z_size(2)
    g(z_i, z_j) = 1 / (1 + e^(-z(z_i, z_j)));
  end
end
% =============================================================

end
