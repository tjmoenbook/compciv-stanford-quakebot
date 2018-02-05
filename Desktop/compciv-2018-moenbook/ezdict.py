
ez_dict = {'birthdate': '1946-06-14', 'party': 'Republican',
           'gender': 'M',
           'identifiers': {
             'twitter': 'realDonaldTrump',
             'fec': 'P80001571',
           },
           'name': {'first': 'Donald', 'last': 'Trump'},
           'birthplace': {'state': 'NY', 'city': 'New York City'},
           'children': ['Donald', 'Ivanka',
                        'Eric', 'Tiffany', 'Barron'],
            'spouse': 'Melania Trump',
            'terms': [{'start_date': '2017-01-20',
                     'end_date': '2021-01-20'}]
           }



def foo_hello():
    """
    This function should simply return the `type`
     of the `ez_dict` object.

    This guarantees that you'll past at least one of
      the tests/assertions in test_ezdict.py
    """
    return type(ez_dict)


def foo_a():
    """
    Return the value that corresponds to the `'spouse'`
      property/key of ez_dict
    """



def foo_b():
    """
    Return the "first name" value
    """


def foo_bx():
    """
    Return the type of the object that
      the `'terms'` attribute points
    """


def foo_c():
    """
    Return a string that consists of the
        last and first name together, separated by a comma and
        space, e.g. 'Obama, Barack'
    """


def foo_d():
    """
    Return the number of top-level attributes in `ez_dict`
    e.g. `'name'` is a "top-level" attribute,
      but `'first'` and `'last'` are not

    """

def foo_e():
    """
    Return the number of children (based on number of names in
     the `'children'` property)
    """


def foo_f():
    """
    Return the name of the last child listed in `'children'`
    """

def foo_g():
    """
    Return a string that is a comma-delimited list of the
      names of the spouse and the children. The string
      should start with the spouse's name, followed by
      the children's names

    Hint: Think about how you can create a new list by
      adding two separate lists. Do not use the `append()`
      method.
    """

def foo_h():
    """
    Print the start date of President Trump's initial term
    """


def foo_i():
    """
    Return the age that President Trump will be
     at the end of his initial term, i.e.
     the number of full years between his `'birthdate'`
     and the `'end_date'` of his initial term

    Hint: You should be using the third-party `dateutil`
      library for this.
    """


def foo_j():
    """
    Return the full URL for the FEC.gov page for
     *candidate* President Trump.

    Example: President Obama's and VP Biden's
      FEC.gov candidacy page URL is:

      http://docquery.fec.gov/cgi-bin/fecimg/?P80003338
    """




