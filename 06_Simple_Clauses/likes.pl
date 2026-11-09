% Given facts
likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

% Rules from the lab manual
likes(john, X) :- likes(mary, X).
likes(john, Y) :- likes(Y, wine).
likes(john, Y) :- likes(Y, Y).

% Sample queries:
% ?- likes(mary, food).
% ?- likes(john, food).
% ?- likes(john, wine).
% ?- likes(john, Who).
