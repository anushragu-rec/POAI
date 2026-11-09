% Find the minimum of two numbers.
minimum(X, Y, X) :- X =< Y.
minimum(X, Y, Y) :- X > Y.

% Find the maximum of two numbers.
maximum(X, Y, X) :- X >= Y.
maximum(X, Y, Y) :- X < Y.

% Example query:
% ?- minimum(8, 3, Min), maximum(8, 3, Max).
% Min = 3,
% Max = 8.
