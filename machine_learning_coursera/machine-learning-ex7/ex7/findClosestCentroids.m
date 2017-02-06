function idx = findClosestCentroids(X, centroids)
%FINDCLOSESTCENTROIDS computes the centroid memberships for every example
%   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
%   in idx for a dataset X where each row is a single example. idx = m x 1 
%   vector of centroid assignments (i.e. each entry in range [1..K])
%

% Set K
K = size(centroids, 1);

% You need to return the following variables correctly.
idx = zeros(size(X,1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Go over every example, find its closest centroid, and store
%               the index inside idx at the appropriate location.
%               Concretely, idx(i) should contain the index of the centroid
%               closest to example i. Hence, it should be a value in the 
%               range 1..K
%
% Note: You can use a for-loop over the examples to compute this.
%

dlen = length(X);

for didx = 1: dlen
  dist = 0;
  item_idx = -1;
  for cidx = 1: K
    v_sim = centroids(cidx, :) - X(didx, :);
    diff = sum(v_sim .* v_sim);
    if ((item_idx == -1) || (dist > diff))
      dist = diff;
      item_idx = cidx;
    end
  end
  idx(didx) = item_idx;
end
% =============================================================

end

