% ============================================
% PROGRAM 1: Students, Courses, and Professors
% ============================================

% FACTS
studies(charlie, csc135).
studies(olivia, csc135).
studies(jack, csc131).
studies(arthur, csc134).
studies(emma, csc171).
studies(mia, csc135).

teaches(kirke, csc135).
teaches(collins, csc131).
teaches(collins, csc171).
teaches(juniper, csc134).
teaches(anderson, csc135).

% RULE: Professor teaches a student if they share a course
professor(X, Y) :-
    teaches(X, C),
    studies(Y, C).

% ============================================
% QUERIES TO RUN IN SWISH
% ============================================

/*
Copy and paste these queries one by one into SWISH:

1. studies(charlie, What).
2. studies(Who, csc135).
3. professor(kirke, Students).
4. professor(collins, Who).
5. findall((X,Y), professor(X,Y), List).
6. teaches(collins, Course).
7. studies(olivia, Course).
*/


% ============================================
% PROGRAM 2: Apartment Pets
% ============================================

% FACTS
poodle(fluffy).
poodle(tommy).

cat(sushi).
cat(whiskers).

dog(tommy).
dog(rocky).

% RULES
dog(X) :- poodle(X).

pet(X) :- cat(X).
pet(X) :- dog(X).

small(tommy).
small(sushi).

small(X) :- poodle(X).

apartmentpet(X) :- pet(X), small(X).

% ============================================
% QUERIES TO RUN IN SWISH
% ============================================

/*
Copy and paste these queries:

1. apartmentpet(X).
2. pet(X).
3. small(X).
4. dog(X).
5. cat(X).
6. poodle(X).
*/


% ============================================
% PROGRAM 3: goodpet with AND/OR Logic
% Demonstrates: (A,B);C vs C;(A,B)
% ============================================

% FACTS
poodle(fluffy).
poodle(tommy).

cat(sushi).
cat(whiskers).

dog(rocky).

% RULES
dog(X) :- poodle(X).

pet(X) :- cat(X).
pet(X) :- dog(X).

small(X) :- poodle(X).

% VERSION 1: (pet AND small) OR cat
goodpet1(X) :- (pet(X), small(X)); cat(X).

% VERSION 2: cat OR (pet AND small)
goodpet2(X) :- cat(X); (pet(X), small(X)).

% ============================================
% QUERIES TO RUN IN SWISH
% ============================================

/*
Copy and paste these queries:

1. goodpet1(X).
2. goodpet2(X).
3. pet(X), small(X).
4. cat(X).

QUESTION: Why does sushi appear first in both versions?
ANSWER: Because sushi satisfies cat(X) which is checked first
        in the OR condition regardless of order.
*/


% ============================================
% PROGRAM 4: Sweets - Ram and Seeta
% Demonstrates: Rule chaining (transitive inference)
% ============================================

% FACTS
sweet(laddu).
sweet(gulabjam).
sweet(jalebi).
sweet(pedha).
sweet(rasmalai).

% RULES
% Ram likes all kinds of sweets
likes(ram, X) :- sweet(X).

% Seeta likes whatever Ram likes
likes(seeta, X) :- likes(ram, X).

% Additional rule: If someone likes something, they are happy
happy(Person) :- likes(Person, _).

% ============================================
% QUERIES TO RUN IN SWISH
% ============================================

/*
Copy and paste these queries:

1. likes(ram, X).
2. likes(seeta, laddu).
3. likes(seeta, X).
4. happy(ram).
5. happy(seeta).
6. sweet(laddu).
*/