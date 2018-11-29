#TurtleOWL

This library is used to generate ontologies represented in _OWL_ using _Turtle_ dialect.

In order to use the library include it.

```
    import TurtleOWL

    owl = TurtleOWL("http://baseuri.example.com/MyOntology")
    
    owl.add_class("MyParentClass")
    owl.add_annotation("MyParentClass", "rdfs:label", "ParentClass")

    owl.add_class("MyChildClass", "MyParentClass")
    owl.add_annotation("MyChildClass", "rdfs:label", "ChildClass", "en")
    owl.add_annotation("MyChildClass", "rdfs:label", "ClasseFiglia", "it")

    print owl.to_turtle().encode('utf-8')
```
