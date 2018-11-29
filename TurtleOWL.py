#-*- encoding: utf-8 -*-
# TurtleOWL, a library for bootstrapping OWL ontologies.
# Copyright © 2018 Alessio Zamboni <zambotn@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


class Node(object):

    """Docstring for Node. """

    def __init__(self, uri, superclass, annotations=None):
        """TODO: to be defined1.

        :uri: uri
        :superclass: uri
        :annotations: dict(value, lang)
        """
        self._uri = uri
        self._superclass = superclass
        if annotations is None:
            self._annotations = {}
        else:
            self._annotations = annotations

    def add_annotation(self, annotation, value, lang):
        """Add notation in current class

        :annotation: annotation name
        :value: value to assign to the annotation
        :lang: language used to express the :value:
        :returns: annotation structure

        """
        self._annotations.setdefault(annotation, []).append((value, lang))
        return self._annotations[annotation]

    def to_turtle(self):
        """Return turtle string
        :returns: turtle string

        """
        txt = [u"<{}> rdf:type owl:Class".format(self._uri)]
        if self._superclass:
            txt.append(u"\trdfs:subClassOf <{}>".format(self._superclass))
        if self._annotations:
            for a, vals in self._annotations.iteritems():
                values = []
                for (val, lang) in vals:
                    if lang:
                        values.append(u"\"{}\"@{}".format(val, lang))
                    else:
                        values.append(u"\"{}\"".format(val))
                txt.append(u"\t{} {}".format(a, ",\n\t\t".join(values)))
        return ";\n".join(txt) + " .\n"



class TurtleOWL(object):

    """Bootstrap a OWL file using Turtle dialect"""

    def __init__(self, baseuri):
        """TODO: to be defined1.

        :baseuri: base uri
        """
        self._baseuri = baseuri
        self._namespaces = {}
        self.ontology = {}

    def _uri(self, name):
        """Generates a uri from classname

        :name: name of the class
        :returns: generated uri

        """
        if not name is None:
            return unicode(self._baseuri + "#" + name.replace(' ', '_'))
        else:
            return None

    def add_namespace(self, namespace, url):
        """Add namespace to the ontology

        :namespace: namespace to add
        :url: uurl of the namespace to add
        :returns: None

        """
        self._namespaces[namespace] = url

    def add_class(self, classname, superclass=None):
        """Add to a new class to the ontology

        :classname: name of the class to add
        :superclass: _optional_ superclass of the current one
        :returns: the class

        """
        cls = Node(self._uri(classname), self._uri(superclass))
        self.ontology[classname] = cls
        return cls


    def add_annotation(self, classname, annotation, value, lang=None):
        """Add an annotation to the selected class

        :classname: class name
        :annotation: annotation to add
        :value: value to assign to the annotation
        :lang: language used for expressing the value
        :returns: the modified class

        """
        cls = self.ontology[classname]
        cls.add_annotation(annotation, value, lang)
        return cls

    def to_turtle(self):
        """Format the ontology in turtle format
        :returns: return the ontology in turtle format

        """
        txt = u"@prefix : <{0}#> .\n" +\
                "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n" +\
                "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n" +\
                "@prefix xml: <http://www.w3.org/XML/1998/namespace> .\n" +\
                "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n" +\
                "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n" +\
                "\n".join(["@prefix {}: <{}>".format(ns, uri) for ns, uri in self._namespaces.iteritems()]) +\
                "@base <{0}> .\n\n" +\
                "<{0}> rdf:type owl:Ontology .\n\n"
        txt = txt.format(self._baseuri)
        for cls in self.ontology.itervalues():
            txt += cls.to_turtle()
        return txt


if __name__ == "__main__":
    owl = TurtleOWL("http://it.zambotn/Test")
    owl.add_class("myClass")
    owl.add_class("myClassChild", "myClass")
    owl.add_annotation("myClassChild", "rdfs:label", "ClasseFiglia", "it")
    owl.add_annotation("myClassChild", "rdfs:label", "ChildClass", "en")
    print owl.to_turtle()
