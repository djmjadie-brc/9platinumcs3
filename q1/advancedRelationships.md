# Advanced Class Relationships

## Previous Activities
[classAttributeMethods](classAttributesMethods.md)

[classRelationships](classRelationships.md)

## Existing System Description:
__Class 1:__ Typhoon

__Class 2:__ CycloneBulettin

__What problem or limitation exists in your current design:__ Problems I found were repeated attributes and repeated methods because I always did a summary of the attributes of a class while also using wind signal on both classes.

## Inheritance Relationship
__Parent:__ CycloneBulletin

__Child:__ CycloneWarningBulletin

__Explanation:__ The term "cyclone bulletins" is generalized as there are many types of bulletins when issued at a different time. A cyclone warning bulletin is implemented when a storm is epected to hit landfall in less than 24 hours. So it is considered a child class from the CycloneBulletin parent class.

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation
__Relationship:__ The realationship im using is Composition (Strong HAS-A relationship)

__Explanation:__ Because a CycloneWarningBulletin needs to own its specific alert details, such as the emergency instructions, and wind signals are created for that specific warning. If you delete the warning bulletin, the specific emergency proceudres should be deleted aswell.

## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
![Test](images/advancedTestRun.png)

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:

1. As I said before, the term "cyclone bulletins" is generalized as there are many types of bulletins when issued at a different time. A cyclone warning bulletin is implemented when a storm is epected to hit landfall in less than 24 hours. So it is considered a child class from the CycloneBulletin parent class.

2. Inheritance reduces duplicate code by allowing you to reuse properties and methods from an already existing class. Moreover, child classes already have access to those methods without declaring one again. Attributes that were reused are windSignal and BulletinNumber.

3. Like I said earlier, because a CycloneWarningBulletin needs to own its specific alert details, such as the emergency instructions, and wind signals are created for that specific warning. If you delete the warning bulletin, the specific emergency proceudres should be deleted aswell. Moreover, the relationship explained in simpler terms is that in Composition, a part can't meaningfully exist without the whole part being there.

4. In Association, the relationship between classes is that a class is shown have another sub-class inside it. On the other hand, the advanced relationship I implemented includes a class inherting properties from another class while also have an object class that has a HAS-A relationship. In other words, the difference between these is that the relationship is now directly related to each other and not just associated with one other.

5. My design follows the DRY (Don't Repeat Yourself) principle by preventing reusing code over and over again by using Inheritance instead. Additionally, when I update the main logic of the system or parent class, It automatically updates the child classes under it. So these are the reasons why my design follows the DRY principle.
