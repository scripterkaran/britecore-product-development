Problem
-------
**Dynamic Fields using Relation Database**

Project live URL  http://britecore-product.us-east-1.elasticbeanstalk.com/


Project:
--------
This sample application uses a relational database and allows dynamic fields in forms. Form creator can add as many fields as they want to a specific risk type.

As a Form Creator, he/she can use `FormTemplates` that are predefined by britecore team, moderators etc. These templates have fields(`FormTemplateField`) defined which can be used by form creator. 
Flow would go like this:  If form creator uses "use a template" , a new `RiskType` would be created, and new RiskTypeField would be created/copied from `FormTemplateFields`.
Now on this `RiskType` the form Creator can edit, delete and also add new fields. 

DB Design: 
![DB design](https://github.com/scripterkaran/britecore-product-development/blob/master/diagram.png)



This design structure allows flexibility in terms of form validations. 
For example using min max validators, regex check etc. 
we can define the meta JSON as

    meta : {
	    "is_required": true,
	    "min": 0
	    "max" : 100
	    "regex" : "<some-regex>"
	    ... // other 
    }

The current live project do not use these meta validations as we are not to submit form.


Reasons to not store fields as a JSON
-------------------------------------
One of the solutions I thought included storing all the fields into one JSON field.
Although JSON approach seems simple and easy to implement, It has concerning problems.

 - Saving Response from user :
 Since we have no ID specific to a field we will be not be able to map  responses of users, properly. That said, it is still possible but will be a development overhead. 
 - Updating a specific field will require a full JSON update.
 If the form is huge then a simple update will also cause memory overhead, since you would have to load the entire obj in memory.
 

Tech Stack:

 - Python with Django Framework
 - Relational Database 
 - Apache Web Server
 - Vue JS Front End
 - AWS: ElasticBeanStalk Deployment
 - VCS: Git






