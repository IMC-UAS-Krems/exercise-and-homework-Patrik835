a) find all the pizzerias frequented by at least one person under the age of 18
frequents
person
P [pizzeria](frequents)-> {[pizzeria]}
How do we get persons in the equation?

Join the tables using the name as key then select all names of people

Intersection of pizzeria and people

>select underage persons

UnderAge = 5 [ age < 18] - (Person) -> (name, age, gender)

PizzaNames INTERSECT UnderAge

(pizzeria) --- (name, age, gender) ?? Imcompatible attributes

PizzaNames x UnderAge ---> (pizzeria, name , age, gender)

P [pizzeria] (PizzaNames x UnderAge) --> (pizzeria)

Patrik, 55, Male
Alan, 12, Male
Mihelle, 17, Female

Patrik, Gopizza
Alan, Gopizza
Mihelle, PizzaDomino

PizzaNames = Gopizza, PizzaDomino

UnderAge = {(Alan, 12, Male),(Mihelle, 17, Female)}

PizzaNames x UnderAge   # Count all possibilities! We need to emake sure we represent consistent

CrossProduct = len UnderAge * len PizzaNames

Gopizza(Alan, 12, Male)
Gopizza(Mihelle, 17, Female)
PizzaDomino(Alan, 12, Male)
PizzaDomino(Mihelle, 17, Female)

Result = {Gopizza, PizzaDomino}

b) find the names of all females who eat either "mushroom" or "pepperoni" but not both

Person
Eats
#we cannot do intersect
Intersect ( name, age, gender) INTERSECT (Person.name, pizza)

S[name == Person.name] - Person x Eats --> (name, age, genderm Person.name, pizza)

#project to remove duplicates
PersonEatJoins = P[name, age, gender, pizza] - Person x Eats --> (name, age, gender, pizza)
WomenPizza = S [gender = "female"] - (PersonEatJoins)

WomenPepperoni = S [pizza = "pepperoni"] - WomenPizza -->(name, age, gender, pizza)
WomenMushroom = S [pizza = "mushroom"] - WomenPizza -->(name, age, gender, pizza)

WomenMushroom U WomenPepperoni -> not good

Union of (WomenPepperoni- WomenMushroom) U (WomenMushroom - WomenPepperoni)

We can do (WomenMushroom | WomenPepperoni ) & NOT 