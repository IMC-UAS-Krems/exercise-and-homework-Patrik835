Males and Females: AND
Males or Females:  OR
Males or Females but not both: AND - OR , XOR

# Find all pizzerias that are frequented by **only** [[female]persons] or **only** [[males] persons].

S (gender == Female)    :: select individual who is female
S (gender == Male)    :: select individual who is female from person table

S (gender == Female)    :: select individual who is female from person table
S (gender == Male)    :: select individual who is female from person table

S (gender == Female) AND NOT (gender == Male)    :: select individual who is only female from person table


