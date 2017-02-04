function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

cands = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
cand_len = size(cands, 2);

min_e = 100000000;
rst_c = 0;
rst_sigma = 0;

for idx_c = 1: cand_len
  for idx_sigma = 1: cand_len
    C = cands(idx_c);
    sigma = cands(idx_sigma);
    model = svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma));
    predictions = svmPredict(model, Xval);
    Eval = mean(double(predictions ~= yval));
    if (Eval < min_e)
      min_e = Eval;
      rst_c = C;
      rst_sigma = sigma;
    end
end

  C = rst_c;
  sigma = rst_sigma;
% =========================================================================

end
