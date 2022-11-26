/*
  Newspaper problem
   - Melissa Gonzalez Nebrijo
   - Wilmer Bautista Ochoa
   - Juan Diego Garcia
   - Jhon Carlos Valencia
*/

% Data
int: n = 5;
array[1..n] of int: potential_readers = [1500,2000,1000,1500,750];

% Decision variables
array[1..n] of var 0..1: newspaper_topics;
array[1..n] of var int: newspaper;

% Constraints
constraint sum(i in 1..n)(newspaper[i]) = 10;
constraint forall(i in 1..n)(newspaper[i] >= 0);
constraint (newspaper_topics[1] == 1 -> newspaper[1] <= 9 /\ newspaper[1] >= 5);
constraint (newspaper_topics[2] == 1 -> newspaper[2] <= 7 /\ newspaper[2] >= 4);
constraint (newspaper_topics[3] == 1 -> newspaper[3] <= 5 /\ newspaper[3] >= 2);
constraint (newspaper_topics[4] == 1 -> newspaper[4] <= 4 /\ newspaper[4] >= 2);
constraint (newspaper_topics[5] == 1 -> newspaper[5] <= 3 /\ newspaper[5] >= 1);

% Maximize potential readers
var int: f = sum(i in 1..n)(newspaper_topics[i] * newspaper[i] * potential_readers[i]);

solve maximize f;

output [" Topics: \(newspaper_topics)\n Pages: \(newspaper)\n Potential readers:\(f)"];