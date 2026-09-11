# Class Relationships: Association and Multiplicity
## Previous Work

[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
__Class:__ Typhoon

__Description:__ This class represents tracking a typhoon with its location, signal number, windspeed and more.

## New Related Class
__Class:__ CycloneBulletin

__Description:__ This class represents showing the different levels of a typhoon/cyclone and showing a warning system in each level.

## Association
__Relationship:__ A typhoon includes a dedicated cyclone bulletin

__Explanation:__ A cyclone bulletin shows the strength of it and shows the necessary precautions we must do when hit by this typhooon/tropical storm so it is a HAS-A relationship.

## Multiplicity

__Multiplicity:__ 0..* (Zero or more)

__Explanation:__ A tropical cyclone/typhoon can have multiple bulletins as the strength of it can vary over time. Moreover, having multiple bulletins rather than only updating one can show the history of the typhoon's strength and wind signal. Lastly, a typhoon can have no cyclone bulletins if it is not inside the Philippine Area of Responsibility (PAR).

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
- The association between my classes is that a typhoon can include a cyclone bulletin. Using my actual system, you can see that a typhoon has multiple cyclone bulletins. So the relationship I used between these two classes was one to many.
### What multiplicity did you choose and why?
- I chose the multiplicity of zero or more because a typhoon can have multiple bulletins as the strength of it can vary over time. Moreover, having multiple bulletins rather than only updating one can show the history of the typhoon's strength and wind signal. Lastly, it can have no cyclone bulletins if it is not inside the Philippine Area of Responsibility (PAR).
### How did you implement the relationship in Python?
- First, I implemented the relationship in Python by creating a list inside the class Typhoon called self.bulletins. Then using a method to add/append the CycloneBulletin objects into that list. And the attribute that stores the related objects is the list self.bulletins.
### Why did you store an object reference instead of copying its data?
- I stored an object refrence instead of just copying its data in the list because if not, it would lose its functionality. An example of this from my code would be typhoon1.add_bulletin(cyclone_bulletin1). If I would only copy the class's attributes/properties of cyclone_bulletin1, I would not be able to use the methods from that class such as bulletinSummary().
### If your relationship uses many, why is a list appropriate?
- Using a list is appropriate for this because it allows you to put multiple object references in one main object from the main class. Additionally using this relationship in my code allows to see the chronological order of each cyclone bulletin of a typhoon, allowing me too see the timeline history of it. Lastly, the list contains object references to other instances/classes in my program.
