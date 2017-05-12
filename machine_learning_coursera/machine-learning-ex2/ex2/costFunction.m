function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta
%

h_theta = sigmoid(X * theta);
j_sum = 0;
pval = -100000000;
for iter = 1:m
  tval = h_theta(iter);
  if (y(iter) == 0)
    if (tval == 1)
      j_sum = j_sum - pval;
    else
      j_sum = j_sum - log(1 - tval);
    end
  else
    if (tval == 0)
      j_sum -= pval;
    else
      j_sum -= log(tval);
    end
  end

end

J = j_sum / m;

grad = (((h_theta - y)' * X) / m)';

% =============================================================

end
