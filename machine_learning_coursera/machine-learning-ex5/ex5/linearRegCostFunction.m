function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%

h_theta = X * theta;

j_left = sum((h_theta - y) .* (h_theta - y));
j_right = sum(theta .* theta) - theta(1)^2;

J = (j_left + j_right * lambda) / 2 / m;

grad_theta = theta(:);
grad_theta(1) = 0;
grad = (((h_theta  - y)' * X)' + (lambda * grad_theta)) / m;

% =========================================================================

grad = grad(:);

end
