function plotData(X, y)
%PLOTDATA Plots the data points X and y into a new figure 
%   PLOTDATA(x,y) plots the data points with + for the positive examples
%   and o for the negative examples. X is assumed to be a Mx2 matrix.

% Create New Figure
figure; hold on;

% ====================== YOUR CODE HERE ======================
% Instructions: Plot the positive and negative examples on a
%               2D plot, using the option 'k+' for the positive
%               examples and 'ko' for the negative examples.
%
m = length(y);

for iter = 1:m
  x = X(iter);
  y_val = y(iter);
  if (y_val > 0)
    plot(X(iter, 1), X(iter, 2), 'k+', 'LineWidth', 2, 'MarkerSize', 7);
  else
    plot(X(iter, 1), X(iter, 2), 'ro', 'MarkerFaceColor', 'y', 'MarkerSize', 7);

  end
end






% =========================================================================



hold off;

end
