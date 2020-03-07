# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:41:55 2019
Use OOP to modelize restriction enzyme, and sequences.

the sequence must implement the following methods

enzyme_filter which take as a list of enzymes as argument and return a new list containing the enzymes 
which have binding site in sequence
the restriction enzyme must implements the following methods

binds which take a sequence as argument and return True if the sequence contains a binding site, False otherwise.
@author: Kz
"""

class Sequence(object):

    def __init__(self, identifier, comment, seq):
        self.id = identifier
        self.comment = comment
        self.seq = self._clean()

    def _clean(self):
        """

        :param seq:
        :return:
        """
        return self.seq.replace('\n')

    def enzyme_filter(self, enzymes):
        """

        :param enzymes:
        :return:
        """
        enzymes_which_binds = []
        for enz in enzymes:
            if enz.binds(self.seq):
                enzymes_which_binds.append(enz)
        return


class RestrictionEnzyme(object):

    def __init__(self, name, binding, cut, end, comment=''):
        self._name = name
        self._binding = binding
        self._cut = cut
        self._end = end
        self._comment = comment

    @property
    def name(self):
        return self._name

    def binds(self, seq):
        """

        :param seq:
        :return:
        """
        return self.binding in seq.seq