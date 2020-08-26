# Testing

If we integration-test, we have some stages:

* Clean storage
* Data generation
* Create objects
* Testing
* Validation
* Clean storage

If we unit-test, we have some stages: 

* Create objects
* Testing
* Validation

In this way unit-test is partial case of integration test. We use unit-test for testing 
logic in context one object, function (method). For example, we have function:

    def plus(a, b):
        return a + b
        
This is unit-test. We want to test simple object. This situation is not always possible. 
If we want communication some systems and modules, we deal with integration tests. 
For example, we test connect to data base and collect data from there. This is 
integration-tests. 
