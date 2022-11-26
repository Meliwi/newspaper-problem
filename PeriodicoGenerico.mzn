/*
  Newspaper general problem
   - Melissa Gonzalez Nebrijo
   - Wilmer Bautista Ochoa
   - Juan Diego Garcia
   - Jhon Carlos Valencia
*/

% Parameters
int: num_pages;
enum Topics;
array[Topics] of int: potential_readers;
array[Topics] of int: min_nb_pages;
array[Topics] of int: max_nb_pages;

% Variables
array[Topics] of var 0..1: newspaper_topics;
array[Topics] of var int: newspaper;

% Constraints
constraint sum(i in Topics)(newspaper[i]) = num_pages;
constraint forall(i in Topics)(newspaper[i] >= 0);
constraint forall(i in Topics)(newspaper_topics[i] == 1 -> newspaper[i] <= max_nb_pages[i] /\ newspaper[i] >= min_nb_pages[i]);

% Maximize potential readers
var int: f = sum(i in Topics)(newspaper_topics[i] * newspaper[i] * potential_readers[i]);

solve maximize f;
output ["Topics: \(Topics)\nChosen topics \(newspaper_topics)\nPages: \(newspaper)\nPotential readers:\(f)"]