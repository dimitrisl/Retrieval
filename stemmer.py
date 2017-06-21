#- * - coding: utf - 8 -*-


def stem(term):
    if len(term) >= 4:
        if term.endswith(u"ΟΥΣ") or term.endswith(u"ΕΙΣ") or term.endswith(u"ΕΩΝ") or term.endswith(u"ΟΥΝ"):
            term = term[:-3]
        # Remove the 2 letter suffixes
        elif (term.endswith(u"ΟΣ") or term.endswith(u"ΗΣ") or term.endswith(u"ΕΣ") or term.endswith(u"ΩΝ") or term.endswith(u"ΟΥ") or \
                 term.endswith(u"ΟΙ") or term.endswith(u"ΑΣ") or term.endswith(u"ΩΣ") or term.endswith(u"ΑΙ") or term.endswith(u"ΥΣ") or \
                 term.endswith(u"ΟΝ") or term.endswith(u"ΑΝ") or term.endswith(u"ΕΙ")):
            term = term[:-2]

        elif (term.endswith(u"Α") or term.endswith(u"Η") or term.endswith(u"Ο") or term.endswith(u"Ε") or term.endswith(u"Ω")\
                 or term.endswith(u"Υ") or term.endswith(u"Ι")):
            term = term[:-1]
    return term
